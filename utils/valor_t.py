def t_tabelado(ns, n):
    import pandas as pd
    df_tabela_t = pd.read_excel('tabelat.xlsx')
    prob = (df_tabela_t.columns.values)
    tabela_t = list()
    for i in range(0, 5):
        coluna_t = df_tabela_t[prob[i]].values.tolist()
        tabela_t.append(coluna_t[:])
        coluna_t.clear()
    if ns == 1:
        t1 = 0
        t2 = 1
    elif ns == 5:
        t1 = 2
        t2 = 3
    elif ns == 10:
        t1 = 3
        t2 = 4
    ttab1 = tabela_t[t1][n - 2]
    ttab2 = tabela_t[t2][n - 2]
    return ttab1, ttab2
