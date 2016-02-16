#!/usr/bin/env python

from distutils.core import setup
import nagioscheck

setup(
    name = 'nagioscheck',
    version = nagioscheck.__version__,
    author = 'Saj Goonatilleke',
    author_email = 'sg@redu.cx',

    description = 'A Python framework for Nagios plug-in developers',
    long_description = """
pynagioscheck is a Python framework for Nagios plug-in developers.

pynagioscheck strives to conform to the practices described in the
Nagios Plug-in Development Guidelines and, more importantly, save
valuable system administrator time.
    """,
    license = 'BSD',
    platforms = [ 'Linux', 'Unix' ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
    ],

    py_modules = ['nagioscheck'],
)

