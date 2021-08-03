import pandas as pd
def GL(tabela, N, ns):
    df_tabela_t = pd.read_excel('./resources/tabelat.xlsx')
    prob = (df_tabela_t.columns.values)
    tabela_t: list = list()
    for i in range(5):
        coluna_t = df_tabela_t[prob[i]].values.tolist()
        tabela_t.append(coluna_t[:])
        coluna_t.clear()

    resultados = list()
    ttab = list()
    medestrat = vmfi = vminfi = vestrat = dpestrat = iam = wt = s1 = den = n = 0
    for i in range(0, len(tabela)):
        medestrat = medestrat + tabela[i][3] * tabela[i][4]
        n = n + tabela[i][1]
        wt = wt + tabela[i][3]
        dpestrat = dpestrat + tabela[i][7]
        vestrat = vestrat + tabela[i][8]
        iam = iam + tabela[i][9]
        vminfi = vminfi + tabela[i][10]
        vmfi = vmfi + tabela[i][11]
    # Cálculo do numerador e denominador da fórmula de graus de liberdade ponderado
        s1 = s1 + ((tabela[i][2]*(tabela[i][2] - tabela[i][1]))/tabela[i][1])*tabela[i][6]
        den = den + (((tabela[i][2]*(tabela[i][2] - tabela[i][1]))/tabela[i][1])**2*tabela[i][6]**2)/(tabela[i][1] - 1)
    resultados.append('Total')  # 0
    resultados.append(n)  # 1
    resultados.append(N)  # 2
    resultados.append(1.0000)  # 3
    resultados.append(medestrat)  # 4
    resultados.append('-')   # 5
    resultados.append('-')  # 6
    resultados.append(dpestrat)  # 7
    resultados.append(vestrat)  # 8
    resultados.append(iam)  # 9
    resultados.append(vminfi)  # 10
    resultados.append(vmfi)  # 11
    if s1**2 % den == 0:
        gl = int(s1 ** 2 // den)
    else:
        gl = int(s1 ** 2 // den + 1)

    if ns == 1:
        t1 = 0
        t2 = 1
    elif ns == 5:
        t1 = 2
        t2 = 3
    elif ns == 10:
        t1 = 3
        t2 = 4
    ttab1 = tabela_t[t1][gl - 1]
    ttab2 = tabela_t[t2][gl - 1]
    ttab.append(ns) # 0
    ttab.append(gl) # 1
    ttab.append(ttab1) # 2
    ttab.append(ttab2) # 3

    f = n/N
    if f < 0.05:
        eaa = (resultados[10] ** (1/2)) * ttab[2]
        estimativaMinimaDeConfiancaErro = (resultados[10] ** (1/2)) * ttab[3]
    else:
        eaa = (resultados[11] ** (1 / 2)) * ttab[2]
        estimativaMinimaDeConfiancaErro = (resultados[11] ** (1 / 2)) * ttab[3]

    return resultados, ttab, eaa, estimativaMinimaDeConfiancaErro, gl, N


