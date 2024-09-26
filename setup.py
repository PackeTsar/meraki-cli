#!/usr/bin/env python


"""
PIP installation configuration file
"""


import os
import sys
from setuptools import setup
from setuptools import find_packages

# Find local file path
localdir = os.path.split(os.path.abspath(__file__))[0]


# Using a function to make the damn linter happy
def version():
    project_dir = os.path.join(localdir, "meraki_cli")
    sys.path = [project_dir] + sys.path
    import __version__
    return __version__.version


with open(os.path.join(
        localdir, "README.md"), "r", encoding='utf-8') as readme:
    long_description = readme.read()
    readme.close()


with open(os.path.join(
        localdir, "requirements.txt"), "r", encoding='utf-8') as req_file:
    install_requires = []
    for package in req_file.read().split("\n"):
        if package:
            install_requires.append(package)
    req_file.close()


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: Microsoft',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System',
    'Topic :: System :: Networking']


setup(name='meraki_cli',
      version=version(),
      description='A Simple CLI tool to automate and control your '
      'Meraki Dashboard',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='John W Kerns',
      classifiers=CLASSIFIERS,
      author_email='jkerns@packetsar.com',
      url='https://github.com/PackeTsar/meraki-cli',
      license="GNU",
      packages=find_packages(),
      install_requires=install_requires,
      extras_require={'dev': ['jinja2', 'pytest', 'coverage', 'flake8',
                              'requests-mock', 'tox', 'mkdocs',
                              'mkdocs-material']},
      entry_points={
          'console_scripts': [
              'meraki = meraki_cli.__main__:main'
          ]
      }
      )
