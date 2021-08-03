class Populacao:

    def __init__(self, areaParcelas=0, areaTotal=0) -> None:
        self._areaParcelas: float = areaParcelas
        self._areaTotal: float = areaTotal
        self._totalParcelas: float = areaTotal/areaParcelas
        self._tipo: str = ''

    @property
    def totalParcelas(self) -> float:
        return self._totalParcelas

    @totalParcelas.setter
    def totalParcelas(self, value) -> None:
        self._totalParcelas = value

    @property
    def areaParcelas(self) -> float:
        return self._areaParcelas

    @areaParcelas.setter
    def areaParcelas(self, N) -> None:
        self._areaParcelas = N

    @property
    def areaTotal(self) -> float:
        return self._areaTotal

    @areaTotal.setter
    def areaTotal(self, areatotal) -> None:
        self._areaTotal = areatotal

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, value) -> None:
        self._tipo = value
