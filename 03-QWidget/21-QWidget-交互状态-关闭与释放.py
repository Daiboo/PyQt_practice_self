import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("交互状态-关闭")
window.resize(500,500)
window.move(400,250)

btn  = QPushButton(window)
btn.setText("按钮")
btn.destroyed.connect(lambda: print("按钮被释放了"))

# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()
# btn.deleteLater()

btn.setAttribute(Qt.WA_DeleteOnClose,True)  # 关闭时释放对象属性
btn.close()
# btn.show()

window.show()

sys.exit(app.exec_())

# 关闭仍然保留在内存中，释放 在内存中删除
