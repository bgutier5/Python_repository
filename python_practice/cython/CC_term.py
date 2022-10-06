def delta_E(L, n_virtuals, n_occupied, f_pq, v_pqrs, t_ai, t_abij):
    result = 0

    m=0


    L_0 = [i for i in range(-L, L+1)]
    domain_o = L_0

    for o in domain_o:
        for a in range(n_virtuals):
            L_o = [i for i in range(o-L, o+L+1)]
            domain_p = list( set(L_o) )
            for p in domain_p:
                for i in range(n_occupied):
                    result += 1*f_pq(i, p, a + n_occupied, o)*t_ai(a, o ,i ,p)
    return(result)

