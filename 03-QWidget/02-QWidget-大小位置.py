import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton

app = QApplication(sys.argv)

window = QWidget()
# window.resize(500,500)
window.setFixedSize(500,500)  # 固定尺寸
window.move(200,200)

label = QLabel(window)
label.setText("ABC")
label.move(100,100)
label.setStyleSheet("background-color:cyan;")

def change_cao():
    new_content = label.text() + "ABC"
    label.setText(new_content)
    # label.resize(label.width() + 100,label.height())  # 必须增大labeL的大小才能使更差的文本显示出来
    label.adjustSize()  # 根据内容自适应大小

btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100,300)
btn.clicked.connect(change_cao)

# window.setGeometry(0,0,150,150)

window.show()

print(window.x())
print(window.width())
print(window.geometry())

sys.exit(app.exec_())





