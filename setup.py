from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='abrilskopsorting',
  version='0.0.1',
  description='Metodos de Ordenamiento complejos',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abrilskop',
  author_email='uberpot.ia@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='sorting_algorithm', 
  packages=find_packages(),
  install_requires=[''] 
)
