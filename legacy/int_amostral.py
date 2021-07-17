def calc_int_amostral(tabela, tabela_t, result, nparc, metodo, f, ns, n, E):
# Aqui começa o cálculo do método proporcional
    if metodo == 1:
# Aqui começa o cálculo do método proporcional população infinita
        if f <= 0.05:
            if ns == 1:
                t1 = 0
            elif ns == 5:
                t1 = 2
            elif ns == 10:
                t1 = 3       
            ttab3 = tabela_t[t1][n - 2]
            if (ttab3**2*result[0][8])%(result[0][4]*E)**2 == 0:
                n_otimo1 = int((ttab3**2*result[0][8])//(result[0][4]*E)**2)
            else:
                n_otimo1 = int((ttab3**2*result[0][8])//(result[0][4]*E)**2 + 1)        
            ttab3 = tabela_t[t1][n_otimo1 - 2]
            if (ttab3**2*result[0][8])%(result[0][4]*E)**2 == 0:
                n_otimo2 = int((ttab3**2*result[0][8])//(result[0][4]*E)**2)
            else:
                n_otimo2 = int((ttab3**2*result[0][8])//(result[0][4]*E)**2 + 1)        
            ttab3 = tabela_t[t1][n_otimo2 - 2]
            for i in range(0, 20):
                if n_otimo1 == n_otimo2:
                    for i in range(0, len(nparc)):
                        nparc_estrato = (tabela[i][3]*n_otimo2)
                        inteiro = nparc_estrato // 1
                        resto = nparc_estrato % 1
                        if resto == 0:
                            print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                        else:
                            print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
                    break
                else:
                    n_otimo1 = n_otimo2
                    if (ttab3**2*result[0][8])%(result[0][4]*E)**2 == 0:
                        n_otimo2 = int((ttab3**2*result[0][8])//(result[0][4]*E)**2)
                    else:
                        n_otimo2 = int((ttab3**2*result[0][8])//(result[0][4]*E)**2 + 1)             
                ttab3 = tabela_t[t1][n_otimo2 - 2]
            if n_otimo2 - n_otimo1 < 3 and n_otimo2 != n_otimo1:
                for i in range(0, len(nparc)):
                    nparc_estrato = (tabela[i][3]*n_otimo2)
                    inteiro = nparc_estrato // 1
                    resto = nparc_estrato % 1
                    if resto == 0:
                        print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                    else:
                        print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
# Aqui começa o cálculo do método proporcional população finita      
        else:
            if ns == 1:
                t1 = 0
            elif ns == 5:
                t1 = 2
            elif ns == 10:
                t1 = 3       
            ttab3 = tabela_t[t1][n - 2]
            if (ttab3**2*result[0][8])%((result[0][4]*E)**2 + ttab3**2*result[0][9]) == 0:
                n_otimo1 = int((ttab3**2*result[0][8])//((result[0][4]*E)**2 + ttab3**2*result[0][9]))
            else:
                n_otimo1 = int((ttab3**2*result[0][8])//((result[0][4]*E)**2 + ttab3**2*result[0][9]) + 1)        
            ttab3 = tabela_t[t1][n_otimo1 - 2]
            if (ttab3**2*result[0][8])%((result[0][4]*E)**2 + ttab3**2*result[0][9]) == 0:
                n_otimo2 = int((ttab3**2*result[0][8])//((result[0][4]*E)**2 + ttab3**2*result[0][9]))
            else:
                n_otimo2 = int((ttab3**2*result[0][8])//((result[0][4]*E)**2 + ttab3**2*result[0][9]) + 1)        
            ttab3 = tabela_t[t1][n_otimo2 - 2]
            for i in range(0, 20):
                if n_otimo1 == n_otimo2:
                    for i in range(0, len(nparc)):
                        nparc_estrato = (tabela[i][3]*n_otimo2)
                        inteiro = nparc_estrato // 1
                        resto = nparc_estrato % 1
                        if resto == 0:
                            print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                        else:
                            print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
                    break
                else:
                    n_otimo1 = n_otimo2
                    if (ttab3**2*result[0][8])%((result[0][4]*E)**2 + ttab3**2*result[0][9]) == 0:
                        n_otimo2 = int((ttab3**2*result[0][8])//((result[0][4]*E)**2 + ttab3**2*result[0][9]))
                    else:
                        n_otimo2 = int((ttab3**2*result[0][8])//((result[0][4]*E)**2 + ttab3**2*result[0][9]) + 1)             
                ttab3 = tabela_t[t1][n_otimo2 - 2]
            if n_otimo2 - n_otimo1 < 3 and n_otimo2 != n_otimo1:
                for i in range(0, len(nparc)):
                    nparc_estrato = (tabela[i][3]*n_otimo2)
                    inteiro = nparc_estrato // 1
                    resto = nparc_estrato % 1
                    if resto == 0:
                        print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                    else:
                        print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
# Aqui começa o cálculo do método de Neyman               
    else:
# Aqui começa o cálculo do método de Neyman população infinita
        if f <= 0.05:
            if ns == 1:
                t1 = 0
            elif ns == 5:
                t1 = 2
            elif ns == 10:
                t1 = 3       
            ttab3 = tabela_t[t1][n - 2]
            if (ttab3**2*result[0][7]**2)%(result[0][4]*E)**2 == 0:
                n_otimo1 = int((ttab3**2*result[0][7]**7)//(result[0][4]*E)**2)
            else:
                n_otimo1 = int((ttab3**2*result[0][7]**2)//(result[0][4]*E)**2 + 1)        
            ttab3 = tabela_t[t1][n_otimo1 - 2]
            if (ttab3**2*result[0][7]**2)%(result[0][4]*E)**2 == 0:
                n_otimo2 = int((ttab3**2*result[0][7]**2)//(result[0][4]*E)**2)
            else:
                n_otimo2 = int((ttab3**2*result[0][7]**2)//(result[0][4]*E)**2 + 1)        
            ttab3 = tabela_t[t1][n_otimo2 - 2]
            for i in range(0, 20):
                if n_otimo1 == n_otimo2:
                    for i in range(0, len(nparc)):
                        nparc_estrato = (tabela[i][3]*n_otimo2)
                        inteiro = nparc_estrato // 1
                        resto = nparc_estrato % 1
                        if resto == 0:
                            print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                        else:
                            print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
                    break
                else:
                    n_otimo1 = n_otimo2
                    if (ttab3**2*result[0][7]**2)%(result[0][4]*E)**2 == 0:
                        n_otimo2 = int((ttab3**2*result[0][7]**2)//(result[0][4]*E)**2)
                    else:
                        n_otimo2 = int((ttab3**2*result[0][7]**2)//(result[0][4]*E)**2 + 1)             
                ttab3 = tabela_t[t1][n_otimo2 - 2]
            if n_otimo2 - n_otimo1 < 3 and n_otimo2 != n_otimo1:
                for i in range(0, len(nparc)):
                    nparc_estrato = (tabela[i][3]*n_otimo2)
                    inteiro = nparc_estrato // 1
                    resto = nparc_estrato % 1
                    if resto == 0:
                        print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                    else:
                        print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
# Aqui começa o cálculo do método de Neyman população finita      
        else:
            if ns == 1:
                t1 = 0
            elif ns == 5:
                t1 = 2
            elif ns == 10:
                t1 = 3       
            ttab3 = tabela_t[t1][n - 2]
            if (ttab3**2*result[0][7]**2)%((result[0][4]*E)**2 + ttab3**2*result[0][9]) == 0:
                n_otimo1 = int((ttab3**2*result[0][7]**2)//((result[0][4]*E)**2 + ttab3**2*result[0][9]))
            else:
                n_otimo1 = int((ttab3**2*result[0][7]**2)//((result[0][4]*E)**2 + ttab3**2*result[0][9]) + 1)        
            ttab3 = tabela_t[t1][n_otimo1 - 2]
            if (ttab3**2*result[0][7]**2)%((result[0][4]*E)**2 + ttab3**2*result[0][9]) == 0:
                n_otimo2 = int((ttab3**2*result[0][7]**2)//((result[0][4]*E)**2 + ttab3**2*result[0][9]))
            else:
                n_otimo2 = int((ttab3**2*result[0][7]**2)//((result[0][4]*E)**2 + ttab3**2*result[0][9]) + 1)        
            ttab3 = tabela_t[t1][n_otimo2 - 2]
            for i in range(0, 20):
                if n_otimo1 == n_otimo2:
                    for i in range(0, len(nparc)):
                        nparc_estrato = (tabela[i][3]*n_otimo2)
                        inteiro = nparc_estrato // 1
                        resto = nparc_estrato % 1
                        if resto == 0:
                            print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                        else:
                            print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
                    break
                else:
                    n_otimo1 = n_otimo2
                    if (ttab3**2*result[0][7]**2)%((result[0][4]*E)**2 + ttab3**2*result[0][9]) == 0:
                        n_otimo2 = int((ttab3**2*result[0][7]**2)//((result[0][4]*E)**2 + ttab3**2*result[0][9]))
                    else:
                        n_otimo2 = int((ttab3**2*result[0][7]**2)//((result[0][4]*E)**2 + ttab3**2*result[0][9]) + 1)             
                ttab3 = tabela_t[t1][n_otimo2 - 2]
            if n_otimo2 - n_otimo1 < 3 and n_otimo2 != n_otimo1:
                for i in range(0, len(nparc)):
                    nparc_estrato = (tabela[i][3]*n_otimo2)
                    inteiro = nparc_estrato // 1
                    resto = nparc_estrato % 1
                    if resto == 0:
                        print(f'O Estrato {i + 1} deve receber {inteiro} parcelas.')
                    else:
                        print(f'O Estrato {i + 1} deve receber {inteiro + 1} parcelas.')
                