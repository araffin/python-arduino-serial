from __future__ import print_function, division, absolute_import

import time
import threading

from robust_serial import write_order, Order
from robust_serial.threads import CommandThread, ListenerThread

from robust_serial.utils import open_serial_port, CustomQueue


def reset_command_queue():
    """
    Clear the command queue
    """
    command_queue.clear()


if __name__ == '__main__':
    try:
        serial_file = open_serial_port(baudrate=115200)
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

    # Create Command queue for sending orders
    command_queue = CustomQueue(2)
    # Number of messages we can send to the Arduino without receiving an acknowledgment
    n_messages_allowed = 3
    n_received_semaphore = threading.Semaphore(n_messages_allowed)
    # Lock for accessing serial file (to avoid reading and writing at the same time)
    serial_lock = threading.Lock()

    # Event to notify threads that they should terminate
    exit_event = threading.Event()

    print("Starting Communication Threads")
    # Threads for arduino communication
    threads = [CommandThread(serial_file, command_queue, exit_event, n_received_semaphore, serial_lock),
               ListenerThread(serial_file, exit_event, n_received_semaphore, serial_lock)]
    for t in threads:
        t.start()

    # Send 3 orders to the arduino
    command_queue.put((Order.MOTOR, -56))
    command_queue.put((Order.SERVO, 120))
    time.sleep(2)
    #
    command_queue.put((Order.MOTOR, 0))

    # End the threads
    exit_event.set()
    n_received_semaphore.release()

    print("Exiting...")

    for t in threads:
        t.join()
