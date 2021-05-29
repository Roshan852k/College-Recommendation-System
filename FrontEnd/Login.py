# Import Libraries
import sys
import PyQt5
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton ,QStackedWidget

from Firebase_Operations import user_exists, get_data, generate_log
from Alerts_and_Messages import Message
from SignUp import SignUp_Window
from Home import Home_Window


class Login_Window(QMainWindow):

    def __init__(self, window_stack = None):
        """Load the Login Window and Extract the username, password and run validation"""

        super(Login_Window, self).__init__()
        uic.loadUi('C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\Login_Window.ui', self)                          # Load the .ui file

        self.window_stack = window_stack

        self.username_field = self.findChild(QLineEdit, 'Username_Field')               # Username Field
        self.password_field = self.findChild(QLineEdit, 'Password_Field')               # Password Field

        login_button = self.findChild(QPushButton, 'Login_Button')                      # Login Button
        login_button.clicked.connect(self.login_validation)                             # Call login_validation on Button Press

        sign_up_btn = self.findChild(QPushButton, 'SignUp_Button')                      # Register Button
        sign_up_btn.clicked.connect(self.register)                                      # Call Register on Button Press

    def login_validation(self):
        """Validate the username and password"""
        username = self.username_field.text()                                           # Extract Username form the Field
        password = self.password_field.text()                                           # Extract Password form the Field

        if username == '' or password == '':                                            # If Either of Fields are Blank
            Message(self, "WARNING", "Please Fill all the Details.")                    # Display Error Message

        elif user_exists("Users", username):                                            # If username exists in the database
            if password == get_data(username, "Password"):                              # And Passwords Match as well
                generate_log(username, "Sign-in")                                       # Create a Log in database that a User has signed in

                Message(self, "SUCCESS", "Login Suceessfully.") 

                home_window = Home_Window(username, self.window_stack)
                self.window_stack.addWidget(home_window)
                self.window_stack.setCurrentIndex(5)                                     # Changing Window to Home Window
                self.window_stack.resize(1121, 863)                                      # Dimensions of Home Window
                self.window_stack.setWindowTitle("Home")                                 # Changing Title of Stack to Home

            else:                                                                        # If Password does not match in database
                Message(self, "ERROR", "Invalid Password")
        else:                                                                            # If Username doesn't Exist in the Database
            Message(self, "ERROR", "Username Does not Exist.")

    def register(self):
        """Change the Current Window to Register Window"""
        self.window_stack.setCurrentIndex(1)                                             # Changing Window to Register Window
        self.window_stack.setWindowTitle("SignUp")                                       # Changing Title of Stack to Signup
        self.window_stack.resize(1121, 864)                                              # Dimensions of Signup Window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))
    login_window = Login_Window()
    login_window.show()

    window_stack = QStackedWidget()  

    login_window = Login_Window(window_stack)                                             
    signup_window = SignUp_Window(window_stack)
                                     

    window_stack.setWindowTitle("Login")                                                 # SETTING TITLE OF STACK TO LOGIN
    window_stack.resize(1129, 838)                                                       # DIMENSIONS OF LOGIN WINDOW

    window_stack.addWidget(login_window)                                                                                               
    window_stack.addWidget(signup_window)
    
    window_stack.show()

    sys.exit(app.exec_())