from __future__ import print_function, division

import argparse

import bluetooth

from robust_serial import write_i32, read_i32

PORT = 4885
# show mac address: hciconfig
SERVER_ADDR = "B8:27:EB:F1:E4:5F"


def receive_messages():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", PORT))
    server_sock.listen(1)

    client_sock, client_address = server_sock.accept()
    print("Accepted connection from {}".format(client_address))
    client_sock.read = client_sock.recv

    number = read_i32(client_sock)
    print("Received: {}".format(number))

    client_sock.close()
    server_sock.close()


def send_message(mac_address):
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((mac_address, PORT))
    socket.write = socket.send
    write_i32(socket, -32768)
    socket.close()


def discover_devices():
    nearby_devices = bluetooth.discover_devices()
    for bdaddr in nearby_devices:
        print("{} + [{}]".format(bluetooth.lookup_name(bdaddr), bdaddr))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test bluetooth server/client connection")
    arg_group = parser.add_mutually_exclusive_group(required=True)
    arg_group.add_argument("-s", "--server", dest="server",
                           action='store_true', default=False, help="Create a server")
    arg_group.add_argument("-c", "--client", dest="client",
                           action='store_true', default=False, help="Create a client")
    args = parser.parse_args()
    if args.server:
        receive_messages()
    else:
        send_message(SERVER_ADDR)
