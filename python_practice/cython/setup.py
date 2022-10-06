from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["CC_term_cython.pyx"])
)
