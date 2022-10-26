from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='ottoeplitz',
      version='0.1',
      description='Toeplitz hashing algorithm for post-processing Random Number Generation',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
      ],
      url='https://github.com/BYUCamachoLab/ottoeplitz',
      author='Sarah Maia, Sarah Gonzalez',
      author_email='sarahcrismaia@gmail.com, sarahg.3545@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy', 'scipy',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)