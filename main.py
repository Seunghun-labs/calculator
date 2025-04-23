import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox)
from PyQt5.QtGui import QIcon # icon을 추가하기 위한 라이브러리

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.btn1 = QPushButton('Message', self) # Add Button
        self.btn1.clicked.connect(self.activateMessage) # if click button, connect handler function
        
        vbox = QVBoxLayout() # Create vertical layout widget
        vbox.addStretch(1) # space
        vbox.addWidget(self.btn1) # button of location
        vbox.addStretch(1) # space
        
        self.setLayout(vbox) # space - button - space layout setting
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()
        
    def activateMessage(self): # if click button, execute this function
        QMessageBox.information(self, 'information', 'Button clicked !')
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())