import sys
from PyQt5.QtWidgets import QApplication,QLabel,QLabel,QWidget
from PyQt5.QtGui import QPixmap,QCursor
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("鼠标光标操作")
window.resize(500,500)
window.move(400,250)

# window.setCursor(Qt.ForbiddenCursor)
# window.setCursor(Qt.OpenHandCursor)

label = QLabel(window)
label.setText("muzing")
label.resize(300,300)
label.move(100,100)
label.setStyleSheet("background-color:cyan;")

# label.setCursor(Qt.ForbiddenCursor)  # 进入控件范围内，鼠标变化
pixmap = QPixmap("Icons\python_96px.ico")  # 图片路径
pixmap = pixmap.scaled(100,100)  # 重新设置大小
cursor = QCursor(pixmap,0,0)  # 0,0 为热点位置
label.setCursor(cursor)
# label.unsetCursor()  # 回复鼠标
current_cursor = label.cursor()
print(current_cursor.pos())  # 获取光标位置（相对于整个电脑屏幕）
current_cursor.setPos(100,100)
window.show()

sys.exit(app.exec_())



