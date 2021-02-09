import socket


class SockSendReceive(object):
    def __init__(self):
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 65432        # The port used by the server
        self.board = [3,3,3,3,3,3,3,3,3]

    def send(self):
        message = ""
        for x in self.board:
            message += str(x)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(bytes(message, 'utf-8'))
            data = s.recv(1024)

        print('Received', data)

    def rec(self):
        arr = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    for x in data.decode('utf-8'):
                        arr.append(int(x))
                    conn.sendall(data)
        self.board = arr
        print('Received', arr)