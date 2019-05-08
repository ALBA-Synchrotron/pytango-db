#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages


TESTING = any(x in sys.argv for x in ["test", "pytest"])

requirements = ['PyTango',
                'futures ; python_version < "3"',
                'gevent']

setup_requirements = []
if TESTING:
    setup_requirements += ['pytest-runner']
test_requirements = ['pytest', 'pytest-cov']
extras_requirements = {'server': ['gevent']}

setup(
    author="Jairo Moldes, Tiago Coutinho",
    author_email='jmoldes@cells.es, tcoutinho@cells.es',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python Tango Database server",
    entry_points={
        'console_scripts': [
            'DataBaseds = tangodb:main',
        ]
    },
    install_requires=requirements,
    license="GPLv3",
    long_description="A device server written in python that mimics the official Tango DataBaseds",
    keywords='tango, pytango, database, device server',
    name='pytango-db',
    packages=find_packages(),
    package_data={'': ['*.sql']},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extras_requirements,
    url='http://github.com/ALBA-Synchrotron/pytango-db',
    version='0.2.0',
    zip_safe=True
)
