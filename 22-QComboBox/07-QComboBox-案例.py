import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox-案例")
        self.resize(500,500)
        self.move(400,250)
        self.city_dic = {
            "北京": {"东城": "001", "西城": "002", "朝阳": "003", "丰台": "004"},
            "上海": {"黄埔": "005", "徐汇": "006", "长宁": "007", "静安": "008", "松江": "009"},
            "广东": {"广州": "010", "深圳": "011", "湛江": "012", "佛山": "013"},
        }
        self.setup_ui()

    def setup_ui(self):
        # 1.创建两个下拉列表控件
        pro_combobox = QComboBox(self)
        self.pro_combobox = pro_combobox
        city_combobox = QComboBox(self)
        self.city_combobox = city_combobox
        pro_combobox.move(100,100)
        city_combobox.move(250,100)

        # 3.监听 省下拉列表里卖弄当前值法伤改变的信号
        pro_combobox.currentIndexChanged[str].connect(self.pro_changed)

        # 4.监听 城市下拉列表里面的当前值发生改变的信号
        city_combobox.currentIndexChanged[int].connect(self.city_changed)

        # 2.展示数据第一个到下拉选择控件当中
        pro_combobox.addItems(self.city_dic.keys())

    def pro_changed(self,pro_name):
        print("调用pro_changed")
        # 1.根据省的名称，到字典中获取对应的城市字典
        cities = self.city_dic[pro_name]
        self.city_combobox.blockSignals(True)  # 暂时阻塞信号连接，防止clear时发生信号导致获得None
        self.city_combobox.clear()
        self.city_combobox.blockSignals(False)  # 恢复信号连接
        # self.city_combobox.addItems(cities.keys())  # 这个只添加键明
        for key,val in cities.items():
            self.city_combobox.addItem(key,val)

    def city_changed(self,item_idx):
        print("调用city_changed")
        print(self.city_combobox.itemData(item_idx))   # 打印出数据

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())






