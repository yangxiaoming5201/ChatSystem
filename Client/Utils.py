from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QMessageBox


def set_only_input_digital(control):
    """
    只能输入数字
    :return:
    """
    reg = QRegExp('[0-9]+$')
    validator = QRegExpValidator(control.parent())
    validator.setRegExp(reg)
    control.setValidator(validator)


def adjust_friend_relax(friends, friend_id):
    for friend in friends:
        if friend[1] == friend_id:
            return True
    return False


def set_encrypted_display(edit):
    """
    加密显示edit控件
    """
    edit.setEchoMode(QLineEdit.Password)  # 表示在用户界面的文本框内显示的信息是加密的


def get_key_by_value(dic, value):
    """:cvar
    根据字典的值查找对应的键
    """
    key_list = dic.keys()
    for key in key_list:
        if dic[key] == value:
            return key


def msg_dialog(msg):
    # 核心功能代码就两行，可以加到需要的地方
    msg_box = QMessageBox(QMessageBox.Warning, '警告', msg)
    msg_box.exec_()


def adjust_edit_empty(edit_list):
    """:type
    对多个edit判断是否为空，返回值为boolean
    """
    for edit in edit_list:
        if edit == "":
            return True
    return False
