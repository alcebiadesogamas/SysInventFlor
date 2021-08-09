from model.Populacao import Populacao
import pandas as pd
from strategyamostra.EstrategiaAmostragem import EstrategiaAmostragem
import random
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

    def simulacoes(self, tamAmostra, nsim, diretorio):
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
        print(vars)
        # self.estat(amostraColetadas, nParcelas, vars, pesos, tamanhoEstratos)


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
            n0.append(numerador ** 2 / denominador)
            numerador = 0
            denominador = 0
        return n0

    def estat(self, nSimulacao, nParc, vars, pesos, tamEstrato):
        parcial = list()
        tabela = list()
        N = sum(tamEstrato)
        for i in range(len(nSimulacao)):
            for j in range(len(nParc)):
                wh = pesos[j]
                med = mean(nSimulacao[j])
                whMed = wh * med
                parcial.append(whMed)  # 0
                var = vars[i][j]
                print(var)
            #     desvpad = var**(1/2)
            #     parcial.append(desvpad)  # 1
            #     parcial.append(var) # 2
            #     wh2s2nh = wh**2*var/nParc[i]
            #     parcial.append(wh2s2nh)  # 3 Variância da média infinita
            #     wh2s2nhf = (wh ** 2 * var / nParc[i]) * (1 - nParc[i]/N)
            #     parcial.append(wh2s2nhf)  # 4 Variancia da média finita
            #     tabela.append(parcial[:])  # 5
            #     parcial.clear()
            # return tabela

if __name__ == '__main__':
    ce = EstrategiaCasualEstratificada()
    # ce.colheAmostras(tamanhoAmostra=20,diretorio=r'C:\Users\Gilson\Documents\Projeto_SysInventFlor\SysInventFlor\resources\pop.xlsx')
    # a = [[[15.8, 7.6, 8.8, 12.5, 11.1, 16.2, 12.2], [20.4, 30.5, 30.7, 27.2, 28.4, 19.7, 20.4, 23.1], [21.3, 24.3, 29.2, 21.8, 33.1, 35.8, 26.7]], [[15.8, 7.6, 8.8, 12.5, 11.1, 16.2, 12.2], [20.4, 30.5, 30.7, 27.2, 28.4, 19.7, 20.4, 23.1], [21.3, 24.3, 29.2, 21.8, 33.1, 35.8, 26.7]]]
    ce.simulacoes(tamAmostra=20, nsim=2, diretorio=r'C:\Users\Gilson\Documents\Projeto_SysInventFlor\SysInventFlor\resources\pop.xlsx')
