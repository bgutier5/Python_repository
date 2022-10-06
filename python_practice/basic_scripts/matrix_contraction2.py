f = 5*[5*[5*[5*[3]]]]
t = 5*[5*[5*[5*[2]]]]

def contract(f, t, a, n, i, m):
	upper_lim1 = len(f)
	upper_lim2 = len(f[0]) 
	ft_an_im = 0
	for c in range(upper_lim1):
		for o in range(upper_lim2):
			ft_an_im += f[a][n][c][o]*t[c][o][i][m]
	return ft_an_im

print(contract(f, t, 1, 1, 1, 1))
