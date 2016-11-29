from setuptools import setup

setup(name='vaporimage',
      version='0.1',
      description='Procedurally generate aesthetic placeholder image in python.',
      url='https://github.com/danyalette/vaporimage',
      author='Danya Lette',
      author_email='danyalette@gmail.com',
      license='MIT',
      packages=['vaporimage'],
      install_requires=[
          'pillow',
          'django'
      ],
      zip_safe=False)