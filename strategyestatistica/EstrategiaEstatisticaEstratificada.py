import numpy as np
from model.Estatistica import Estatistica
from model.Tabela import Tabela
from model.Populacao import Populacao
class HandlerEstatisticaEstratificada:
    def estat(self, variaveis, nparc, area_estrato, area_parcela, A, N):
        parcial = list()
        tabela = list()
        soma = soma2 = cont1 = 0
        li = 0
        for i in range(0, len(nparc)):
            ls = li + nparc[i]
            parcial.append(i + 1)
            nh = nparc[i]
            parcial.append(nh)
            Nh = round(area_estrato[i]/(area_parcela/10000))
            parcial.append(Nh)
            wh = area_estrato[i]/A
            parcial.append(wh)
            for j in range(li, ls):
                soma = soma + variaveis[j]
                soma2 = soma2 + variaveis[j]**2
                cont1 = cont1 + 1
            li = ls
            med = soma/cont1
            parcial.append(med)
            var = (soma2 - soma**2/cont1)/(cont1 - 1)
            desvpad = var**(1/2)
            parcial.append(desvpad)
            parcial.append(var)
            whsh = wh*desvpad
            parcial.append(whsh)
            whs2h = wh*var
            parcial.append(whs2h)
            whs2hN = whs2h/N
            parcial.append(whs2hN)
            wh2s2nh = wh**2*var/nh
            parcial.append(wh2s2nh)
            wh2s2nhf = wh ** 2 * var / nh*(1 - nh/N)
            parcial.append(wh2s2nhf)
            tabela.append(parcial[:])
            parcial.clear()
            soma = soma2 = cont1 = med = var = desvpad = 0 
        return tabela