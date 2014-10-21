#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="paultag",
      version='0.0.1',
      author="Paul Tagliamonte",
      author_email='tag@pault.ag',
      license="BSD-3",
      description="paultag API",
      long_description="",
      url="",
      packages=[
          'paultag',
          'paultag.travel',
      ],
      include_package_data=True,
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   ],
      )
