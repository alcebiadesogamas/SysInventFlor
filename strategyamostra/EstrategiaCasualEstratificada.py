from model.Populacao import Populacao
import pandas as pd
from strategyamostra.EstrategiaAmostragem import EstrategiaAmostragem
import random

class EstrategiaCasualEstratificada(EstrategiaAmostragem):


    def colheAmostras(self, populacao: Populacao=None, tamanhoAmostra=0) -> list:
        pop = pd.read_excel('C:/Users/Gilson/Documents/Projeto_SysInventFlor/SysInventFlor/resources/pop.xlsx', usecols=['VAR', 'ESTRATO'], dtype={'VAR': float, 'ESTRATO': int})
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
            transitoria.append(random.sample(popEstrat[i], nParcelas[i]))
            amostrasEstratificada.append(transitoria[:])
            transitoria.clear()





    def pesos(self, tamanhoEstratos, estratos):
        pesosEstratos = list()
        for i in range(len(tamanhoEstratos)):
            pesosEstratos.append(tamanhoEstratos[i] / len(estratos))
        return pesosEstratos


if __name__ == '__main__':
    ce = EstrategiaCasualEstratificada()
    ce.colheAmostras(tamanhoAmostra=20)


