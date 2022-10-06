import timeit

L =  3    # interval L
n =  1    # free index
m = -1    # free index

L_n = [i for i in range(n-L, n+L+1)]
L_m = [i for i in range(m-L, m+L+1)]

domain_r = L_n

start_time = timeit.default_timer()
result = 0
for r in domain_r:
	L_r = [i for i in range(r-L, r+L+1)]
	domain_p = list(set(L_r) & set(L_m))
	for p in domain_p:
		L_p = [i for i in range(p-L, p+L+1)]
		domain_q = list( set(L_n) & set(L_r) & set(L_p) )
		for q in domain_q:
			L_q = [i for i in range(q-L, q+L+1)]
			domain_o = list(set(L_n) & set(L_r) & set(L_q) & set(L_p))
			for o in domain_o:
				result += r*p*q*o
print(result)
print(timeit.default_timer() - start_time)


start_time = timeit.default_timer()
result2 = 0
for r in domain_r:
	L_r = [i for i in range(r-L, r+L+1)]
	domain_p = list(set(L_r) & set(L_m))
	domain_p.sort()
	for p in domain_p:
		L_p = [i for i in range(p-L, p+L+1)]
		domain_q = list( set(L_n) & set(L_r) & set(L_p) )
		domain_q.sort()
		for q in domain_q:
			L_q = [i for i in range(q-L, q+L+1)]
			domain_o = list(set(L_n) & set(L_r) & set(L_q) & set(L_p))
			domain_o.sort()
			for o in domain_o:
				result2 += r*p*q*o
print(result)
print(timeit.default_timer() - start_time)



start_time = timeit.default_timer()
result3 = 0
for r in domain_r:
	L_r = [i for i in range(r-L, r+L+1)]
	domain_p = list(set(L_r) & set(L_m))
	max_p    = max(domain_p)+1
	min_p    = min(domain_p)
	for p in range(min_p, max_p):
		L_p      = [i for i in range(p-L, p+L+1)] 
		domain_q = list(set(L_n) & set(L_r) & set(L_p))
		max_q    = max(domain_q)+1
		min_q    = min(domain_q)
		for q in range(min_q, max_q):
			L_q      = [i for i in range(q-L, q+L+1)]
			domain_o = list(set(L_n) & set(L_r) & set(L_q) & set(L_p))
			max_o    = max(domain_o)+1
			min_o    = min(domain_o)
			for o in range(min_o, max_o):
				result3 += r*p*q*o
print(result2) 	
print(timeit.default_timer() - start_time)

