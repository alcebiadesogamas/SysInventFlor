class Populacao:

    def __init__(self, totalParcelas=0, areaTotal=0) -> None:
        self._totalParcelas: int = totalParcelas
        self._areaTotal: float = areaTotal
        self._tipo: str = ''

    @property
    def totalParcelas(self) -> int:
        return self._totalParcelas

    @totalParcelas.setter
    def totalParcelas(self, N) -> None:
        self._totalParcelas = N

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
