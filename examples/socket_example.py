from __future__ import print_function, division

import argparse
import socket

from robust_serial import write_i8, write_i32, read_i8, read_i32

PORT = 4444
SERVER_ADDR = "localhost"

class SocketAdapter(object):
    """
    Wrapper around socket object to use the robust_serial lib
    It just renames recv() to read() and send() to write()
    """

    def __init__(self, client_socket):
        super(SocketAdapter, self).__init__()
        self.client_socket = client_socket

    def read(self, num_bytes):
        return self.client_socket.recv(num_bytes)

    def write(self, num_bytes):
        return self.client_socket.send(num_bytes)

    def close(self):
        return self.client_socket.close()


def receive_messages():
    """
    Receive messages (server side)
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT))
    print("Waiting for client...")
    # Wait for client
    server_socket.listen(1)

    client_sock, client_address = server_socket.accept()
    print("Accepted connection from {}".format(client_address))
    # Wrap socket to work with the lib
    client_sock = SocketAdapter(client_sock)

    for i in range(10):
        print("Received (i8): {}".format(read_i8(client_sock)))
    big_number = read_i32(client_sock)

    print("Received (i32): {}".format(big_number))

    print("Server exiting...")
    client_sock.close()
    server_socket.close()


def send_messages(server_address):
    """
    Send messages (client side)
    :param server_address: (str)
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, PORT))

    # Wrap socket to work with the lib
    client_socket = SocketAdapter(client_socket)

    print("Connected to {}".format(server_address))
    for i in range(10):
        write_i8(client_socket, i)
    write_i32(client_socket, 32768)
    print("Client exiting...")
    client_socket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test socket server/client connection")
    arg_group = parser.add_mutually_exclusive_group(required=True)
    arg_group.add_argument("-s", "--server", dest="server",
                           action='store_true', default=False, help="Create a server")
    arg_group.add_argument("-c", "--client", dest="client",
                           action='store_true', default=False, help="Create a client")
    args = parser.parse_args()
    if args.server:
        receive_messages()
    else:
        send_messages(SERVER_ADDR)
