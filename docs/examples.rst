.. _examples:

Examples
========

Examples provided here are also in the ``examples/`` folder of the repo.

Arduino Serial Communication
----------------------------

Serial communication with an Arduino: `Arduino Source Code`_

.. _Arduino Source Code: https://github.com/araffin/arduino-robust-serial/tree/master/arduino-board/


.. code-block:: python

  from __future__ import print_function, division, absolute_import

  import time

  from robust_serial import write_order, Order, write_i8, write_i16, read_i8, read_order
  from robust_serial.utils import open_serial_port


  try:
      serial_file = open_serial_port(baudrate=115200, timeout=None)
  except Exception as e:
      raise e

  is_connected = False
  # Initialize communication with Arduino
  while not is_connected:
      print("Waiting for arduino...")
      write_order(serial_file, Order.HELLO)
      bytes_array = bytearray(serial_file.read(1))
      if not bytes_array:
          time.sleep(2)
          continue
      byte = bytes_array[0]
      if byte in [Order.HELLO.value, Order.ALREADY_CONNECTED.value]:
          is_connected = True

  print("Connected to Arduino")

  motor_speed = -56

  # Equivalent to write_i8(serial_file, Order.MOTOR.value)
  write_order(serial_file, Order.MOTOR)
  write_i8(serial_file, motor_speed)

  write_order(serial_file, Order.SERVO)
  write_i16(serial_file, 120)

  for _ in range(10):
      order = read_order(serial_file)
      print("Ordered received: {:?}", order)



Reading / Writing in a file
---------------------------

Read write in a file (WARNING: the file will be deleted when the script exits)


.. code-block:: python

  from __future__ import print_function, division, absolute_import
  import os

  from robust_serial import Order, write_order, write_i8, write_i16, write_i32, read_i8, read_i16, read_i32, read_order

  test_file = "test.txt"

  with open(test_file, 'wb') as f:
      write_order(f, Order.HELLO)

      write_i8(f, Order.MOTOR.value)
      write_i16(f, -56)
      write_i32(f, 131072)

  with open(test_file, 'rb') as f:
      # Equivalent to Order(read_i8(f))
      order = read_order(f)
      print(order)

      motor_order = read_order(f)
      print(motor_order)
      print(read_i16(f))
      print(read_i32(f))

  # Delete file
  os.remove(test_file)
