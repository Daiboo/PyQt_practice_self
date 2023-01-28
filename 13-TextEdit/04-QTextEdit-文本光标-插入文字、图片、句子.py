import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QTextEdit-文本光标")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        te = QTextEdit(self)
        self.te = te

        test_btn = QPushButton("测试按钮",self)
        test_btn.move(350,140)
        test_btn.clicked.connect(self.test_btn_cao)

    def test_btn_cao(self):
        print(self.te.document())  # 返回QTextDocument
        print(self.te.textCursor())  # 返回  QTextCursor
        self.光标插入内容()

    def 光标插入内容(self):
        # tcf = QTextCharFormat()   # 文本字符格式
        # tcf.setToolTip("我是一个Tooltip")
        # tcf.setFontFamily("PingFang SC-Regular")  # 字体，以及字体的类型
        # tcf.setFontPointSize(10)  
        
        tc = self.te.textCursor()  # 创建一个文本光标对象，在光标处插入，动词：insert
        # tc.insertText("光标插入文字",tcf)
        # tc.insertHtml("<a href='https://muzing.top'>muzing的个人博客</a>")

        # -------插入图片-----------
        # tif = QTextImageFormat()
        # tif.setName("Icons/search_48px.ico")  # 里面的字符串仅仅是名字str
        # tif.setWidth(30)
        # tif.setHeight(30)
        # tc.insertImage(tif)

        # ------插入句子----------
        # tdf = QTextDocumentFragment.fromHtml("<h2>muzing</h2>")
        tdf = QTextDocumentFragment.fromPlainText("<h2>muzing</h2>")
        tc.insertFragment(tdf)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())


