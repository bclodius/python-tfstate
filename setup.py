# -*- coding: utf-8 -*-

from src import tfstate
from setuptools import setup, find_packages

# Package dependencies
install_requires = [

]

# Trove classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules'
]


setup(
    # Package info
    name=tfstate.name,
    version=tfstate.version,
    description=tfstate.description,
    author=tfstate.author,
    author_email=tfstate.author_email,
    url='',
    long_description=tfstate.description,

    # Package classifiers
    classifiers=classifiers,

    # Package structure
    packages=find_packages('src', exclude=['ez_setup', '*.tests', '*.tests.*', 'tests.*', 'tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

    # Dependencies
    install_requires=install_requires,

)
