import socket
import threading


class Client:
    recv_size = 102400

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务器
        self.client.connect(("localhost", 8888))
        self.lock = threading.Lock()

    def request(self, cmd, data):
        """:cvar
        请求会返回一个字典
        """
        self.lock.acquire()
        cmd_data_str = cmd + '|' + str(data)
        self.client.send(cmd_data_str.encode())
        res = eval(self.client.recv(self.recv_size).decode())
        # print(res)
        self.lock.release()
        return res


if __name__ == '__main__':
    client = Client()
