class HandlerEstatisticaEstratificada:
    def estat(self, variaveis, nparc, area_estrato, area_parcela, A, N):
        parcial = list()
        tabela = list()
        soma = soma2 = cont1 = 0
        li = 0
        for i in range(0, len(nparc)):
            ls = li + nparc[i]
            parcial.append(i + 1)  # 0
            nh = nparc[i]
            parcial.append(nh)  # 1
            Nh = round(area_estrato[i] / (area_parcela / 10000))
            parcial.append(Nh)  # 2
            wh = area_estrato[i] / A
            parcial.append(wh)  # 3
            for j in range(li, ls):
                soma = soma + variaveis[j]
                soma2 = soma2 + variaveis[j] ** 2
                cont1 = cont1 + 1
            li = ls
            med = soma / cont1
            parcial.append(med)  # 4
            var = (soma2 - soma ** 2 / cont1) / (cont1 - 1)
            desvpad = var ** (1 / 2)
            parcial.append(desvpad)  # 5
            parcial.append(var)  # 6
            whsh = wh * desvpad
            parcial.append(whsh)  # 7
            whs2h = wh * var
            parcial.append(whs2h)  # 8
            whs2hN = whs2h / N
            parcial.append(whs2hN)  # 9
            wh2s2nh = wh ** 2 * var / nh
            parcial.append(wh2s2nh)  # 10 Variância da média infinita
            wh2s2nhf = (wh ** 2 * var / nh) * (1 - nh / N)
            parcial.append(wh2s2nhf)  # 11 Variancia da média finita
            tabela.append(parcial[:])  # 12
            parcial.clear()
            soma = soma2 = cont1 = med = var = desvpad = 0
        return tabela
