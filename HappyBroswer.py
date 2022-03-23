# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


class MainWindow(QMainWindow):

 
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
 
        self.browser = QWebEngineView()
 
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        self.setStyleSheet('QLineEdit {background-color:green}')

 
        self.browser.urlChanged.connect(self.update_urlbar)
 
        self.browser.loadFinished.connect(self.update_title)
 
        self.setCentralWidget(self.browser)
 
        self.status = QStatusBar()
 
        self.setStatusBar(self.status)
 
        navtb = QToolBar("Navigation bar:")

        self.addToolBar(navtb)
 
        home_btn = QAction("Go to DuckDuckGo!", self)
        home_btn.setStatusTip("Go to DuckDuckGo!")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)


 
        navtb.addSeparator()
 
        self.urlbar = QLineEdit()
 
        self.urlbar.returnPressed.connect(self.navigate_to_url)
 
        navtb.addWidget(self.urlbar)

 
 
        self.show()
 
 
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Happy Broswer 1.0!" % title)
 
 
    def navigate_home(self):

 
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
 
    def navigate_to_url(self):
 
        q = QUrl(self.urlbar.text())
 
        if q.scheme() == "":
            q.setScheme("https")
 
        self.browser.setUrl(q)
 
    def update_urlbar(self, q):
 
        self.urlbar.setText(q.toString())
 
        self.urlbar.setCursorPosition(0)
 
 
fss = QApplication(sys.argv)

fss.setApplicationName("Happy Broswer by Jonathan Steadman!")
fss.setWindowIcon(QIcon('icon.png'))

 
 
window = MainWindow()
fss.exec_()