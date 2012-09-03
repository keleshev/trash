"""`trash` lives on `GitHub <http://github.com/halst/trash/>`_."""
from distutils.core import setup


setup(name='trash',
      version='0.1.0',
      description='Safe `rm` substitute for OS X',
      long_description=__doc__,
      license='MIT',
      author='Vladimir Keleshev',
      author_email='vladimir@keleshev.com',
      url='https://github.com/halst/trash/',
      classifiers=['Intended Audience :: Developers',
                   'Environment :: Console',
                   'Programming Language :: Python :: 2',
                   'Operating System :: MacOS',
                   'License :: OSI Approved :: MIT License'],
      keywords='rm, rmtrash, trash',
      py_modules=['trash'],
      scripts=['trash'])
