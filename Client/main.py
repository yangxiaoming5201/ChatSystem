import datetime
import sys
from time import sleep
from multiprocessing import Queue

import queue

from PyQt5 import QtCore, Qt
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtGui import QTextOption, QPicture, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QMessageBox, QDialog
import threading
import login
import register
from client import Client
import chatFriend
import Utils
import addFriend
import deleteFriend


class DeleteWindow(QMainWindow, deleteFriend.Ui_MainWindow):
    def __init__(self, client):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.event_listing()

    def delete_friend(self):
        friend_id = self.friend_login_id_edit.text()
        data = {'friend_login_id': friend_id}
        res_data = self.client.request('delete_friend', data)
        if res_data['res'] == 0:
            self.add_notice_label.setText("没有该用户！")
        elif res_data['res'] == 1:
            self.add_notice_label.setText("该好友已经被删除！")
        else:
            self.add_notice_label.setText("该用户与您不是好友关系，不能删除！")

    def delete_friend_thread(self):
        threading.Thread(target=self.delete_friend).start()

    def event_listing(self):
        self.delete_friend_button.clicked.connect(self.delete_friend_thread)
        pass


class AddWindow(QMainWindow, addFriend.Ui_MainWindow):
    def __init__(self, client):
        super().__init__()
        self.setupUi(self)
        self.alert = QMessageBox(self)
        self.client = client
        self.event_listen()

        self.input_verification()

    def setupUi(self, m):
        super(AddWindow, self).setupUi(m)

    def input_verification(self):
        Utils.set_only_input_digital(self.friend_login_id_edit)

    def add_friend(self):
        friend_login_id = self.friend_login_id_edit.text()
        data = {'friend_login_id': friend_login_id}
        res = self.client.request('add_friend', data)
        if res['res'] == 0:
            self.add_notice_label.setText("提示：没有该用户")
        elif res['res'] == 2:
            self.add_notice_label.setText("提示：已经与该用户建立好友关系")
        else:
            self.add_notice_label.setText("提示：好友已添加成功")

    def add_friend_thread(self):
        threading.Thread(target=self.add_friend).start()

    def event_listen(self):
        self.add_friend_button.clicked.connect(self.add_friend_thread)


class MainWindow(QMainWindow, chatFriend.Ui_MainWindow):
    def __init__(self, client, queue):
        super().__init__()
        self.data = None
        self.u_id = None
        self.friends_keys = None
        self.current_friend_id = None
        self.old_msg = ""
        self.text = ""
        self.no_label = ""
        self.queue = queue
        self.client = client
        self.add_window = AddWindow(client)
        self.delete_window = DeleteWindow(client)
        self.setupUi(self)
        # 获取登录过程中放入队列的数据，格式：{'res': 1, 'user_info': (3, '36', 'ds', 's', 's', b'\x01', 36), 'friends': {2: 's',
        # 1: 'ming'}}
        self.events_listening()
        self.th = threading.Thread(target=self.update_msg)

    def setupUi(self, mw):
        """:cvar
        设置界面UI
        """
        super(MainWindow, self).setupUi(mw)
        self.all_chat_text.setWordWrapMode(QTextOption.WordWrap)
        self.chat_with_who_notice.setStyleSheet("color:red;")
        self.chat_data_text.setPlaceholderText('请输入您要发的消息。。。')
        self.all_chat_text.ensureCursorVisible()
        self.images_label.setPixmap(QPixmap('logo.gif'))
        self.all_chat_text.updatesEnabled()
        self.friend_list_update.setIcon(QIcon('resizeApi.png'))
        self.raise_()

        threading.Thread(target=self.label_update).start()

    def label_update(self):
        """:cvar
        让提示标签动起来
        """

        while True:
            for i in range(1, 7):
                self.chat_with_who_notice.setText(self.no_label + '.' * i)
                sleep(0.5)

    def show_message(self):

        # 防止列表空数据出错
        if self.firend_list.count() == 0:
            return
        # 获取当前聊天对象的id
        current_index = self.firend_list.currentIndex().row()
        self.current_friend_id = list(self.friends_keys)[current_index]
        # 提交给服务器自己与聊天对象的id
        data = {'ua_id': self.u_id, 'ub_id': self.current_friend_id}
        # 从服务器请求对应好友的聊天信息
        res = self.client.request('get_message', data)
        # self.all_chat_text.clear()
        # print(res)
        self.text = ""
        # 给对话框添加聊天记录
        for msg_data in res:
            from_u = msg_data['from_u']
            # to_u = msg_data['to_u']
            msg = msg_data['msg']
            msg_date = msg_data['msg_date']
            if from_u != self.u_id:
                if self.firend_list.currentItem() is None:
                    return
                title = self.firend_list.currentItem().text() + '     ' + msg_date
                self.text += f'<hr><div align="left"><div><span style="font-size:10px;color: blue;font-family: 微软雅黑,serif;padding-right: 10px;padding-left: 10px;">{title}</span></div><div><span  style="padding-left:15px;padding-right:15px;background-color: cadetblue; color: honeydew;border-radius: 15px;font-family: 楷体,serif;font-size: 15pt;">{msg}</span></div></div>'
            else:
                title = self.data['user_info'][2] + '     ' + msg_date
                self.text += f'<hr><div align="right"><div><span style="font-size:10px;color: blue;font-family: 微软雅黑,serif;padding-right: 10px;padding-left: 10px;">{title}</span></div><div><span style="padding-left:15px;padding-right:15px;background-color: cadetblue; color: honeydew;border-radius: 15px;font-family: 楷体,serif;font-size: 15pt">{msg}</span></div></div>'
        # 判断聊天框是否被清空，否则就连接数据
        if len(self.all_chat_text.toPlainText()) == 0:
            self.old_msg = ""
        if self.old_msg == self.text:
            return
        else:
            # 如果内容清空就重新载入而不是连接新的一条数据
            print(self.all_chat_text.toPlainText())
            s = self.text
            self.text = self.text.replace(self.old_msg, '')
            self.old_msg = s
        self.all_chat_text.append(self.text)
        cursor = self.all_chat_text.textCursor()
        pos = len(self.all_chat_text.toPlainText())
        cursor.setPosition(pos)
        self.all_chat_text.setTextCursor(cursor)

    def show_message_thread(self):
        # 清空聊天框
        self.all_chat_text.clear()
        # 设置与谁聊天的动态信息
        self.chat_with_who_notice.setText(f"正在与{self.firend_list.currentItem().text()}对话")
        self.no_label = self.chat_with_who_notice.text()
        sleep(0.5)
        # 显示聊天信息
        # threading.Thread(target=self.show_message).start()

    def update_msg(self):
        """:cvar
        
        """
        while True:
            sleep(1)
            # threading.Thread(target=self.all_chat_text.clear).start()
            # print("update")
            self.show_message()

    def send_msg(self):

        msg = self.chat_data_text.toPlainText()
        data = {'from_uid': self.u_id, 'to_uid': self.current_friend_id, 'msg': msg}
        res = self.client.request('send_msg', data)
        # print(res)

    def send_msg_thread(self):
        if self.firend_list.count() == 0:
            self.chat_data_text.clear()
            self.chat_data_text.setPlaceholderText('您没有好友，请添加好友')
            return
        # 输入内容空判断
        if len(self.chat_data_text.toPlainText()) == 0:
            self.chat_data_text.setPlaceholderText('不能发送空内容')
            return
        # sleep(0.25)

        threading.Thread(target=self.send_msg).start()
        # 防止过早清除内容
        sleep(0.3)
        self.chat_data_text.clear()
        # self.show_message_thread()

    def add_friend(self):
        self.add_window.add_notice_label.clear()
        self.add_window.show()

    def delete_friend(self):
        self.delete_window.add_notice_label.clear()
        self.delete_window.show()

    def update_friends_list(self):
        self.firend_list.clear()
        res_data = self.client.request('update_friends', {'u_id': self.u_id})
        friends = res_data['friends']
        self.friends_keys = friends.keys()
        # 将好友添加到好友列表，并显示昵称
        for f_key in self.friends_keys:
            nickname = friends[f_key]
            self.firend_list.addItem(QListWidgetItem(nickname))

    def update_friends_list_thread(self):
        # print("update_friends_list_thread")
        threading.Thread(target=self.update_friends_list).start()

    def events_listening(self):
        # 列表好友点击事件更新聊天记录
        self.firend_list.itemClicked.connect(self.show_message_thread)
        # 发送消息更新聊天记录
        self.send_button.clicked.connect(self.send_msg_thread)
        # 添加按钮的点击事件
        self.add_friend_button.clicked.connect(self.add_friend)
        # 好友列表的更新事件
        self.friend_list_update.clicked.connect(self.update_friends_list_thread)
        # 删除好友
        self.delete_friend_button.clicked.connect(self.delete_friend)
        # self.group_chat_button.clicked.connect(lambda: self.all_chat_text.clear())

    def show(self):
        self.init_data()

        super(MainWindow, self).show()

    def init_data(self):
        self.data = self.queue.get()
        # 初始化个人信息
        self.u_id = self.data['user_info'][0]
        login_id = self.data['user_info'][1]
        nick_name = self.data['user_info'][2]
        name = self.data['user_info'][4]
        sex = '男' if self.data['user_info'][5] else '女'
        age = self.data['user_info'][6]
        info = f'昵称:{nick_name}\n账号：{login_id}\n姓名：{name}\n性别：{sex}\n年龄：{age}'
        self.info_label.setText(info)
        # 获取朋友信息
        friends = self.data['friends']
        # 获取朋友的账号id
        self.friends_keys = friends.keys()
        # 清空好友列表
        self.firend_list.clear()
        # 将好友添加到好友列表，并显示昵称
        for f_key in self.friends_keys:
            nickname = friends[f_key]
            self.firend_list.addItem(QListWidgetItem(f'{nickname}'))
        # 睡眠一秒，让列表完全载入数据
        sleep(1)
        self.th.start()


class RegisterWindow(QMainWindow, register.Ui_MainWindow):
    def __init__(self, cliente):
        super().__init__()
        self.client = client
        self.setupUi(self)
        Utils.set_only_input_digital(self.reg_age_edit)
        # 注册按钮点击事件监听

        self.reg_button.clicked.connect(self.regis_thread)
        self.input_verification()

    def regis_thread(self):
        # 给注册过程发分配一个线程
        threading.Thread(target=self.register()).start()

    def register(self):
        # 从表单获取数据
        U_LoginID = self.reg_username_edit.text()
        U_PassWord = self.reg_password_edit.text()
        U_NickName = self.reg_nickname_edit.text()
        U_Name = self.reg_name_edit.text()
        U_Sex = True if self.reg_sex_comboBox.currentText() else False
        U_Age = self.reg_age_edit.text()
        confirm_password = self.reg_confirm_password_edit.text()
        # 验证两次输入的密码
        if U_PassWord != confirm_password:
            Utils.msg_dialog("两次密码不匹配！")
            return
        # 研究表单空字段
        if Utils.adjust_edit_empty([U_LoginID, U_PassWord, U_NickName, U_Name, U_Age]):
            Utils.msg_dialog("请不要留有空数据！")
            return
        # 提交给服务器的数据
        data = {'U_LoginID': U_LoginID, 'U_PassWord': U_PassWord, 'U_NickName': U_NickName, 'U_Name': U_Name,
                'U_Sex': U_Sex, 'U_Age': U_Age}
        # 获取服务器的注册请求响应，格式：{'res': 0}
        res = self.client.request('register', data)
        if res['res'] == 0:
            Utils.msg_dialog("该用户已存在")
        else:
            Utils.msg_dialog("注册成功")
        # 关闭注册窗口
        self.close()

    def input_verification(self):
        Utils.set_only_input_digital(self.reg_username_edit)


class LoginWindow(QMainWindow, login.Ui_MainWindow):
    def __init__(self, client):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.queue = Queue()

        # 主窗口对象
        self.main_window = MainWindow(client, self.queue)
        # 注册窗口对象
        self.register_window = RegisterWindow(client)
        self.events_listing()
        self.input_verification()

    def setupUi(self, window):
        super().setupUi(window)
        self.notice_label.setStyleSheet("color:red")
        w = self.width()
        self.notice_label.resize(w, self.notice_label.height())

    def input_verification(self):
        Utils.set_only_input_digital(self.uesrname_edit)
        Utils.set_encrypted_display(self.password_edit)

    def login_trg(self):
        """
        登录提交与响应处理
        :return
        """
        # 获取用户名和密码
        username = self.uesrname_edit.text()
        password = self.password_edit.text()
        # 文本框验证
        if len(username) != 0 and len(password) != 0:
            # 要发给服务器的数据
            form_str = {'username': username, 'password': password}
            self.notice_label.setText("")
            # 向服务器请求登录并返回数据格式：{'res': 0, 'user_info': None, 'friends': None}
            res = self.client.request('login', form_str)
            # print(res)
            if res['res'] == 0:
                self.notice_label.setText("登录信息有误")
            if res['res'] == 1:
                self.queue.put(res)
        else:
            self.notice_label.setText("用户名或密码不能为空！")

    def login_thread(self):
        """:cvar
        登录线程启动执行登录操作
        """
        threading.Thread(target=self.login_trg).start()
        # 沉睡一秒，接受服务器响应处理
        sleep(1)
        if self.queue.empty():
            self.notice_label.setText("登录失败！")
        else:
            self.notice_label.setText("登录成功！")
            # 打开聊天窗口
            self.main_window.show()
            # 关闭登录窗口
            self.close()

    def events_listing(self):
        """
        开启登录界面的监听事件
        :return:
        """
        # 登录按钮的监听事件
        self.login_button.clicked.connect(self.login_thread)
        # 注册窗口的监听事件
        self.register_button.clicked.connect(self.register_window.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = Client()
    lw = LoginWindow(client)
    lw.show()
    sys.exit(app.exec_())
