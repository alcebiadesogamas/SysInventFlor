import model.Tabela as tabela
import pandas as pd

def getAmostrasEstratificada():
    tb = tabela.Tabela(diretorio='C:/Users/Gilson/Documents/Projeto_SysInventFlor/SysInventFlor/resources/tabelat.xlsx')
    amostraACE = pd.read_excel(r'C:\Users\Gilson\Documents\Projeto_SysInventFlor\SysInventFlor\resources\ACE.xlsx', usecols=['Estratos', 'Variavel', 'Area'], dtype={'Estratos': int, 'Variavel': float, 'Area': float})
    areas = amostraACE['Area'].values.tolist()
    variavel = amostraACE['Variavel'].values.tolist()
    estratos = amostraACE['Estratos'].values.tolist()

    areaEstrato = list()
    aux = areas[0]
    areaEstrato.append(aux)
    for i in range(len(areas)):
        if areas[i] != aux:
            areaEstrato.append(areas[i])
            aux = areas[i]
    totalAreaEstrato = sum(areaEstrato)


if __name__ == '__main__':
    getAmostrasEstratificada()