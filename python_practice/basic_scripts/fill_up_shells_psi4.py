
def get_indices(counter, shape):
    beg = prev_counter 
    end = prev_counter + shape
    return beg, end



n_shells = 5
V_shape = [1,1,3,1,3]
tensor = [i for i in range(9)]
prev_counter = 0
for p in range(n_shells):
    shape = V_shape[p]
    beg, end = get_indices(prev_counter, shape)
    prev_counter = end
    print(tensor[beg:end])
