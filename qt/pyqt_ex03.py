## QT5 사용자 윈도우 구성 예제
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My QT5 Window') #제목 표시줄
        self.setGeometry(80, 150, 600, 300)
        self.setWindowIcon(QIcon('./Resources/chart.png'))

        #label 추가
        self.label = QLabel('메시지: ', self)
        self.label.move(10, 10)
        self.label.setFixedSize(300, 20)
        #self.label.setGeometry(10,10,300,20)

        #button 추가
        self.btn = QPushButton('Click', self)
        self.btn.move(10, 50)

        #signal 추가
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메시지: 버튼클릭!!')

app = QApplication(sys.argv)

win = MyWindow()
win.show()
app.exec_()