#!/usr/bin/env python

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

# http://pytest.org/latest/goodpractises.html#integration-with-setuptools-distribute-test-commands
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, because outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

# taken from the exemplar setup.py script at
# https://github.com/mgedmin/restview/blob/master/setup.py
def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()

setup(
    name="immutable",
    version="0.1",
    author="James R. Garrison",
    author_email="jim@garrison.cc",
    url='https://github.com/garrison/python-immutable',
    download_url='https://pypi.python.org/pypi/immutable',
    description='Class decorator for immutable objects in python',
    long_description=read('README.rst'),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['immutable'],
    tests_require=['pytest', 'six'],
    cmdclass={'test': PyTest},
    use_2to3=True,
)
