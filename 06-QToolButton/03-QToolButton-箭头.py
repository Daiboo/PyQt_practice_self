import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QToolButton箭头")
window.resize(500, 500)
window.move(400, 250)

tb = QToolButton(window)
tb.setText("这是一个QToolButton")
# 注意：即使设置了文字和图标，也不一定显示
tb.setIcon(QIcon("Icons/search_48px.ico"))
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# tb.setArrowType(Qt.NoArrow)
# tb.setArrowType(Qt.UpArrow)  # 向上的箭头
# tb.setArrowType(Qt.DownArrow)
# tb.setArrowType(Qt.LeftArrow)
# tb.setArrowType(Qt.RightArrow)


window.show()

sys.exit(app.exec_())
