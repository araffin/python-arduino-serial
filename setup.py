from setuptools import find_packages, setup

long_description = """
Robust Arduino Serial is a simple and robust serial communication protocol.
It was designed to make two arduinos communicate,
but can also be useful when you want a computer (e.g. a Raspberry Pi) to communicate with an Arduino.
https://medium.com/@araffin/simple-and-robust-computer-arduino-serial-communication-f91b95596788
"""

setup(
    name="robust_serial",
    packages=[package for package in find_packages() if package.startswith("robust_serial")],
    install_requires=[
        "pyserial",
    ],
    tests_require=["pytest", "pytest-cov", "mypy", "ruff", "black", "isort"],
    author="Antonin RAFFIN",
    author_email="antonin.raffin@ensta.org",
    url="https://github.com/araffin/arduino-robust-serial",
    description="Simple and Robust Serial Communication Protocol",
    long_description=long_description,
    keywords="serial hardware arduino RS232 communication protocol raspberry",
    license="MIT",
    version="0.2",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
