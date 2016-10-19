from setuptools import setup

setup(name='python-lametric-api',
      version='0.0.1',
      description='Python API for sending notifications to LaMetric',
      url='https://github.com/heytcass/python-lametric-api',
      author='Tom Cassady',
      license='MIT',
      install_requires=['requests>=2.0'],
      packages=['pylametric'],
      zip_safe=True)
