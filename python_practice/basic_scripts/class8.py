class Pizza(object):
     def __init__(self, size):
         self.size = size

     def get_size(self):
         return self.size

#Pizza.get_size()
size = Pizza(42).get_size()
print(size)
