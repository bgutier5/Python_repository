f = 5*[5*[3]]
t = 5*[5*[2]]

def contract(f, t, i, j):
	upper_lim = len(f)
	ft_ij = 0
	for k in range(upper_lim):
		ft_ij += f[i][k]*t[k][j]
	return ft_ij

print(contract(f, t, 1, 1))
