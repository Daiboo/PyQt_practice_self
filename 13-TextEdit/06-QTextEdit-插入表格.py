import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextTableFormat,QTextLength
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QTextEdit-插入表格")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        te = QTextEdit(self)
        self.te = te
        te.setText("abc")

        test_btn = QPushButton("测试按钮",self)
        test_btn.move(350,140)
        test_btn.clicked.connect(self.test_btn_cao)

    def test_btn_cao(self):
        self.cursor_insert_table()

    def cursor_insert_table(self):
        tc = self.te.textCursor()  # 创建光标对象
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)  # 设置右对齐
        ttf.setCellPadding(0)  # 单元格边距  内边距
        ttf.setCellSpacing(10)  # 单元格间距  外边距
        ttf.setColumnWidthConstraints(
            (
                QTextLength(QTextLength.PercentageLength,50),
                QTextLength(QTextLength.PercentageLength,40),
                QTextLength(QTextLength.PercentageLength,10),
            )
        )   # 设置列宽约束，百分比约束
        table = tc.insertTable(5,3,ttf)  # 返回QTextTable
        # table.appendColumns(2)  # 对表格进行追加2列


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

 

        