# QT Designer 연동 소스
import webbrowser
from PyQt5 import QtGui,QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./UI/NaverSearch.ui',self)

        #ui에 있는 위젯하고 연결하는 시그널 처리(컨트롤 이벤트처리)
        self.BtnSearch.clicked.connect(self.BtnSearch_Clicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)
        self.TxtSearchWord.returnPressed.connect(self.BtnSearch_Clicked)

    def tblResult_Selected(self):
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 1).text()
        #QMessageBox.about(self, 'URL', url)
        webbrowser.open(url)

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))

        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])

        n = 0
        for post in result:
            title = post['title'].replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&quot', '')
            self.tblResult.setItem(n, 0, QTableWidgetItem(title))
            self.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1

        self.tblResult.setColumnWidth(0, 400)
        self.tblResult.setColumnWidth(1, 300)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) #컬럼데이터 수정 금지

    def BtnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = [] 
        sNode = 'news'
        search_word = self.TxtSearchWord.text()
        display = 100

        if len(search_word) == 0:
            QMessageBox.about(self, 'popup', '검색어를 입력하세요')
            return

        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items']
        print(len(jsonResult))
        self.stsResult.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        
        # model = QtGui.QStandardItemModel()
        # self.LsvResult.setModel(model)

        # for post in jsonResult:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)
        self.makeTable(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())