from __future__ import print_function, division, absolute_import
from tempfile import TemporaryFile

from robust_serial import Order, write_i8, write_i16, write_i32, read_i8, read_i16, read_i32


def assert_eq(left, right):
    assert left == right, "{} != {}".format(left, right)


def test_read_write_orders():
    motor_speed = -57
    servo_angle = 512  # 2^9
    big_number = -32768  # -2^15

    f = TemporaryFile()

    write_i8(f, Order.MOTOR.value)
    write_i8(f, motor_speed)

    write_i8(f, Order.SERVO.value)
    write_i16(f, servo_angle)

    write_i8(f, Order.ERROR.value)
    write_i32(f, big_number)

    f.seek(0, 0)
    read_1st_order = Order(read_i8(f))
    read_motor_speed = read_i8(f)

    read_2nd_order = Order(read_i8(f))
    read_servo_angle = read_i16(f)

    read_3rd_order = Order(read_i8(f))
    read_big_number = read_i32(f)

    assert_eq(read_1st_order, Order.MOTOR)
    assert_eq(read_motor_speed, motor_speed)

    assert_eq(read_2nd_order, Order.SERVO)
    assert_eq(read_servo_angle, servo_angle)

    assert_eq(read_3rd_order, Order.ERROR)
    assert_eq(read_big_number, big_number)