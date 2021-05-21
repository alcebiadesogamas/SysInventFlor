import math as m
import pandas as pd


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class LeitorPopulacaoSingleton(metaclass=SingletonMeta):

    def sanitizer(self, value: list) -> list:
        # er = re.compile('[a-zA-Z]')
        popfinal = [a for a in value if a.pop(0)]
        popfinal = [[float(v) for v in x] for x in popfinal]
        popfinal = [[aux for aux in x if not m.isnan(aux)] for x in popfinal]
        # for i in popfinal:
        #     print(i)
        return popfinal

    def save(self, value: list) -> None:
        n = pd.DataFrame(value)
        n.to_excel('populacao.xlsx', sheet_name='sheet', float_format='%.5f')

    def open(self, value: str, entrada: str) -> list:
        first = pd.read_excel(value, sheet_name=entrada)
        pop = first.values.tolist()
        return pop


# if __name__ == '__main__':
#     leitor = LeitorPopulacaoSingleton()
#     p = leitor.open('populacao1.xlsx', 'Entrada2')
#
#     p = leitor.sanitizer(p)
#     leitor.save(p)
