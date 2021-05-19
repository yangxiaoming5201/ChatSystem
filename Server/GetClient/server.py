import socket
import threading
import service

if __name__ == '__main__':
    # 初始化socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP地址和端口
    server.bind(("localhost", 8888))
    # 设置最大监听数
    server.listen(15)
    # 设置一个字典，用来保存每一个客户端的连接 和 身份信息
    print("服务器已启动。。。。")
    client_number = 0
    socket_mapping = {}
    # 开启准备等待获取客户端的链接
    while True:
        sc, addr = server.accept()
        # print(sc)

        # 为每一个客户端开启一个线程、保证程序的高效运行
        lock = threading.Lock()
        threading.Thread(target=service.get_client_info, args=(sc, socket_mapping, lock)).start()
        client_number += 1
        print(f'已经有{client_number}个客户端连接到服务器')
