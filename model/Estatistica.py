

class Estatistica:
    
    def __init__(self):
      self.media: float = 0.0
      self.somatorio: float = 0.0
      self.somatorioQuadrado: float = 0.0
      self.desvioPadrao: float = 0.0
      self.variancia: float = 0.0
      self.coeficienteDeVariacao: float = 0.0
      self.varianciaDaMedia: float = 0.0
      self.erroPadraoDaMedia: float = 0.0
      self.erroDeAmostragemAbsoluto: float = 0.0
      self.erroDeAmostragemRelativo: float = 0.0
      self.fFracaoDeAmostragem: float = 0.0
      self.fatorDeCorrecao: float = 0.0
      self.ttab: list = None
      self.nivelSignificancia = 0.0
      self.tamAmostra = 0.0
      self.areaParcela = 0.0
      self.AreaTotal = 0.0

