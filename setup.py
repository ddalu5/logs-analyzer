from setuptools import setup, find_packages


setup(name='logs-analyzer',
      version='0.1',
      description='logs-analyzer helps you analyze logs.',
      long_description='logs-analyzer helps you analyze logs.',
      url='https://github.com/ddalu5/logs-analyzer',
      author='Salah OSFOR',
      author_email='icarus@daedalu5.org',
      license='Apache V2',
      packages=find_packages(exclude=['docs', 'tests']),
      test_suite='nose.collector',
      tests_require=['nose'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers :: Sysadmins :: DevOps',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 2',
      ],
      zip_safe=False)
