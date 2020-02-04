#!/usr/bin/env python

import os
from setuptools import setup


path_req = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')
install_req = [e.strip() for e in open(path_req).readlines()]


setup(name='pysentiment',
      version='0.2',
      description='Python sentiment analysis utilities',
      author='Zhichao HAN',
      author_email='hanzhichao@gmail.com',
      packages=['pysentiment'],
      package_dir={'pysentiment': 'pysentiment'},
      install_requires=install_req,
      data_files=[('pysentiment/static',
                   ['pysentiment/static/%s' % e for e in [
                        'HIV-4.csv', 'LM.csv',
                        'Currencies.txt', 'DatesandNumbers.txt',
                        'Generic.txt', 'Geographic.txt', 'Names.txt']])],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis"])
