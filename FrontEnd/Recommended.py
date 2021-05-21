# Importing Libraries
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton,QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from Alerts_and_Messages import Message

from Source import Source
from Loading import Loading_Window

class Recommended_Window(QMainWindow):
    def __init__(self, window_stack = None):
        """Load Recommended Ui Files and Extract all the user data"""
        super(Recommended_Window, self).__init__()

        
        
        uic.loadUi('C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Recommended_Window.ui', self)

        self.window_stack = window_stack

        self.rank_field = self.findChild(QLineEdit, 'Rank_Field')
        self.city_field = self.findChild(QLineEdit, 'City_Field')
        self.gender_field = self.findChild(QComboBox, 'Gender_Field')
        self.category_field = self.findChild(QComboBox, 'Category_Field')
        self.minority_field = self.findChild(QComboBox, 'Minorit_Field')
        self.branch_field = self.findChild(QComboBox, 'Branch_Field')

        self.predict_btn = self.findChild(QPushButton, 'Predict_Button')
        self.predict_btn.clicked.connect(self.validation)

    

    def validation(self):
        
        global rank,gender,category,minority,branch,city

        rank = self.rank_field.text()                                                  # Extract rank from the Field
        city=self.city_field.text()                                                    # Extract city from the Field
        gender = self.gender_field.currentText()                                       # Extract gender from the Field
        category = self.category_field.currentText()                                   # Extract category from the Field
        minority = self.minority_field.currentText()                                   # Extract minority from the Field
        branch = self.branch_field.currentText()                                       # Extract branch from the Field

        
        if rank == '' or gender=='-Select-'  or branch=='-Select-' or city=='':   # If Either of Fields are Blank or Not Selected
            Message(self, "WARNING", "Please Fill all the Details.") 

        elif category =='-Select-' and minority =='-Select-'  :
            Message(self, "WARNING", "Please Fill all the Details.") 
        
        elif category !='-Select-' and minority !='-Select-'  :
            Message(self, "ERROR", "Please Select Category or Minority.") 
        
        elif int(rank)<0:
            Message(self, "ERROR", "Rank should be Positive.") 
        
        else:
            self.predict_btn = self.findChild(QPushButton, 'Predict_Button') 
            self.predict_btn.clicked.connect(self.result)

        

        if branch=='Computer Science (CS)':
            branch='cs'
        elif branch=="Information Technology (IT)":
            branch='it'
        elif branch=="Mechanical (ME)":
            branch='me'
        elif branch=="Civil (CE)":
            branch='ce'
        elif branch=="Chemical (CH)":
            branch='ch'
        elif branch=="Electroninc & Telecommuniction (EXTC)":
            branch='ee'   
        


 
    def result(self):

        m='minor'
        result=[]
        if category!='-Select-':                                                    #FOR CATEGORY
            l=list(Source.show(category,int(rank),branch))
            loading_window=Loading_Window(l,self.window_stack)
            self.window_stack.addWidget(loading_window) 
    
            """Change the Current Window to Result Window"""
            self.window_stack.setCurrentIndex(5)                                        # Changing Window to Loading Window
            self.window_stack.setGeometry(600,350,680,400)                               # Dimensions of Loading Window  
            
            self.window_stack.setWindowTitle("Loading")                                   # Dimensions of Loading Window
   

        else:                                                                          #FOR MINORITY
            l=list(Source.show(m,int(rank),branch,minority))
            loading_window=Loading_Window(l,self.window_stack)
            self.window_stack.addWidget(loading_window) 
    
    
            """Change the Current Window to Result Window"""
            self.window_stack.setCurrentIndex(5)                                        # Changing Window to Loading Window
            self.window_stack.setGeometry(600,350,680,400)                               # Dimensions of Loading Window
            self.window_stack.setWindowTitle("Loading")                                    # Dimensions of Loading Window
    

    
    def exit(self):
        self.window_stack.setWindowTitle("Login")  # Setting Title of Stack to Home
        self.window_stack.resize(1129,838)
        self.window_stack.setCurrentIndex(0)  # Adding Login Window to Window Stack


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))
    
       
    recommended_window = Recommended_Window()
    recommended_window.show()


    sys.exit(app.exec_())