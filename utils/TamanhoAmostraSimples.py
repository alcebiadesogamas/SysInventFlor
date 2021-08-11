def int_amostral(ns, n, N, f, media, var, E):
    nfinal = 0
    import valor_t
    n1 = n
    if f <= 0.05:
        ttab = valor_t.t_tabelado(ns, n1)
        if (ttab[0] ** 2 * var) % (media * E) ** 2 == 0:
            n_otimo1 = int((ttab[0] ** 2 * var) // (media * E) ** 2)
        else:
            n_otimo1 = int((ttab[0] ** 2 * var) // (media * E) ** 2 + 1)
        n1 = n_otimo1
        ttab = valor_t.t_tabelado(ns, n1)
        if (ttab[0] ** 2 * var) % (media * E) ** 2 == 0:
            n_otimo2 = int((ttab[0] ** 2 * var) // (media * E) ** 2)
        else:
            n_otimo2 = int((ttab[0] ** 2 * var) // (media * E) ** 2 + 1)
        n1 = n_otimo2
        ttab = valor_t.t_tabelado(ns, n1)
        for i in range(0, 20):
            if n_otimo1 == n_otimo2:
                nfinal = n_otimo2
                return nfinal
            else:
                n_otimo1 = n_otimo2
                if (ttab[0] ** 2 * var) % (media * E) ** 2 == 0:
                    n_otimo2 = int((ttab[0] ** 2 * var) // (media * E) ** 2)
                else:
                    n_otimo2 = int((ttab[0] ** 2 * var) // (media * E) ** 2 + 1)
            n1 = n_otimo2
            ttab = valor_t.t_tabelado(ns, n1)
        if n_otimo2 - n_otimo1 < 3 and n_otimo2 != n_otimo1:
            nfinal = n_otimo2
            return nfinal
    else:
        ttab = valor_t.t_tabelado(ns, n1)
        if N * (ttab[0] ** 2 * var) % (N * (media * E) ** 2 + (ttab[0] ** 2 * var)) == 0:
            n_otimo1 = int(N * (ttab[0] ** 2 * var) // (N * (media * E) ** 2 + (ttab[0] ** 2 * var)))
        else:
            n_otimo1 = int(N * (ttab[0] ** 2 * var) // (N * (media * E) ** 2 + (ttab[0] ** 2 * var))) + 1
        n1 = n_otimo1
        ttab = valor_t.t_tabelado(ns, n1)
        if N * (ttab[0] ** 2 * var) % (N * (media * E) ** 2 + (ttab[0] ** 2 * var)) == 0:
            n_otimo2 = int(N * (ttab[0] ** 2 * var) // (N * (media * E) ** 2 + (ttab[0] ** 2 * var)))
        else:
            n_otimo2 = int(N * (ttab[0] ** 2 * var) // (N * (media * E) ** 2 + (ttab[0] ** 2 * var))) + 1
        n1 = n_otimo2
        ttab = valor_t.t_tabelado(ns, n1)
        for i in range(0, 20):
            if n_otimo1 == n_otimo2:
                nfinal = n_otimo2
                return nfinal
            else:
                n_otimo1 = n_otimo2
                if N * (ttab[0] ** 2 * var) % (N * (media * E) ** 2 + (ttab[0] ** 2 * var)) == 0:
                    n_otimo2 = int(N * (ttab[0] ** 2 * var) // (N * (media * E) ** 2 + (ttab[0] ** 2 * var)))
                else:
                    n_otimo2 = int(N * (ttab[0] ** 2 * var) // (N * (media * E) ** 2 + (ttab[0] ** 2 * var))) + 1
            n1 = n_otimo2
            ttab = valor_t.t_tabelado(ns, n1)
        if n_otimo2 - n_otimo1 < 3 and n_otimo2 != n_otimo1:
            return n_otimo2
        return ttab, n_otimo1, n_otimo2
