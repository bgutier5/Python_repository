class matvec:
 def __init__(M):
  self.M = M

 def __call__(self):
  return(numpy.dot(M,v))

