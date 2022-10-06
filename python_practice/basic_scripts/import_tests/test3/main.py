#mylib = __import__('2package')
import importlib
mylib = importlib.import_module('2package', package=None)
newlib = importlib.import_module('./subfolder1/2subfolder/inner_function', package=True)

#mylib.print_myname('Hello world!')
newlib.deep_function('Boris')

