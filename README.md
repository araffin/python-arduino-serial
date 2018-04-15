# Robust Arduino Serial Protocol in Python

[![Build Status](https://travis-ci.org/araffin/python-arduino-serial.svg?branch=master)](https://travis-ci.org/araffin/python-arduino-serial)

**Robust Arduino Serial** is a simple and robust serial communication protocol. It was designed to make two arduinos communicate, but can also be useful when you want a computer (e.g. a Raspberry Pi) to communicate with an Arduino.

It supports both Python 2 and 3.

This repository is part of the Robust Arduino Serial project, main repository: [https://github.com/araffin/arduino-robust-serial](https://github.com/araffin/arduino-robust-serial)

**Please read the [Medium Article](https://medium.com/@araffin/simple-and-robust-computer-arduino-serial-communication-f91b95596788) to have an overview of this protocol.**

Implementations are available in various programming languages:

- [Arduino](https://github.com/araffin/arduino-robust-serial)
- [Python](https://github.com/araffin/python-arduino-serial)
- [C++](https://github.com/araffin/cpp-arduino-serial)
- [Rust](https://github.com/araffin/rust-arduino-serial)

## Installation

```
git clone https://github.com/araffin/python-arduino-serial.git
pip install -e .
```

## Tests
Run the tests (require pytest):
```
pytest
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

### Bluetooth Example

Dependency:
```
sudo apt-get install libbluetooth-dev bluez
pip install pybluez
```

Server:
```
python -m examples.bluetooth_example --server
```

Client:
```
python -m examples.bluetooth_example --client
```
