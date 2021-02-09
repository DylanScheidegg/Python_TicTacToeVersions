import socket


class SockSendReceive(object):
    def __init__(self):
        self.HOST = '127.0.0.1'  # The server's hostname or IP address
        self.PORT = 65432        # The port used by the server

    def send(self):
        arr = ['4','5','6']
        lis = ""
        for x in arr:
            lis += x

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(bytes(lis, 'utf-8'))
            data = s.recv(1024)

        print('Received', data)

    def rec(self):
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

                    arr = []
                    for x in data.decode('utf-8'):
                        # print(x)
                        arr.append(int(x))
                    print(arr)
                    conn.sendall(data)