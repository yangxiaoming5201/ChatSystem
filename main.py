import sys

from PyQt5.QtWidgets import QListWidgetItem, QApplication, QListWidget, QMainWindow, QTextBrowser


class MyList(QListWidget):
    def __init__(self):
        QListWidget.__init__(self)
        self.add_items()
        self.itemClicked.connect(self.item_click)
        print(self.count())

    def add_items(self):
        for item_text in ['item1', 'item2']:
            item = QListWidgetItem(item_text)
            self.addItem(item)

    def item_click(self, item):
        print(item, item.text(), item.flags)


class yy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500, 500)
        self.text_browser = QTextBrowser(self)
        self.text_browser.resize(200, 200)
        self.text_browser.setHtml('<div align="left">sss</div><div align="right">sss</div>')

        self.text_browser.append(
            '<br><div align="right"><div><font color="blue" size="0.5" >姓名和事件</font></div><div>消息</div></div>')
        self.text_browser.append(
            '<br><div align="left"><div><font color="blue" size="0.5" >姓名和事件</font></div><div>消息</div></div>')
        print(self.text_browser.toHtml())


        self.show()


from multiprocessing import Queue

if __name__ == '__main__':
    app = QApplication([])
    # myList = MyList()
    # myList.show()
    # q=Queue()
    # q.put("sss")
    # print(q.empty())
    # print(q.get())
    u = yy()
    s="fjdsid"
    s.replace("fj","")
    print(s)
    # s={}
    # s.keys()
    sys.exit(app.exec_())
