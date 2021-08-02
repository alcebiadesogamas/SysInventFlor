def GL(tabela, tabela_t, n, N):
    resultados = list()
    ttab = list()
    medestrat = vmfi = vminfi = vestrat = dpestrat = iam = wt = s1 = den = 0
    for i in range(0, len(tabela)):
        medestrat = medestrat + tabela[i][3] * tabela[i][4]
        wt = wt + tabela[i][3]
        dpestrat = dpestrat + tabela[i][7]
        vestrat = vestrat + tabela[i][8]
        iam = iam + tabela[i][9]
        vminfi = vminfi + tabela[i][10]
        vmfi = vmfi + tabela[i][11]    
    # Cálculo do numerador e denominador da fórmula de graus de liberdade ponderado
        s1 = s1 + ((tabela[i][2]*(tabela[i][2] - tabela[i][1]))/tabela[i][1])*tabela[i][6]
        den = den + (((tabela[i][2]*(tabela[i][2] - tabela[i][1]))/tabela[i][1])**2*tabela[i][6]**2)/(tabela[i][1] - 1)
    resultados.append('Total')
    resultados.append(n)
    resultados.append(N)
    resultados.append(1.0000)
    resultados.append(medestrat)
    resultados.append('-')
    resultados.append('-')
    resultados.append(dpestrat)
    resultados.append(vestrat)
    resultados.append(iam)
    resultados.append(vminfi)
    resultados.append(vmfi)
    if s1**2 % den == 0:
        gl = int(s1 ** 2 // den)
    else:
        gl = int(s1 ** 2 // den + 1)               
    ns = int(input('Informe o nível de significância [1%, 5% ou 10%]: '))
    print()
    while True:
        if ns != 10 and ns != 5 and ns != 1:
            print('OPÇÃO INVÁLIDA. TENTE OUTRA VEZ!!!!')
            ns = int(input('Informe o nível de significância [1%, 5% ou 10%]: '))
        else:
            break
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
    ttab.append(ns)
    ttab.append(gl)
    ttab.append(ttab1)
    ttab.append(ttab2)
    return resultados, ttab


