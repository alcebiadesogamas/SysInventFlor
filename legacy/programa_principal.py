import pandas as pd
# Aqui é importado o arquivo de dados excel com os estratos e a variável medida
dados = pd.read_excel('c:/Curso_Python/ACE.xlsx')
estratos = dados['Estratos'].values.tolist()
variaveis = dados['Variavel'].values.tolist()
# Aqui é criado uma lista com o número de parcelas para cada estrato (resp_dados)
import entrada_dados
nparc = entrada_dados.ent_dados(estratos)
print (nparc)
