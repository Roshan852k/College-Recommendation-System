import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from qt_material import apply_stylesheet



class Message_Box(QMainWindow):
    def __init__(self):
        super(Message_Box, self).__init__()

        uic.loadUi("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\Message_Box.ui", self)

        self.message_label = self.findChild(QLabel, "Message_Label")
        self.ok_btn = self.findChild(QPushButton, "OK_Button")

        self.ok_btn.clicked.connect(lambda: self.close())
    
    
    def display(self, code, message):
        self.setWindowTitle(code)
        self.message_label.setText(message)
        self.message_label.setStyleSheet("color:white;")



def Message(self, code, message):
    self.message_box = Message_Box()
    self.message_box.display(code, message)
    self.message_box.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Main Application
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon")) #Setting Applicatin Icon
    apply_stylesheet(app, theme='dark_amber.xml')  # Setting Theme of Application



    sys.exit(app.exec_())