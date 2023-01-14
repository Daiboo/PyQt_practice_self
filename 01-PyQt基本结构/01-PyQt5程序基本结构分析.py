import sys
from PyQt5.QtWidgets import QApplication,QWidget,qApp,QLabel

# argv = sys.argv
# print(argv)
# try:
#     if argv[1] == '1':
#         print("传入了1")
# except IndexError:
#     print("可能未从外部传入参数")

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
print(app.arguments())

print(qApp.arguments())  # 全局变量
# 上面两个都是一样的


# 2.控件的操作
# 创建控件，设置控件（大小，位置，样式……），事件，信号的处理
# 2.1创建控件
# 当我们创建一个控件之后，如果该控件无父控件，则把它作为顶层控件（窗口）
# 系统会自动给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题、图标等）
window = QWidget()
window.setWindowTitle("这是一个窗口标题")
window.setGeometry(500,250,500,500)

# 控件也可以做为一个容器(承载其他控件)
label = QLabel(window)  # 注意要写明父类
label.setText("label里的文字")
label.move(100,100)

# 2.3展示控件
# 刚创建好一个控件之后（该控件无父控件），默认不会展示该控件，只有手动调用show()
window.show()

# 3.应用程序的执行， 进入到消息循环
# 让整个程序开始执行，并且进入到消息循环（无限循环）
# 检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())
