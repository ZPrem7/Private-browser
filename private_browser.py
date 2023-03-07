import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *



class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Private Browser")
        self.setGeometry(50, 50, 800, 600)

        self.tabs = QTabWidget(self)
        self.tabs.setGeometry(0, 0, 800, 550)
        self.setCentralWidget(self.tabs)

        self.web = QWebEngineView()
        self.tabs.addTab(self.web, "New Tab")
        self.web.load(QUrl("https://www.google.com"))
        self.web.show()


        self.urlbar = QLineEdit(self)
        self.urlbar.setGeometry(0,550,700,50)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(700,550,50,50)
        self.back_button.clicked.connect(self.web.back)

        self.forward_button = QPushButton("Forward", self)
        self.forward_button.setGeometry(750,550,50,50)
        self.forward_button.clicked.connect(self.web.forward)

        self.new_tab_button = QPushButton("New Tab", self)
        self.new_tab_button.setGeometry(800, 550, 50, 50)
        self.new_tab_button.clicked.connect(self.add_new_tab)

        self.web.urlChanged.connect(self.update_urlbar)
        self.web.setZoomFactor(1)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)




    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.web.load(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def add_new_tab(self):
        tab_count = self.tabs.count()
        self.tabs.addTab(QWebEngineView(), "New Tab")
        self.tabs.setCurrentIndex(tab_count)

    def close_tab(self, index):
        self.tabs.removeTab(index)

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())
