import os
import re
import sys
from setuptools import setup, find_packages


install_requires = ['psycopg2>=2.5.2']

PY_VER = sys.version_info

if PY_VER >= (3, 4):
    pass
elif PY_VER >= (3, 3):
    install_requires.append('asyncio')
else:
    raise RuntimeError("aiozmq doesn't suppport Python earllier than 3.3")

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), 'aiopg', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in aiopg/__init__.py')

classifiers=[
    'License :: OSI Approved :: BSD License',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Operating System :: POSIX',
    'Environment :: Web Environment',
]

if 'a' in read_version():
    classifiers.append('Development Status :: 3 - Alpha')
elif 'b' in read_version():
    classifiers.append('Development Status :: 4 - Beta')
else:
    classifiers.append('Development Status :: 5 - Production/Stable')

setup(name='aiopg',
      version=read_version(),
      description=('Postgress integration with asyncio.'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=classifiers,
      platforms=['POSIX'],
      author='Andrew Svetlov',
      author_email='andrew.svetlov@gmail.com',
      url='http://aiozmq.readthedocs.org',
      download_url='https://pypi.python.org/pypi/aiozmq',
      license='BSD',
      packages=find_packages(),
      install_requires = install_requires,
      provides = ['aiopg'],
      requires = ['psycopg2'],
      include_package_data = True)