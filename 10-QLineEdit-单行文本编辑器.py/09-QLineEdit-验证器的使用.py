import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QValidator
from PyQt5.QtGui import *

# 通过继承重写QValidator，创建一个自定义的验证器
class AgeValidator(QValidator):
    def validate(self,input_str:str,pos_int:int):
        print(input_str,pos_int)
        try:
            if 18 < int(input_str) <= 180:
                return QValidator.Acceptable,input_str,pos_int
            elif 1<= int(input_str) <=17:
                return QValidator.Intermediate,input_str,pos_int
            else:
                return QValidator.Invalid,input_str,pos_int
        except Exception:
            # 如果用户还没有输入，输入字符为空
            if not input_str:
                return QValidator.Intermediate,input_str,pos_int
            return QValidator.Invalid,input_str,pos_int

    # 如果用户输入不满足要求，最后还会调用fixup方法修复



    def fixup(self,p_str:str) -> str:   # 结果有问题
        print("调用fixup")
        try:
            if int(p_str) < 18:  # 若用户最终输入小于18，则返回18
                return "18"
            return "180"  # 否则返回180
        except Exception:  # 如果没有输入
            return "18"

# 通过继承重写的QInValidator，更简单的实现年龄验证器
class MyAgeValidator(QIntValidator):
    def fixup(self,input:str) -> str:
        if len(input) == 0 or int(input) < 18:
            return "18"
        elif int(input) > 180:
            return "180"
        return input

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit-验证器的使用")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100,100)

        # 验证器举例：数字18-180：
        # 创建验证其实例
        validator = AgeValidator(le)
        # validator = MyAgeValidator(18,180,le)
        # 为le设置验证器
        le.setValidator(validator)

        # 对照没有设置验证器的line edit观察效果
        le2 = QLineEdit(self)
        le2.move(100,150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())



