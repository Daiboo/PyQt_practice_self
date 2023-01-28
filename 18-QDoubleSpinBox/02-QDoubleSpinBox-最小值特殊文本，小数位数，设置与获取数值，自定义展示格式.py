import sys

from PyQt5.QtWidgets import *


# ------自定义展示格式--------
class MyDoubleSpinBox(QDoubleSpinBox):
    def textFromValue(self, v: float) -> str:
        print("v",v)
        return str(v) + "**"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        dsb = MyDoubleSpinBox(self)
        dsb.move(100,100)
        dsb.resize(200,30)

        # ----------最小值特殊文本--------
        dsb.setSpecialValueText("达到最小值了!")

        # ----------设置小数位数---------
        dsb.setDecimals(3)  # 默认两位小数

        # --------设置数值---------
        dsb.setValue(66.666)   # 如果设置的小数位数过多，会按照真实的位数四舍五入

        # ---------获取数值----------
        print(dsb.value())  # 获取数值
        print("cleanText",dsb.cleanText())  # 包含任何前后缀
        print(dsb.lineEdit().text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())