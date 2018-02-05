#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
  'matplotlib',
  'pandas',
  'twisted',
]

setup_requirements = [
]

test_requirements = [
]

setup(
    name='bands',
    version='0.1.0',
    description="Chromosome bands plotting",
    long_description=readme + '\n\n' + history,
    author="Francesco G. Brundu",
    url='https://github.com/fbrundu/bands',
    packages=find_packages(include=['bands']),
    include_package_data=True,
    package_data={
      'bands': ['ref/*.txt'],
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='bands',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
