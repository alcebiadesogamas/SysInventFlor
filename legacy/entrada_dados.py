def ent_dados(lista1):
    nparc = list()
    a = lista1[0]
    cont = 0
    for i in range(0, len(lista1)):
        if lista1[i] == a:
            cont = cont + 1
        else:
            nparc.append(cont)
            a = lista1[i]
            cont = 1
    nparc.append(cont)
    return nparc


    
    