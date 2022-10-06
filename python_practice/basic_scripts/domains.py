L = 2
n = 1
m = -1

domain_r = [r for r in range(n-L, n+L)]
domain_p = list( set([p for r in range(n-L, n+L) for p in range(r-L, r+L)]) & set([p for p in range(m-L, m+L)]) )
domain_p.sort()

for r in domain_r:
	for p in domain_p:
		print('r=', r, 'p=', p)  
