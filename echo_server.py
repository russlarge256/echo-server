import socket
import sys
import traceback


def server(log_buffer=sys.stderr):

    # set an address for the server
    server_address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

    # log that server is built
    print(f"Making a server on: {server_address[0]}:{server_address[1]}",
          file=log_buffer)

    # bind sock to above address. begin to listen for incoming connections
    sock.bind(('127.0.0.1', 10000))
    sock.listen(1)

    try:
        while True:
            # create new connections to sockets
            print('waiting for a connection...', file=log_buffer)

            # make new socket when client connects
            clientsocket, address = (sock.accept())
            print(f'connection from {address} has been established.',
                  file=log_buffer)

            # set buffer size
            buffer_size = 55

            try:
                print(f'connection - {server_address[0]}:{server_address[1]}',
                      file=log_buffer)
                while True:
                    data = (clientsocket.recv(buffer_size)).decode('utf-8')

                    # add fixed-length (16 bytes) header!
                    # receive messages sent by the client

                    print(f"Received {data} from Client.", file=log_buffer)
                    clientsocket.sendall(bytes(data, 'utf-8'))
                    print(f"Sent {data} to Client.", file=log_buffer)
                    if len(data) < 55:
                        break

                return data

            except Exception as e:
                traceback.print_exc()
                print(e)
                sys.exit(1)
            finally:
                print('closing client socket connection...', file=log_buffer)
                clientsocket.close()
                sys.exit(0)
    except KeyboardInterrupt:
        pass
        print('quitting echo server...')

if __name__ == '__main__':
    server()
    sys.exit(0)
