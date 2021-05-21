# Importing Libraries
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from Feedback import Feedback_Window
from Recommended import Recommended_Window


class Home_Window(QMainWindow):
    def __init__(self, username, window_stack=None):
        """Load SignUp Ui Files and Extract all the user data"""
        super(Home_Window, self).__init__()

        uic.loadUi('C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Home_Window.ui', self)

        self.window_stack = window_stack
        self.username = username
        
        self.recommended_btn = self.findChild(QPushButton, 'Recommended_Button')
        self.recommended_btn.clicked.connect(self.recommended)

        self.feedback_btn = self.findChild(QPushButton, 'Feedback_Button')
        self.feedback_btn.clicked.connect(self.feedback)

        recomended_window = Recommended_Window(self.window_stack)
        self.window_stack.addWidget(recomended_window)

        feedback_window = Feedback_Window(self.username, self.window_stack)
        self.window_stack.addWidget(feedback_window)

    def recommended(self):
        self.window_stack.setCurrentIndex(2)                                     # Changing Window to Home Window
        self.window_stack.resize(1121, 861)                                      # Dimensions of Home Window
        self.window_stack.setWindowTitle("Recommended")                          # Changing Title of Stack to Home

    def feedback(self):
        self.window_stack.setWindowTitle("Feedback")            # Setting Title of Stack to Home
        self.window_stack.resize(1122, 865)
        self.window_stack.setCurrentIndex(3)                    # Adding Login Window to Window Stack


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))
    home_window = Home_Window()
    home_window.show()

    sys.exit(app.exec_())
