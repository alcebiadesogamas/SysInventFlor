import pandas as pd
import random
import matplotlib.pyplot as plt
from statistics import variance, mean


class EstrategiaCasualEstratificada():
    def __init__(self, diretorio, tamanhoAmostra=0):
        self.pop = pd.read_excel(diretorio, usecols=['VAR', 'ESTRATO'], dtype={'VAR': float, 'ESTRATO': int})
        self.estratos = self.pop['ESTRATO'].values.tolist()
        self.varEstratos = self.pop['VAR'].values.tolist()
        self.paramsEstrat = self.params()
        self.pesosEstratos = self.pesos(self.paramsEstrat[1], self.estratos)
        self.nParcelas = [(round(peso * tamanhoAmostra) + 1) for peso in self.pesosEstratos]
        self.f = sum(self.nParcelas) / len(self.varEstratos)

    def params(self):
        tamanhoEstratos = list()
        estratoAtual = self.estratos[0]
        popEstrat = list()
        transitoria = list()
        cont = 0
        for indice, valor in enumerate(self.estratos):
            if valor == estratoAtual:
                cont += 1
                transitoria.append(self.varEstratos[indice])
            else:
                popEstrat.append(transitoria[:])
                transitoria.clear()
                tamanhoEstratos.append(cont)
                cont = 1
                estratoAtual = valor
        tamanhoEstratos.append(cont)
        popEstrat.append(transitoria[:])
        transitoria.clear()

        return popEstrat, tamanhoEstratos

    def colheAmostras(self) -> list:
        amostrasEstratificada = list()

        for i in range(0, len(self.nParcelas)):
            amostrasEstratificada.append((random.sample(self.paramsEstrat[0][i], self.nParcelas[i])))

        return amostrasEstratificada

    def pesos(self, tamanhoEstratos, estratos):
        pesosEstratos = list()
        for i in range(len(tamanhoEstratos)):
            pesosEstratos.append(tamanhoEstratos[i] / len(estratos))
        return pesosEstratos

    def simulacoes(self, nsim, ns, amp):
        amostraColetadas = list()
        while len(amostraColetadas) != nsim:
            parcela = self.colheAmostras()
            if parcela not in amostraColetadas:
                amostraColetadas.append(parcela)

        listVars = self.variancias(amostraColetadas)
        Gs = self.calculaGs(self.paramsEstrat[1], self.nParcelas)
        n0 = self.calculaN0(listVars, Gs, self.nParcelas)
        tabelas = list()
        for i, h in enumerate(amostraColetadas):
            tabelas.append(self.estat(h, self.nParcelas, listVars[i], self.pesosEstratos, self.paramsEstrat[1]))

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

        tabelaIC = list()
        listLimInf = list()
        listLimSup = list()
        listaErros = list()
        ttab = self.valor_t(int(ns), n0)

        if self.f < 0.05:
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

        mediaVerdadeira = sum(self.varEstratos) / len(self.varEstratos)
        tab = self.tab_freq(simulacoes, nsim, mediaVerdadeira, tabelaIC, amp)
        cont1 = tab[3]
        cont2 = tab[4]

        plt.bar(tab[1], tab[2], tick_label=tab[1])
        plt.ylabel('frequências')
        plt.xlabel('classes')
        saida = f'Intevalos de confiança bem definidos: {cont1}\n'
        saida += f'Intevalos de confiança mal definidos: {cont2}'
        plt.suptitle(saida)
        plt.show()

    def variancias(self, amostraColetadas):
        listVariancias = list()
        for simulacao in amostraColetadas:
            listVariancias.append(list(map(variance, simulacao)))
        return listVariancias

    def calculaGs(self, tamanhoEstratos, nParcelas):
        Gs = list()
        for h in range(len(tamanhoEstratos)):
            gh = (tamanhoEstratos[h] * (tamanhoEstratos[h] - nParcelas[h]))/ nParcelas[h]
            Gs.append(gh)
        return Gs

    def calculaN0(self, variancias, Gs, nParcelas):
        numerador = denominador = 0
        n0 = list()
        for i in range(len(variancias)):
            for h in range(len(variancias[i])):
                numerador += (variancias[i][h] * Gs[h])
                denominador += ((Gs[h] ** 2) * (variancias[i][h] ** 2)) / (nParcelas[h] - 1)
            n0.append(round(numerador ** 2 / denominador))
            numerador = 0
            denominador = 0
        return n0

    def estat(self, nSimulacao, nParc, vars, pesos, tamEstrato):
        tabela = list()
        N = sum(tamEstrato)
        for h in range(len(nParc)):
            med = mean(nSimulacao[h])
            wh = pesos[h]
            whMed = wh * med
            tabela.append(whMed)  # 0 whMed
            var = vars[h]
            wh2s2nh = wh**2*var/nParc[h]
            tabela.append(wh2s2nh)  # 1 Variância da média infinita
            wh2s2nhf = (wh ** 2 * var / nParc[h]) * (1 - nParc[h]/N)
            tabela.append(wh2s2nhf)  # 2 Variancia da média finita
        return tabela

    def tab_freq(self, result, nsim, medverd, tabelaIC, amp):
        t_media = []
        for i in range(0, len(result)):
            t_media.append(result[i][0])
        vmin = int(min(t_media))
        vmax = int(max(t_media))
        lic = vmin
        lsc = lic + amp
        cc = lic + amp / 2
        cclas = []
        f = []
        nfreq = []
        freq = []
        # Construindo a tabela de frequência
        while cc <= vmax:
            cclas.append(cc)
            cc = cc + amp
        if not cclas[len(cclas) - 1] == vmax:
            cclas.append(cc)
        for i in range(0, len(cclas)):
            for j in range(0, len(result)):
                if lic <= result[j][0] < lsc:
                    f.append(result[j][0])
            nfreq.append(f[:])
            freq.append(len(nfreq[i]))
            f.clear()
            lic = lic + amp
            lsc = lsc + amp
        if not freq[len(nfreq) - 1]:
            nfreq.pop()
            cclas.pop()
        cont1 = cont2 = 0
        # Calculando a frequência de acertos para o intervalo de confiança com o valor de t
        for i in range(0, nsim):
            if tabelaIC[0][i] <= medverd <= tabelaIC[1][i]:
                cont1 += 1
            else:
                cont2 += 1

        return vmin, cclas, freq, cont1, cont2

    def valor_t(self, ns, n0s):
        df_tabela_t = pd.read_excel(r'./resources/tabelat.xlsx')
        prob = df_tabela_t.columns.values
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
    ...
