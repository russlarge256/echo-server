import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    server_address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

    print(f'connecting to {server_address[0]} port {server_address[1]}',
          file=log_buffer)
    sock.connect(('127.0.0.1', 10000))

    full_msg = ''
    buffer = 55
    try:
        # send message to the server
        print(f'sending {msg}', file=log_buffer)
        send_it = bytes(msg, 'utf-8')
        sock.sendall(send_it)

        while True:
            # send back message in 16-byte chunks.
            # build entire reply from server (full_msg)
            server_message = sock.recv(buffer).decode('utf-8')
            full_msg += str(server_message)

            if len(server_message) < 55:
                break

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

    finally:
        return full_msg


if __name__ == '__main__':
    client('Hello over there, This is a Test.')


