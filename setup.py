#!/usr/bin/env python3

from setuptools import setup

with open('README.rst', 'r') as fh:
    _long_description = fh.read()

with open('VERSION.txt', 'r') as fh:
    _version = fh.read()

_description = 'Program for consistent encoding/decoding of base64 strings'

setup(name="b64",
      version=_version,
      url='https://gitlab.icg360.net/chris-gatewood/b64',
      maintainer='Chris Gatewood',
      maintainer_email='chris.gatewood@icg360.com',
      packages=['b64'],
      scripts=['scripts/b64'],
      license='GPLv3',
      long_description=_long_description,
      description=_description,
      install_requires=[],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPLv3 License",
            "Operating System :: OS Independent"
      ],
      )

