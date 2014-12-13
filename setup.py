#/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import os.path


def _get_version(here):
    with open(os.path.join(here, "foundation", "__init__.py")) as f:
        for line in f.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)
VERSION = _get_version(ROOT_DIR)

setup(
    name="django-zurb-foundation",
    version=VERSION,
    description="Django Zurb Foundation package.",
    author="Amar Šahinović",
    author_email="amar@sahinovic.com",
    url="https://github.com/amarsahinovic/django-zurb-foundation",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Utilities'],
    install_requires=[],
)
