import sys

from PyQt5 import QtCore, uic, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *


from Result import Result_Window


counter = 0                                                                                 # Global Counter for Progress Bar percentage


class Loading_Window(QMainWindow):                                                          
    def __init__(self,l, window_stack = None):
        super(Loading_Window, self).__init__()

        uic.loadUi("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Loading_Window.ui", self)                                      # Loading the Ui File

        self.window_stack = window_stack
        self.l=l
    
        self.dropShadowFrame = self.findChild(QFrame, 'dropShadowFrame')                    # Drop Shadow Frame
        self.progress_bar = self.findChild(QProgressBar, 'Progress_Bar')                    # Progress Bar

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)                                   # Removing Title Bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)                               # Translucent Background

        self.shadow = QGraphicsDropShadowEffect(self)                                       # Creating a Shadow
        self.shadow.setBlurRadius(200)                                                      # Blur Radius of Shadow
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)                                 # Applying Shadow to Drop Shadow Frame

        self.timer = QtCore.QTimer()                                                        # Timer Object
        self.timer.timeout.connect(self.progress)
        self.timer.start(30)                                                                # Start Timer with 30 Millisecond delays


        self.show()

    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress_bar.setValue(counter)

        if counter > 100:
            # STOP TIMER
            self.timer.stop()

                                                                    
            result_window=Result_Window(self.l,self.window_stack)
            self.window_stack.addWidget(result_window) 
            
            """Change the Current Window to Result Window"""
            self.window_stack.setCurrentIndex(7)                                        # Changing Window to Result Window
            self.window_stack.setGeometry(400,90,1112,859)                             # Dimensions of Result Window
            self.window_stack.setWindowTitle("Result")                                   # Dimensions of Result Window

            self.close()                                                            # close loading screen

        counter += 1                                                                # Increasing the Progressbar Percentage


if __name__ == "__main__":
    app = QApplication(sys.argv)   

    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))                     # SETTING APPLICATION ICON   


    sys.exit(app.exec_())