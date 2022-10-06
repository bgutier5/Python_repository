from primes import primes
from containers_classes import one_body_hamiltonian_class, two_body_hamiltonian_class
from containers_classes import single_amplitudes_class, double_amplitudes_class
import CC_term 
import CC_term_cython
import timeit

L = 0
n_virtuals = 2
n_occupied = 2

f_pq = one_body_hamiltonian_class(n_virtuals, n_occupied, L)
v_pqrs = two_body_hamiltonian_class(n_virtuals, n_occupied, L)
t_ai = single_amplitudes_class(n_virtuals, n_occupied, L)
t_abij = double_amplitudes_class(n_virtuals, n_occupied, L)

#print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
# python
start_time = timeit.default_timer()
print( CC_term.delta_E(L, n_virtuals, n_occupied, f_pq, v_pqrs, t_ai, t_abij) )
elapsed = timeit.default_timer() - start_time

# cython
start_time = timeit.default_timer()
print( CC_term_cython.delta_E(L, n_virtuals, n_occupied, f_pq, v_pqrs, t_ai, t_abij) )
elapsed2 = timeit.default_timer() - start_time
print('elapsed time (python)=', elapsed, "sec")
print('elapsed time (cython)=', elapsed2, "sec")
#print(primes(20))
