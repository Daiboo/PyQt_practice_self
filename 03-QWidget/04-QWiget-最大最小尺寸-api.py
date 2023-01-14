import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("最大最小尺寸限定")
# window.resize(500,500)
# window.setFixedSize(500,500)
window.setMinimumSize(200,200)
# window.setMinimumHeight(200)
window.setMaximumSize(500,500)
# window.resize(1000,1000)   # 同样收到500*500的限制

window.show()

sys.exit(app.exec_())



 