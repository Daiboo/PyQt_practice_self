from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QObject
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号的曹祖")
        self.resize(500,500)
        self.move(400,250)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject信号的操作_destroy()
        self.QObject信号的操作_namechanged()
        
        
    def QObject信号的操作_destroy(self):
        self.obj = QObject()

        def destroy_slot(obj):
            print("对象被释放了",obj)

        self.obj.destroyed.connect(destroy_slot)  # 关闭程序的一瞬间释放掉了

    def QObject信号的操作_namechanged(self):
        self.obj = QObject()

        def obj_name_slot(name):
            print("对象名称发生改变:",name)

        self.obj.objectNameChanged.connect(obj_name_slot)  # 建立信号与槽的连接
        self.obj.setObjectName("AAA")
        print("此时有",self.obj.receivers(self.obj.objectNameChanged),"个槽信号与该信号连接")

        def receiver_test_slot():
            pass
        self.obj.objectNameChanged.connect(receiver_test_slot)
        print("此时有",self.obj.receivers(self.obj.objectNameChanged),"个槽信号与该信号连接")
        
        # self.obj.objectNameChanged.disconnect()  # 取消信号与槽的连接

        print("连接是否被阻断: ",self.obj.signalsBlocked())  # 检查信号与曹的连接是否被阻断
        self.obj.blockSignals(True)  # 暂时阻断信号与曹的连接
        print("连接是否被阻断: ",self.obj.signalsBlocked())

        self.obj.setObjectName("BBB")

        self.obj.blockSignals(False)  # 回复信号与曹的连接

        print("连接是否被阻断: " ,self.obj.signalsBlocked())

        self.obj.setObjectName("CCC")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())





