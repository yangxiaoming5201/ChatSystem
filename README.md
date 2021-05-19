# ChatSystem
基于python的在线聊天系统
1.本程序客户端启动必须先配置好数据库再开启服务器
2.服务器的启动方法：Server中的server代码
3.客户端的启动方式，运行Client目录下的main
4.数据库的更改在server的dao中


-----------以下数据库创建程序----------
create database chatsystem;
create table chatsystem.user
(
	U_ID int auto_increment,
	U_LoginID varchar(25) null,
	U_NickName varchar(25) null,
	U_PassWord varchar(25) null,
	U_Name varchar(25) null,
	U_Sex bit null,
	U_Age int null,
	constraint user_pk
		primary key (U_ID)
);
create table chatsystem.friends
(
    F_ID       int auto_increment
        primary key,
    F_FirendID int null,
    F_UserID   int null,
    constraint Friends_user_U_ID_fk
        foreign key (F_UserID) references user (U_ID),
    constraint Friends_user_U_ID_fk_2
        foreign key (F_FirendID) references user (U_ID)
);
create table chatsystem.Messages
(
    M_ID           int auto_increment,
    M_FromUserID   int      null,
    M_ToUserID     int      null,
    M_PostMessages text     null,
    M_Time         datetime null,
    constraint Messages_pk
        primary key (M_ID),
    constraint Messages_user_U_ID_fk
        foreign key (M_FromUserID) references user (U_ID),
    constraint Messages_user_U_ID_fk_2
        foreign key (M_ToUserID) references user (U_ID)
);
