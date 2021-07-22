import io
import sys
import folium
#pip install PyQt5 | PyQtWebEngine
from PyQt5 import QtWidgets, QtWidgets, QtWebEngineWidgets #PyQtWebEngine 추가 설치 -> QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv) #create Qt winform

m = folium.Map(location = [35.1175, 129.0903], zoom_start = 12, tiles='Cartodb Positron') #create folium map

data = io.BytesIO() #byte로
m.save(data, close_file=False) #map data save

win = QtWebEngineWidgets.QWebEngineView() # create QT5 Web Engine
win.setHtml(data.getvalue().decode()) ## covert html to Binary map data
win.resize(800, 600) #resize winform
win.show()

sys.exit(app.exec_()) # sys.exit()
