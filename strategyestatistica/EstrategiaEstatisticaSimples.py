import numpy as np
from model.Estatistica import Estatistica
from model.Tabela import Tabela
from model.Populacao import Populacao


class HandlerEstatistica:

    def __init__(self, estatistica: Estatistica, ttabelado: Tabela, amostra: list, populacao: Populacao,
                nivelSignificancia: float):
      self.estatistica: Estatistica = estatistica
      self.amostra = amostra
      self.ttabelado = ttabelado
      self.populacao = populacao
      self.nivelSignificancia = nivelSignificancia

    def calculate(self):
      self.estatistica.tamAmostra = len(self.amostra)
      self.estatistica.areaParcela = self.populacao.areaParcelas
      self.estatistica.AreaTotal = round(self.populacao.areaTotal/(self.populacao.areaParcelas/10000))
      self.estatistica.ttab = self.ttabelado.valoresTtabelado
      self.estatistica.somatorio = np.sum(self.amostra)
      self.estatistica.somatorioQuadrado = np.sum(np.power(self.amostra, 2))
      self.estatistica.media = np.mean(self.amostra)
      self.estatistica.variancia = np.var(self.amostra)
      self.estatistica.desvioPadrao = np.std(self.amostra)

      self.estatistica.coeficienteDeVariacao = (self.estatistica.desvioPadrao / self.estatistica.media) * 100
      self.estatistica.fFracaoDeAmostragem = (len(self.amostra) / self.populacao.totalParcelas)

      if self.estatistica.fFracaoDeAmostragem <= 0.05:
          self.populacao.tipo = 'Finita'
          self.estatistica.varianciaDaMedia = (self.estatistica.variancia / len(self.amostra))
      else:
          self.populacao.tipo = 'Infinita'
          self.estatistica.varianciaDaMedia = (self.estatistica.variancia / len(self.amostra)) * (1 - self.estatistica.fFracaoDeAmostragem)
      self.estatistica.erroPadraoDaMedia = self.estatistica.varianciaDaMedia ** (1 / 2)
      self.estatistica.erroDeAmostragemAbsoluto = self.estatistica.erroPadraoDaMedia * self.ttabelado.valoresTtabelado[0]
      self.estatistica.erroDeAmostragemRelativo = (self.estatistica.erroDeAmostragemAbsoluto / self.estatistica.media) * 100
      self.estatistica.nivelSignificancia = self.nivelSignificancia

