import pandas as pd


class Tabela:

    def __init__(self, diretorio: str):
        self._diretorio: str = diretorio
        self._valoresTtabelado: list = []

    @property
    def diretorio(self) -> str:
        return self._diretorio

    @diretorio.setter
    def diretorio(self, value) -> None:
        self._diretorio = value

    @property
    def valoresTtabelado(self) -> list:
        return self._valoresTtabelado
        
    def setValoresTtabelado(self, nivelSignificancia, qtdNdeParcelas) -> None:
        df_tabela_t = pd.read_excel(self._diretorio)  # exemplo: 'c:/Curso_Python/tabelat.xlsx'
        prob = df_tabela_t.columns.values
        tabela_t: list = list()
        for i in range(5):
            coluna_t = df_tabela_t[prob[i]].values.tolist()
            tabela_t.append(coluna_t[:])
            coluna_t.clear()
        t1 = t2 = 0
        if nivelSignificancia == 1:
            t1 = 0
            t2 = 1
        elif nivelSignificancia == 5:
            t1 = 2
            t2 = 3
        elif nivelSignificancia == 10:
            t1 = 3
            t2 = 4
        self._valoresTtabelado.append(tabela_t[t1][qtdNdeParcelas - 2])
        self._valoresTtabelado.append(tabela_t[t2][qtdNdeParcelas - 2])


if __name__ == '__main__':
    ...