from __future__ import print_function, division, absolute_import
import argparse
import os

from robust_serial import Order, write_order, write_i8, write_i16, write_i32, read_i8, read_i16, read_i32, read_order


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Reading / Writing a file')
    parser.add_argument('-f', '--test_file', help='Test file name', default="test.txt", type=str)
    args = parser.parse_args()

    with open(args.test_file, 'wb') as f:
        write_order(f, Order.HELLO)

        write_i8(f, Order.MOTOR.value)
        write_i16(f, -56)
        write_i32(f, 131072)

    with open(args.test_file, 'rb') as f:
        # Equivalent to Order(read_i8(f))
        order = read_order(f)
        print(order)

        motor_order = read_order(f)
        print(motor_order)
        print(read_i16(f))
        print(read_i32(f))

    os.remove(args.test_file)
