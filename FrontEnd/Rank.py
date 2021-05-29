# Importing Libraries
import sys
import pandas as pd

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QPushButton
from PyQt5.QtGui import QIcon

class Rank_Window(QMainWindow):

    def __init__(self, window_stack = None):
        """Load the Login Window and Extract the username, password and run validation"""

        super(Rank_Window, self).__init__()
        uic.loadUi('C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\Rank_Window.ui', self)                          # Load the .ui file

        self.window_stack = window_stack
        self.message_label = self.findChild(QTextBrowser,"Rank_Field")

        self.back_btn = self.findChild(QPushButton, 'Back_Button')
        self.back_btn.clicked.connect(self.back)

        
        dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\rating.csv")

        c=1
        
        for i in range(0,31):
            if c==1:
                self.message_label.append(" "+"RANK"+"\t"+"COLLEGE NAME")
            self.message_label.setStyleSheet("font-size:20px solid;color:white;background-color: rgb(52, 52, 52);")
            self.message_label.append('\n')
            self.message_label.append(" "+str(c) +'\t'+dr['College Name'][i])
            c=c+1 

    def back(self):
        self.window_stack.setCurrentIndex(5)                                     # Changing Window to Home Window
        self.window_stack.resize(1121, 863)                                      # Dimensions of Home Window
        self.window_stack.setWindowTitle("Home")                                 # Changing Title of Stack to Home


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))
    rank_window = Rank_Window()
    rank_window.show()

    sys.exit(app.exec_())