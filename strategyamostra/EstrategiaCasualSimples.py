from strategyestatistica.StrategySimple import estatistica
from model.Tabela import Tabela
import pandas as pd
import matplotlib.pyplot as plt
import random


def tab_freq(result, nsim, medverd):
    t_media = []
    for i in range(0, len(result)):
        t_media.append(result[i][0])
        vmin = int(min(t_media))
    vmax = int(max(t_media))
    a = 1 #float(input('Digite a amplitude da classe: '))
    lic = vmin
    lsc = lic + a
    cc = lic + a / 2
    cclas = []
    f = []
    nfreq = []
    freq = []
    # Construindo a tabela de frequência
    while cc <= vmax:
        cclas.append(cc)
        cc = cc + a
    if not cclas[len(cclas) - 1] == vmax:
        cclas.append(cc)
    for i in range(0, len(cclas)):
        for j in range(0, len(result)):
            if result[j][0] >= lic and result[j][0] < lsc:
                f.append(result[j][0])
        nfreq.append(f[:])
        freq.append(len(nfreq[i]))
        f.clear()
        lic = lic + a
        lsc = lsc + a
    if freq[len(nfreq) - 1] == []:
        nfreq.pop()
        cclas.pop()
    cont1 = cont2 = cont3 = cont4 = 0
    # Calculando a frequência de acertos para o intervalo de confiança com o valor de t
    for i in range(0, nsim):
        if medverd >= result[i][5] and medverd <= result[i][6]:
            cont1 = cont1 + 1
        else:
            cont2 = cont2 + 1
    # Calculando a frequência de acertos para o intervalo de confiança sem o valor de t
    for i in range(0, nsim):
        if medverd >= result[i][9] and medverd <= result[i][10]:
            cont3 = cont3 + 1
        else:
            cont4 = cont4 + 1
    return vmin, a, cclas, freq, cont1, cont2, cont3, cont4

def excuteAll(n, nsim, nst, caminho):  
    dados = pd.read_excel(caminho)
    variavel = dados['VAR'].values.tolist()
    lista2 = []
    parcelas = []
    while len(lista2) != nsim:
        parcelas = random.sample(variavel, n)
        if parcelas not in lista2:
            lista2.append(parcelas[:])
        parcelas.clear()


    tb = Tabela(diretorio='./resources/tabelat.xlsx')
    tb.setValoresTtabelado(nst, n)
    valor_t = tb.valoresTtabelado

    result = estatistica(lista2, variavel, nsim, valor_t[0])
    lmedias = []
    for i in range(0, len(result)):
        lmedias.append(result[i][0])

    medverd = sum(variavel) / len(variavel)
    tab = tab_freq(result, nsim, medverd)
    vmin = tab[0]
    a = tab[1]
    tcclas = tab[2].copy()
    freq = tab[3].copy()
    cont1 = tab[4]
    cont2 = tab[5]
    cont3 = tab[6]
    cont4 = tab[7]
    # print()
    # print('  DISTRIBUIÇÃO DE FREQUÊNCIA DAS MÉDIAS   ')
    # print('-' * 30)
    # print('   CLASSE', end=' ')
    # print('     CENTRO', end=' ')
    # print('    fi')
    # print('-' * 30)
    lic = float(vmin)
    lsc = lic + a
    f = 0
    for i in range(0, len(tcclas)):
        # print(f'{lic:<4} ← {lsc:>4}    ', end=' ')
        # print(f'{tcclas[i]:<6}   ', end=' ')
        f = freq[i]
        # print(f'{f:<4} ')
        lic = lic + a
        lsc = lsc + a
    # print('-' * 30)
    # print(f'Os Intevalos de confiança bem definidos com o valor de t foram: {cont1}')
    # print(f'Os Intevalos de confiança mal definidos com o valor de t foram: {cont2}')
    plt.bar(tcclas, freq)
    plt.show()
    # print()
    # optab = str(input('>>>>>>>>>> Você gostaria de avaliar o efeito do valor de t tabelado[S/N]?'))
    # print()
    # while optab not in 'snSN':
    #     print('Opção Inválida: Tente Outra vez.')
    #     optab = str(input('>>>>>>>>>> Você gostaria de avaliar o efeito do valor de t tabelado[S/N]?'))
    # if optab == 's' or optab == 'S':
    #     print(f'Os Intevalos de confiança bem definidos sem o valor de t foram: {cont3}')
    #     print(f'Os Intevalos de confiança mal definidos sem o valor de t foram: {cont4}')

if __name__ == '__main__':
    excuteAll(20, 10000, 0.05)