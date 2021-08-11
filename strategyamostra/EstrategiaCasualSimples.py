from strategyestatistica.StrategySimple import estatistica
from model.Tabela import Tabela
import pandas as pd
import matplotlib.pyplot as plt
import random


class SimulaCasualSimples:
    def tab_freq(self, result, nsim, medverd, amp):
        t_media = []
        for i in range(0, len(result)):
            t_media.append(result[i][0])
        vmin = int(min(t_media))
        vmax = int(max(t_media))
        a = amp
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
                if lic <= result[j][0] < lsc:
                    f.append(result[j][0])
            nfreq.append(f[:])
            freq.append(len(nfreq[i]))
            f.clear()
            lic = lic + a
            lsc = lsc + a
        if not freq[len(nfreq) - 1]:
            nfreq.pop()
            cclas.pop()
        cont1 = cont2 = 0
        # Calculando a frequência de acertos para o intervalo de confiança com o valor de t
        for i in range(0, nsim):
            if result[i][5] <= medverd <= result[i][6]:
                cont1 = cont1 + 1
            else:
                cont2 = cont2 + 1

        return vmin, a, cclas, freq, cont1, cont2

    def simular(self, n, nsim, nst, caminho, amp):
        dados = pd.read_excel(caminho)
        variavel = dados['VAR'].values.tolist()
        amostrasColetadas = []

        while len(amostrasColetadas) != nsim:
            parcelas = random.sample(variavel, n)
            if parcelas not in amostrasColetadas:
                amostrasColetadas.append(parcelas)

        tb = Tabela(diretorio='./resources/tabelat.xlsx')
        tb.setValoresTtabelado(nst, n)
        valor_t = tb.valoresTtabelado

        result = estatistica(amostrasColetadas, variavel, nsim, valor_t[0])

        medverd = sum(variavel) / len(variavel)
        tab = self.tab_freq(result, nsim, medverd, amp)

        plt.bar(tab[2], tab[3], tick_label=tab[2])
        plt.ylabel('frequências')
        plt.xlabel('classes')
        saida = f'Intevalos de confiança bem definidos (com o valor de t): {tab[4]}\n'
        saida += f'Intevalos de confiança mal definidos (com o valor de t): {tab[5]}'
        plt.suptitle(saida)
        plt.show()


if __name__ == '__main__':
    pass
