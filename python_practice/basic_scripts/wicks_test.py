from sympy import symbols, Dummy, latex
from sympy.physics.secondquant import Commutator, Fd, F, contraction, wicks,NO, evaluate_deltas, substitute_dummies


a, b, c, d, e = symbols('a,b,c,d,e', above_fermi=True)
i, j, k, l, m = symbols('i,j,k,l,m', below_fermi=True)
p, q, r, s    = symbols('p,q,r,s', cls=Dummy)
comm = Commutator


V   = NO( Fd(p)*Fd(q)*F(s)*F(r) )
T_1 = NO( Fd(b)*F(j) )

comm1 = wicks( comm(V, T_1) )


result = wicks(  NO(  Fd(i)*F(a) )*comm1, simplify_kronecker_deltas=True, keep_only_fully_contracted=True ) 
print( latex(result) )
