# Importing Libraries
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from Firebase_Operations import generate_feedback,user_exists
from Alerts_and_Messages import Message


class Feedback_Window(QMainWindow):
    def __init__(self,username, window_stack = None):
        """Load SignUp Ui Files and Extract all the user data"""
        super(Feedback_Window, self).__init__()

        uic.loadUi('C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Feedback_Window.ui', self)

        self.window_stack = window_stack
        self.username = username

        self.college_name = self.findChild(QComboBox,'College_Field')
        self.Infrastucture = self.findChild(QLineEdit, 'Infrastucture_Field')
        self.Placement = self.findChild(QLineEdit, 'Placement_Field')
        self.Academics = self.findChild(QLineEdit, 'Academics_Field')
        self.Campuslife = self.findChild(QLineEdit, 'Campuslife_Field')

        self.done_btn = self.findChild(QPushButton, 'Done_Button')

        self.done_btn.clicked.connect(self.exit)



    def exit(self):
        
        if user_exists("Feedback", self.username):
            Message(self, "Error", "You have already provided a review for a college.")

        else:

            generate_feedback(self.username, self.college_name.currentText() , self.Infrastucture.text(), self.Placement.text(), self.Academics.text(), self.Campuslife.text())
            Message(self, "Success", "Thank You for your Feedback.")

            self.window_stack.setWindowTitle("Home")                                           # Setting Title of Stack to Login
            self.window_stack.resize(1121, 863)                                                 # Dimensions of Login Window
            self.window_stack.setCurrentIndex(5)                                                # Adding Login Window to Login Window

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))
    feedback_window = Feedback_Window()
    feedback_window.show()

    sys.exit(app.exec_())