"""Here's our handy setup script for the ipviking django authentication"""

from setuptools import setup, find_packages

setup(
      name = 'ipviking_pyramid',
      version = '0.1',
      description = 'An example of using the IPViking API as authentication in a Pyramid app.',
      author = 'Marcus Hoffman',
      url = 'https://github.com/norsecorp/ipviking-pyramid',
      license = 'BSD',
      packages = find_packages(),
      include_package_data = True,
      package_data = {'':['README.md']},
      install_requires = ['ipviking_api_python', 'pyramid'],
      tests_require = [],
      classifiers = ['Development Status :: 1 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD Licence',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Internet',
                     'Topic :: Network Security',
                     'Topic :: Software Development :: Libraries :: Python Modules'])
