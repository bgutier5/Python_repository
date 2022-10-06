
import matplotlib

# Force matplotlib to not use any Xwindows backend.

# matplotlib.use('Agg')  # this was first one that worked
# matplotlib.use('GTK')
# matplotlib.use('GTKAgg')
# matplotlib.use('Qt4Agg')

import matplotlib.pyplot as plt
plt.plot([1,2,5,6],[2,4,8,2] , label='my line', linestyle='--', marker='o', color='r' )
plt.plot([2,3,6,7],[3,5,9,3] , label='my line 2')
plt.ylabel('some numbers')
plt.legend(bbox_to_anchor=(1, 1), loc=4, borderaxespad=0.)
plt.show()
