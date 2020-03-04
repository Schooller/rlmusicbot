import socket


class Client:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        data = self.s.recv(1024).decode()

    def send_text(self, text):
        self.s.send((text + '\n\r').encode())
        self.s.recv(10240).decode()
        data = self.s.recv(10240).decode()
        return data


if __name__ == "__main__":
    pass
