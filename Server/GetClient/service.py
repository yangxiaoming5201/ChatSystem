import datetime
import json
import threading

from Client import Utils
from Server.GetClient import dao


def client_login():
    pass


recv_size = 10240


def get_client_info(user_socket, socket_mapping, lock):
    # 接收客户端的身份、并进行存储
    # 接收客户端的身份、并进行存储
    while True:
        lock.acquire()
        # 获取客户端发来的请求
        choice = user_socket.recv(recv_size).decode()
        d = dao.Dao()
        # 解析请求命令与数据
        cmd = choice.split('|')[0]
        data = eval(choice.split('|')[1])
        # print(choice)
        # 登录请求处理
        if cmd == 'login':
            # 要返回客户端的数据
            res_data = {'res': 0, 'user_info': None, 'friends': None}
            # 验证用户名和密码
            username = data['username']
            password = data['password']
            res = d.look_userinfo(username, password)
            if res is not None:
                u_id = res[0]
                socket_mapping[u_id] = user_socket
                print(f'用户：{username}已上线，他的昵称是：{res[2]}')
                res_data['res'] = 1
                res_data['user_info'] = res
                friends = d.look_friends(u_id)
                friend_info = {}
                for friend in friends:
                    friend_id = friend[1]
                    friend_nickname = d.look_nickname(friend_id)
                    friend_info[friend_id] = friend_nickname
                res_data['friends'] = friend_info
            # 将数据返回客户端
            user_socket.send(str(res_data).encode())

        elif cmd == 'register':
            res_data = {'res': 0}
            # 提取客户端发来的各个数据信息
            U_LoginID = data['U_LoginID']
            U_PassWord = data['U_PassWord']
            U_NickName = data['U_NickName']
            U_Name = data['U_Name']
            U_Sex = data['U_Sex']
            U_Age = data['U_Age']

            # 验证是否存在该用户
            if d.look_user(U_LoginID) is None:
                res_data['res'] = 1
                d.add_user(U_LoginID, U_PassWord, U_NickName, U_Name, U_Sex, U_Age)

            # 返给客户端该用户是否注册成功
            user_socket.send(str(res_data).encode())

        elif cmd == 'get_message':
            msg_data_list = []
            ua_id = data['ua_id']
            ub_id = data['ub_id']
            # 从数据库查找两个用户的聊天记录
            message = d.look_chat_message(ua_id, ub_id)

            # 将聊天记录封装为字典列表
            for msg_info in message:
                msg_data = {'from_u': msg_info[1], 'to_u': msg_info[2], 'msg': msg_info[3],
                            'msg_date': str(msg_info[4])}
                msg_data_list.append(msg_data)
            # print(msg_data_list)
            # 将聊天记录用字典列表发回客户端
            user_socket.send(str(msg_data_list).encode())
        elif cmd == 'send_msg':
            res_data = {'res': 1}
            d.add_messages(data['from_uid'], data['to_uid'], data['msg'], str(datetime.datetime.now()))
            user_socket.send(str(res_data).encode())
        elif cmd == 'add_friend':

            res_data = {'res': 0}
            # 通过客户端socket获取用户id
            u_id = Utils.get_key_by_value(socket_mapping, user_socket)
            friend_login_id = data['friend_login_id']
            friend_id = d.look_id(friend_login_id)
            print(friend_id, friend_login_id)

            # 判断是否是好友关系
            friends = d.look_friends(u_id)
            # 判断是都存在该用户
            if friend_id is not None:
                # 判断是否已经是好友关系
                if Utils.adjust_friend_relax(friends, friend_id[0]):
                    res_data['res'] = 2
                else:
                    res_data['res'] = 1
                    d.add_friend(u_id, friend_id[0])
                    d.add_friend(friend_id[0], u_id)
            # print(res_data)
            user_socket.send(str(res_data).encode())
        elif cmd == 'update_friends':
            res_data = {}
            u_id = Utils.get_key_by_value(socket_mapping, user_socket)
            friends = d.look_friends(u_id)
            friend_info = {}
            for friend in friends:
                friend_id = friend[1]
                friend_nickname = d.look_nickname(friend_id)
                friend_info[friend_id] = friend_nickname
            res_data['friends'] = friend_info
            user_socket.send(str(res_data).encode())
        elif cmd == 'delete_friend':
            res_data = {'res': 0}
            u_id = Utils.get_key_by_value(socket_mapping, user_socket)
            friend_login_id = data['friend_login_id']
            friends = d.look_friends(u_id)
            friend_id = d.look_id(friend_login_id)
            # 判断是否都存在该用户
            if friend_id is not None:
                # 判断是否已经是好友关系
                if Utils.adjust_friend_relax(friends, friend_id[0]):
                    res_data['res'] = 1
                    d.delete_friend(u_id, friend_id[0])
                    d.delete_friend(friend_id[0], u_id)
                else:
                    res_data['res'] = 2
            user_socket.send(str(res_data).encode())

        else:
            user_socket.send("sssss".encode())
        d.close()

        lock.release()
