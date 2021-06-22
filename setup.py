from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyautoclicker',
  version='1.0.5',
  description="The best autoclicker in python!" ,
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  long_description_content_type="text/markdown",
  url='https://github.com/DevER-M/pyautoclicker',  
  author='Dever',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='autoclicker', 
  packages=find_packages(),
  install_requires=['pynput','random-dice-roller','rand-password-generator','coord-generator',]
) 