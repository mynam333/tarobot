from setuptools import setup, find_packages
 
 
 
setup(name='tarobot',
 
      version='0.0',
 
      url='https://github.com/mynam333/tarobot',
 
      license='Aru',
 
      author='YuAru',
 
      description='Manage configuration files',
 
      packages=find_packages(exclude=['tarobot']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=['nose>=0.0'],
 
      test_suite='nose.collector')
