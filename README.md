# Robust Arduino Serial Protocol in Python

[![Build Status](https://travis-ci.org/araffin/python-arduino-serial.svg?branch=master)](https://travis-ci.org/araffin/python-arduino-serial)

**Robust Arduino Serial** is a simple and robust serial communication protocol. It was designed to make two arduinos communicate, but can also be useful when you want a computer (e.g. a Raspberry Pi) to communicate with an Arduino.

## Installation

```
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

Serial communication with an Arduino: [Arduino Source Code](https://github.com/sergionr2/RacingRobot/tree/master/arduino)
```
python -m examples.arduino_serial
```
