# Robust Arduino Serial Protocol in Python

![CI](https://github.com/araffin/python-arduino-serial/workflows/CI/badge.svg) [![Documentation Status](https://readthedocs.org/projects/python-arduino-serial/badge/?version=latest)](https://python-arduino-serial.readthedocs.io/en/latest/?badge=latest)

**Robust Arduino Serial** is a simple and robust serial communication protocol. It was designed to make two arduinos communicate, but can also be useful when you want a computer (e.g. a Raspberry Pi) to communicate with an Arduino.

It supports Python 3.8+.

This repository is part of the Robust Arduino Serial project, main repository: [https://github.com/araffin/arduino-robust-serial](https://github.com/araffin/arduino-robust-serial)

**Please read the [Medium Article](https://medium.com/@araffin/simple-and-robust-computer-arduino-serial-communication-f91b95596788) to have an overview of this protocol.**

Documentation: [https://python-arduino-serial.readthedocs.io](https://python-arduino-serial.readthedocs.io)

Implementations are available in various programming languages:

- [Arduino](https://github.com/araffin/arduino-robust-serial)
- [Python](https://github.com/araffin/python-arduino-serial)
- [C++](https://github.com/araffin/cpp-arduino-serial)
- [Rust](https://github.com/araffin/rust-arduino-serial)

## Installation

Using pip:
```
pip install robust_serial
```

From Source:
```
git clone https://github.com/araffin/python-arduino-serial.git
pip install -e .
```

## Tests
Run the tests (require pytest):
```
make pytest
```

## Examples

Read write in a file (WARNING: the file will be deleted when the script exits)
```
python -m examples.file_read_write -f test.txt
```

Serial communication with an Arduino: [Arduino Source Code](https://github.com/araffin/arduino-robust-serial/tree/master/arduino-board/)
```
python -m examples.arduino_serial
```

### Example: Communication with Sockets

It can be useful when you want two programs to communicate over a network (e.g. using wifi) or even locally on the same computer (e.g. when you want a python2 script that communicates with a python3 script).

1. Start the server:
```
python -m examples.socket_example --server
```

2. Run the client:
```
python -m examples.socket_example --client
```

### Bluetooth Example with Two Computers

Dependencies:
```
sudo apt-get install libbluetooth-dev bluez
pip install pybluez
```

You need to change the server mac address `SERVER_ADDR`, you can use `hciconfig` to know the mac address of your computer.

Server:
```
python -m examples.bluetooth_example --server
```

Client:
```
python -m examples.bluetooth_example --client
```
