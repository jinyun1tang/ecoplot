#from distutils.core import setup
#from distutils.extension import Extension
from setuptools import setup, Extension

import numpy

import io



install_requires = [
    'numpy',
    'scipy'
]

#extras_require = {
#    'Gaussian Process (GP) Regression':  ['sklearn>=0.18'],
#    'R-based ACE, also requires acepack installed in R':  ['rpy2'],
#    'pure-python ACE':  ['ace>=0.3'],
#    'plotting': ['matplotlib>=1.5', 'networkx>=1.10'],
#    'p-value corrections': ['statsmodels']
#}

tests_require = ['nose']


cmdclass = { }
ext_modules = [ ]



setup(
    name='ecoplot',
    version='1.0b0',
    packages=['ecoplot',],
    license='GNU General Public License v3.0',
    description='Plot script of ecosys',
    author='Jinyun Tang',
    author_email='jinyuntang@gmail.com',
    url='https://github.com/jinyun1tang/ecoplot',
    long_description=io.open('README.md', 'r', encoding='utf-8').read(),
    keywords = 'ECOSYS model',
    cmdclass = cmdclass,
    ext_modules=ext_modules,
    install_requires=install_requires,
    test_suite = 'nose.collector',
    tests_require = tests_require,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Ecosystem modeling',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
    ],
)
