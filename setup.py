#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    raise Exception("This package requires Python 2.7 or higher.")


def read_release_version():
    """Read the version from the file ``RELEASE-VERSION``."""
    with open("RELEASE-VERSION", "r") as f:
        return f.readline().strip()


def read_requirements_file(filename):
    """Read pip-formatted requirements from a file."""
    with open(filename, 'r') as f:
        return [
            line.strip() for line in f.readlines()
            if not line.startswith('#')
        ]


setup(
    name='@@project_name@@',
    description='An Automated Test Repository',
    packages=find_packages(
        exclude=['tests', 'tests.*'],
    ),
    test_suite='nose.collector',
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements_file('requirements.txt'),
    tests_require=read_requirements_file('requirements.txt'),
    long_description='''A python-selenium repo scaffold for new Selenium UI test projects''',
    dependency_links=['https://pypi.python.org/simple/'],
    version=read_release_version(),
    author='Chase Pilon',
    author_email='chasepilon@gmail.com',
    entry_points={
        'console_scripts': [
        ],
    }
)
