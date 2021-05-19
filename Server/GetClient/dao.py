import datetime

import pymysql


class Dao:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root",
                                    password="root", database="chatsystem")
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_user(self, U_LoginID, U_PassWord, U_NickName, U_Name, U_Sex, U_Age):
        """
        添加一个聊天用户
        :param qq:
        :param password:
        :param nickname:
        :return:
        """
        sql = f"insert into user( U_LoginID,U_PassWord, U_NickName, U_Name, U_Sex, U_Age) value{U_LoginID, U_PassWord, U_NickName, U_Name, U_Sex, U_Age} "
        self.cursor.execute(sql)
        self.conn.commit()

    def look_user(self, qq):
        """
        根据qq查找聊天用户
        :param qq:
        :return:
        """
        sql = f"select * from user where U_LoginID='{qq}'"

        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchone()

    def look_userinfo(self, qq, password):
        """
        根据qq查找聊天用户
        :param password:
        :param qq:
        :return:
        """
        sql = f"select * from user where U_LoginID='{qq}' and U_PassWord='{password}'"
        # print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchone()

    def look_all(self):
        sql = f"select * from user"

        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    def look_friends(self, u_id):
        """:cvar
        根据id查找朋友
        """
        sql = f'select * from friends where F_UserID={u_id}'

        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    def look_id(self, U_LoginID):
        sql = f"select U_ID from user where U_LoginID='{U_LoginID}'"

        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchone()

    def look_chat_message(self, ua_id, ub_id):
        sql = f"select * from messages where (M_FromUserID={ua_id} and M_ToUserID={ub_id})" \
              f" or (M_FromUserID={ub_id} and M_ToUserID={ua_id}) order by M_Time"

        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

    def look_nickname(self, U_ID):
        sql = f"select U_NickName from user where U_ID={U_ID}"
        self.cursor.execute(sql)
        self.conn.commit()
        nickname = self.cursor.fetchone()[0]
        return nickname

    def add_messages(self, from_uid, to_uid, msg, date):
        sql = f"insert into messages(M_FromUserID,M_ToUserID,M_PostMessages,M_Time) value({from_uid},{to_uid},'{msg}','{date}')"

        self.cursor.execute(sql)
        self.conn.commit()

    def add_friend(self, u_id, friend_id):
        sql = f"insert into friends(F_FirendID,F_UserID) value({friend_id},{u_id})"

        self.cursor.execute(sql)
        self.conn.commit()

    def delete_friend(self, u_id, friend_id):
        sql = f"delete from friends where F_UserID={u_id} and F_FirendID={friend_id}"
        self.cursor.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    d = Dao()
    # print(d.look_userinfo('02', 's'))
    # print(d.look_user(12))
    # s = d.look_chat_message(2, 3)
    # d.add_messages(3, 1, 'hahah', str(datetime.datetime.now()))
    # d.add_friend(3,5)

    # user('09', '05', 'haha', 'ming', True, 22))
    # print((d.look_friends(3)))
    # print(d.look_nickname(3))
    # print(d.look_id('2512396404'))
    pass
