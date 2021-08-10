from model.Populacao import Populacao
import pandas as pd
from strategyamostra.EstrategiaAmostragem import EstrategiaAmostragem
import random
import matplotlib.pyplot as plt
from statistics import variance, mean

class EstrategiaCasualEstratificada(EstrategiaAmostragem):

    def colheAmostras(self, tamanhoAmostra=0, diretorio='') -> list:
        pop = pd.read_excel(diretorio, usecols=['VAR', 'ESTRATO'], dtype={'VAR': float, 'ESTRATO': int})
        tamanhoEstratos = list()
        estratos = pop['ESTRATO'].values.tolist()
        varEstratos = pop['VAR'].values.tolist()
        estratoAtual = estratos[0]
        popEstrat = list()
        transitoria = list()

        cont = 0
        for indice, valor in enumerate(estratos):
            if valor == estratoAtual:
                cont += 1
                transitoria.append(varEstratos[indice])
            else:
                popEstrat.append(transitoria[:])
                transitoria.clear()
                tamanhoEstratos.append(cont)
                cont = 1
                estratoAtual = valor
        tamanhoEstratos.append(cont)
        popEstrat.append(transitoria[:])
        transitoria.clear()

        pesosEstratos = self.pesos(tamanhoEstratos, estratos)
        nParcelas = [(round(peso * tamanhoAmostra) + 1) for peso in pesosEstratos]
        amostrasEstratificada = list()

        for i in range(0, len(nParcelas)):
            amostrasEstratificada.append((random.sample(popEstrat[i], nParcelas[i])))

        return [amostrasEstratificada, tamanhoEstratos, nParcelas, pesosEstratos]

    def pesos(self, tamanhoEstratos, estratos):
        pesosEstratos = list()
        for i in range(len(tamanhoEstratos)):
            pesosEstratos.append(tamanhoEstratos[i] / len(estratos))
        return pesosEstratos

    def simulacoes(self, tamAmostra, nsim, diretorio, ns):
        pop = pd.read_excel(diretorio, usecols=['VAR', 'ESTRATO'], dtype={'VAR': float, 'ESTRATO': int})
        varEstratos = pop['VAR'].values.tolist()

        amostraColetadas = list()
        while len(amostraColetadas) != nsim:
            colheita = self.colheAmostras(tamanhoAmostra=tamAmostra, diretorio=diretorio)
            parcela = colheita[0]
            tamanhoEstratos = colheita[1]
            nParcelas = colheita[2]
            pesos = colheita[3]
            if parcela not in amostraColetadas:
                amostraColetadas.append(parcela)

        vars = self.variancias(amostraColetadas)
        Gs = self.calculaGs(tamanhoEstratos, nParcelas)
        n0 = self.calculaN0(vars, Gs, nParcelas)
        tabelas = list()
        for i, h in enumerate(amostraColetadas):
            tabelas.append(self.estat(h, nParcelas, vars[i], pesos, tamanhoEstratos))

        simulacoes = list()
        transitoria = list()

        somaMediaEstratificada = somaVarFinita = somaVarInfinita = 0

        for tabela in tabelas:
            # para somaMediaEstratificada
            for j in range(0, len(tabela), 3):
                somaMediaEstratificada += tabela[j]
            # para somaVarInfinita
            for k in range(1, len(tabela), 3):
                somaVarInfinita += tabela[k]
            # para somaVarFinita
            for w in range(2, len(tabela), 3):
                somaVarFinita += tabela[w]
            transitoria.append(somaMediaEstratificada)
            transitoria.append(somaVarInfinita)
            transitoria.append(somaVarFinita)
            simulacoes.append(transitoria[:])
            transitoria.clear()
            somaMediaEstratificada = 0
            somaVarInfinita = 0
            somaVarFinita = 0

        f = sum(nParcelas) / len(varEstratos)
        tabelaIC = list()
        listLimInf = list()
        listLimSup = list()
        listaErros = list()
        ttab = self.valor_t(ns, n0)

        if f < 0.05:
            for i in range(nsim):
                eaa = (simulacoes[i][1] ** (1 / 2)) * ttab[i]
                limInf = simulacoes[i][0] - eaa
                listLimInf.append(limInf)
                listaErros.append(eaa)
                limSup = simulacoes[i][0] + eaa
                listLimSup.append(limSup)
        else:
            for i in range(nsim):
                eaa = (simulacoes[i][2] ** (1 / 2)) * ttab[i]
                limInf = simulacoes[i][0] - eaa
                listLimInf.append(limInf)
                listaErros.append(eaa)
                limSup = simulacoes[i][0] + eaa
                listLimSup.append(limSup)
        tabelaIC.append(listLimInf[:])
        tabelaIC.append(listLimSup[:])


        mediaVerdadeira = sum(varEstratos) / len(varEstratos)
        tab = self.tab_freq(simulacoes, nsim, mediaVerdadeira, tabelaIC)
        cont1 = tab[4]
        cont2 = tab[5]
        print(f'cont1 = {cont1}', f'cont2 = {cont2}')
        print(tab)
        plt.bar(tab[2], tab[3])
        plt.show()



    def variancias(self, amostraColetadas):
        vars = list()
        for simulacao in amostraColetadas:
            vars.append(list(map(variance, simulacao)))
        return vars

    def calculaGs(self, tamanhoEstratos, nParcelas):
        Gs = list()
        for h in range(len(tamanhoEstratos)):
            gh = (tamanhoEstratos[h] * (tamanhoEstratos[h] - nParcelas[h]))/ nParcelas[h]
            Gs.append(gh)
        return Gs

    def calculaN0(self, vars, Gs, nParcelas):
        numerador = denominador = 0
        n0 = list()
        for i in range(len(vars)):
            for h in range(len(vars[i])):
                numerador += (vars[i][h] * Gs[h])
                denominador += ((Gs[h] ** 2) * (vars[i][h] ** 2)) / (nParcelas[h] - 1)
            n0.append(round(numerador ** 2 / denominador))
            numerador = 0
            denominador = 0
        return n0

    def estat(self, nSimulacao, nParc, vars, pesos, tamEstrato):
        parcial = list()
        tabela = list()
        N = sum(tamEstrato)
        for h in range(len(nParc)):
            med = mean(nSimulacao[h])
            wh = pesos[h]
            whMed = wh * med
            tabela.append(whMed)  # 0 whMed
            var = vars[h]
            desvpad = var**(1/2)
            wh2s2nh = wh**2*var/nParc[h]
            tabela.append(wh2s2nh)  # 1 Variância da média infinita
            wh2s2nhf = (wh ** 2 * var / nParc[h]) * (1 - nParc[h]/N)
            tabela.append(wh2s2nhf)  # 2 Variancia da média finita
        return tabela

    def tab_freq(self, result, nsim, medverd, tabelaIC):
        t_media = []
        for i in range(0, len(result)):
            t_media.append(result[i][0])
            vmin = int(min(t_media))
        vmax = int(max(t_media))
        a = 1  # float(input('Digite a amplitude da classe: '))
        lic = vmin
        lsc = lic + a
        cc = lic + a / 2
        cclas = []
        f = []
        nfreq = []
        freq = []
        # Construindo a tabela de frequência
        while cc <= vmax:
            cclas.append(cc)
            cc = cc + a
        if not cclas[len(cclas) - 1] == vmax:
            cclas.append(cc)
        for i in range(0, len(cclas)):
            for j in range(0, len(result)):
                if result[j][0] >= lic and result[j][0] < lsc:
                    f.append(result[j][0])
            nfreq.append(f[:])
            freq.append(len(nfreq[i]))
            f.clear()
            lic = lic + a
            lsc = lsc + a
        if freq[len(nfreq) - 1] == []:
            nfreq.pop()
            cclas.pop()
        cont1 = cont2 = cont3 = cont4 = 0
        # Calculando a frequência de acertos para o intervalo de confiança com o valor de t
        for i in range(0, nsim):
            if medverd >= tabelaIC[0][i] and medverd <= tabelaIC[1][i]:
                cont1 = cont1 + 1
            else:
                cont2 = cont2 + 1

        return vmin, a, cclas, freq, cont1, cont2

    def valor_t(self, ns, n0s):
        df_tabela_t = pd.read_excel(r'C:\Users\Nubia\Documents\SysInventFlor\resources\tabelat.xlsx')
        prob = (df_tabela_t.columns.values)
        tabela_t: list = list()
        for i in range(5):
            coluna_t = df_tabela_t[prob[i]].values.tolist()
            tabela_t.append(coluna_t[:])
            coluna_t.clear()

        ttab = list()
        t1 = 0
        if ns == 1:
            t1 = 0
        elif ns == 5:
            t1 = 2
        elif ns == 10:
            t1 = 3

        for i in range(len(n0s)):
            nAmostra = n0s[i] - 1
            ttab.append(tabela_t[t1][nAmostra])
        return ttab

if __name__ == '__main__':
    ce = EstrategiaCasualEstratificada()
    # ce.colheAmostras(tamanhoAmostra=20,diretorio=r'C:\Users\Gilson\Documents\Projeto_SysInventFlor\SysInventFlor\resources\pop.xlsx')
    # a = [[[15.8, 7.6, 8.8, 12.5, 11.1, 16.2, 12.2], [20.4, 30.5, 30.7, 27.2, 28.4, 19.7, 20.4, 23.1], [21.3, 24.3, 29.2, 21.8, 33.1, 35.8, 26.7]], [[15.8, 7.6, 8.8, 12.5, 11.1, 16.2, 12.2], [20.4, 30.5, 30.7, 27.2, 28.4, 19.7, 20.4, 23.1], [21.3, 24.3, 29.2, 21.8, 33.1, 35.8, 26.7]]]
    ce.simulacoes(tamAmostra=20, nsim=10000, diretorio=r'C:\Users\Nubia\Documents\SysInventFlor\resources\pop.xlsx', ns=10)
