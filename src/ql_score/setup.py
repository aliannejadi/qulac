from distutils.core import setup
from Cython.Build import cythonize

setup(name="ql", ext_modules=cythonize('ql_score.pyx', compiler_directives={'language_level': 3}),)
