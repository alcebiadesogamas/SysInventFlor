def soma_quadrados(x):
    return(x**2)

def estatistica(lista1, variavel, nsim, ttab):
    soma = sq = med = 0
    transicao = []
    resultados = []
    for i in range(0, nsim):
        soma = sum(lista1[i])
        med = soma / len(lista1[i])
        sq = sum(list(map(soma_quadrados, lista1[i])))
        var = (sq - soma ** 2 / len(lista1[i])) / (len(lista1[i]) - 1)
        varmed = var / len(lista1[i])
        epmed = varmed ** (1 / 2)
        eaa = epmed * ttab
        ear = (eaa/med)*100
        li = (med - eaa)
        ls = (med + eaa)
        li1 = (med - epmed)
        ls1 = (med + epmed)
        ev = abs(sum(variavel) / len(variavel) - med)
        transicao.append(med)
        transicao.append(var)
        transicao.append(varmed)
        transicao.append(epmed)
        transicao.append(eaa)
        transicao.append(li)
        transicao.append(ls)
        transicao.append(ev)
        transicao.append(ear)
        transicao.append(li1)
        transicao.append(ls1)
        resultados.append(transicao[:])
        soma = med = sq = var = varmed = epmed = eaa = li = ls = li1 = ls1 = 0
        transicao.clear()
    return(resultados)
