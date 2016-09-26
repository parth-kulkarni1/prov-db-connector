#!/usr/bin/env python
from setuptools import setup

setup(
    name='prov-db-connector',
    version='0.1',
    description='PROV Database Connector',
    keywords=[
        'provenance', 'graph', 'model', 'PROV', 'PROV-DM', 'PROV-JSON', 'JSON',
        'PROV-XML', 'PROV-N'
    ],
    author='DLR, Stefan Bieliauskas, Martin Stoffers',
    author_email='opensource@dlr.de, sb@conts.de, martin.stoffers@studserv.uni-leipzig.de',
    url='https://github.com/DLR-SC/prov-db-connector',
    packages=[
        'provdbconnector',
    ],
    install_requires=[
        "prov==1.4.0",
        "neo4j-driver==1.0.2",
        "networkx==1.11",
        "decorator==4.0.10",
        "lxml==3.6.4",
        "six==1.10.0"
    ],
    license="MIT",
    test_suite='tests',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python 3.4',
    ]
)