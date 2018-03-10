from setuptools import setup, find_packages


setup(name="robust_serial",
      packages=[package for package in find_packages()
                if package.startswith('robust_serial')],
      install_requires=[
          'pyserial',
          'enum34'
      ],
      tests_require=['pytest'],
      author="Antonin RAFFIN",
      author_email="antonin.raffin@ensta.org",
      url="https://github.com/araffin/",
      description="Simple and Robust Serial Communication Protocol",
      keywords="serial hardware arduino RS232 communication protocol raspberry",
      license="MIT",
      version="0.1",
      zip_safe=False)
