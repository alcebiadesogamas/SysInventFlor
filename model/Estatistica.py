

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
        self.ttab = 0.0
        self.nivelSignificancia = 0.0
        self.tamAmostra = 0.0

    # @property
    # def media(self):
    #     return self.media

    # @media.setter
    # def media(self, value):
    #     self.media = value

    # @property
    # def somatorio(self):
    #     return self.somatorio

    # @somatorio.setter
    # def somatorio(self, value):
    #     self.somatorio = value

    # @property
    # def SomatorioQuadrado(self):
    #     return self.somatorioQuadrado

    # @SomatorioQuadrado.setter
    # def SomatorioQuadrado(self, value):
    #     self.somatorioQuadrado = value

    # @property
    # def desvioPadrao(self):
    #     return self.desvioPadrao

    # @desvioPadrao.setter
    # def desvioPadrao(self, value):
    #     self.desvioPadrao = value

    # @property
    # def variancia(self):
    #     return self.variancia

    # @variancia.setter
    # def variancia(self, value):
    #     self.variancia = value

    # @property
    # def coeficienteDeVariacao(self):
    #     return self.coeficienteDeVariacao

    # @coeficienteDeVariacao.setter
    # def coeficienteDeVariacao(self, value):
    #     self.coeficienteDeVariacao = value

    # @property
    # def varianciaDaMedia(self):
    #     return self.varianciaDaMedia

    # @varianciaDaMedia.setter
    # def varianciaDaMedia(self, value):
    #     self.varianciaDaMedia = value

    # @property
    # def erroPadraoDaMedia(self):
    #     return self.erroPadraoDaMedia

    # @erroPadraoDaMedia.setter
    # def erroPadraoDaMedia(self, value):
    #     self.erroPadraoDaMedia = value

    # @property
    # def erroDeAmostragemAbsoluto(self):
    #     return self.erroDeAmostragemAbsoluto

    # @erroDeAmostragemAbsoluto.setter
    # def erroDeAmostragemAbsoluto(self, value):
    #     self.erroDeAmostragemAbsoluto = value

    # @property
    # def erroDeAmostragemRelativo(self):
    #     return self.erroDeAmostragemRelativo

    # @erroDeAmostragemRelativo.setter
    # def erroDeAmostragemRelativo(self, value):
    #     self.erroDeAmostragemRelativo = value

    # @property
    # def fFracaoDeAmostragem(self):
    #     return self.fFracaoDeAmostragem

    # @fFracaoDeAmostragem.setter
    # def fFracaoDeAmostragem(self, value):
    #     self.fFracaoDeAmostragem = value

    # @property
    # def fatorDeCorrecao(self):
    #     return self.fatorDeCorrecao

    # @fatorDeCorrecao.setter
    # def fatorDeCorrecao(self, value):
    #     self.fatorDeCorrecao = value
