# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='fileioapi',
  version='0.0.2',

  description='API wrapper for file.io',
  long_description=long_description,
  long_description_content_type="text/markdown",

  url='https://github.com/gr3atwh173/fileioapi',

  author='Great White',

  license='MIT',

  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],

  python_requires='>=3.5',

  keywords='fileio api',

  packages=find_packages(exclude=['contrib', 'docs', 'tests']),

  install_requires=['requests'],

  project_urls={  
    'Bug Reports': 'https://github.com/Gr3atWh173/fileioapi/issues',
    'Source': 'https://github.com/Gr3atWh173/fileioapi',
  },
)