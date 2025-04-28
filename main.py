import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1 = QPushButton('Message', self) # Add Button
        self.btn1.clicked.connect(self.activateMessage) # if click button, connect handler function
        
        self.btn2 = QPushButton('Clear', self)
        self.btn2.clicked.connect(self.clearMessage)
        
        hbox = QHBoxLayout() # Create horizontal layout widget
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox = QVBoxLayout() # Create vertical layout widget
        vbox.addWidget(self.te1) # TextEdit of location
        vbox.addLayout(hbox)
        # vbox.addWidget(self.btn1) # Button of location
        vbox.addStretch(1) # space
        
        self.setLayout(vbox) # space - button - space layout setting
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()
        
    def activateMessage(self): # if click button, execute this function
        # QMessageBox.information(self, 'information', 'Button clicked !')
        self.te1.appendPlainText("Button Clicked !")
        
    def clearMessage(self):
        self.te1.clear()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())