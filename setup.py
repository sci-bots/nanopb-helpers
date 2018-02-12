#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup
import sys

sys.path.insert(0, '.')
import version

setup(name='nanopb_helpers',
      version=version.getVersion(),
      description='Cross-platform Python API for `nanopb`',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='http://github.com/wheeler-microfluidics/nanopb_helpers.git',
      license='GPLv2',
      install_requires=['path_helpers'],
      packages=['nanopb_helpers'],
      include_package_data=True)
