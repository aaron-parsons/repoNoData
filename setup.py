from setuptools import setup, find_packages
import os
import shutil

def readme():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'README.rst')) as f:
        return f.read()

import sys


if '--help' in sys.argv:
    print 'setting up a no data repo for test use'

def _get_packages():
    others = ['src', 'testr', 'utils']
    return find_packages() + others

setup(name='repoNoData',
      version='0.1',
      description='A no data repo for test use',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering'
        'Operating System :: POSIX :: Linux'
      ],
      author='Aaron Parsons',
      author_email='aaron.parsons@diamond.ac.uk',
      license='Apache License, Version 2.0',
      packages=_get_packages(),
      zip_safe=False)