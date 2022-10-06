class CallMe(object):
 def __call__(self, p, **k):
  print("CallMe instance called with:")
# print("Positional arguments", p)
  print("Keyword arguments", k)
 
c=CallMe()
c(1, 'rabbit',  hamster='elderberries' )
