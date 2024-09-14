from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centralwidget.conect(self.generate)
    
    def generate(self):
        sings=""
        if self.ui.check1.isChecked():
            sings +="qwertyuiopasdfghjklzxcvbnm"
        if self.ui.check2.isChecked():
            sings +="1234567890"
        
        result =""
        number = random.randint(5,10)
        for __ in range(number):
            result+= random.choise(sings)

        result.ui.labels2.setText()
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()