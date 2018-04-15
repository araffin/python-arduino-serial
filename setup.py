from setuptools import setup, find_packages

# Create Package
# rm dist/*
# python setup.py sdist
# python setup.py bdist_wheel
# Upload
# (test) twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# (release) twine upload dist/*

long_description = """
Robust Arduino Serial is a simple and robust serial communication protocol.
It was designed to make two arduinos communicate, but can also be useful when you want a computer (e.g. a Raspberry Pi) to communicate with an Arduino.
https://medium.com/@araffin/simple-and-robust-computer-arduino-serial-communication-f91b95596788
"""

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
      url="https://github.com/araffin/arduino-robust-serial",
      description="Simple and Robust Serial Communication Protocol",
      long_description=long_description,
      keywords="serial hardware arduino RS232 communication protocol raspberry",
      license="MIT",
      version="0.1",
      zip_safe=False)
