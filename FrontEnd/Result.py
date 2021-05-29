# Importing Libraries
import sys
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QMainWindow,QComboBox,QTextBrowser,QPushButton,QLabel
from PyQt5.QtGui import QPixmap, QIcon, QTextCursor

from Alerts_and_Messages import Message

dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\cutoff\\rating.csv")
class Result_Window(QMainWindow):
    def __init__(self,result, window_stack = None):
        """Load Recommended Ui Files and Extract all the user data"""
        super(Result_Window, self).__init__()
        
        

        uic.loadUi('C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Result_Window.ui', self)
        
        self.window_stack = window_stack
        self.result=result
        self.message_label = self.findChild(QTextBrowser,"Result_Field")
        self.location = self.findChild(QComboBox, "Location_Field")
        self.priority = self.findChild(QComboBox, "Priority_Field")
        self.order = self.findChild(QComboBox, "Sort_Field")
        self.apply_btn = self.findChild(QPushButton, 'Apply_Button') 
        self.apply_btn2 = self.findChild(QPushButton, 'Apply_Button_2')   
        self.apply_btn3 = self.findChild(QPushButton, 'Apply_Button_3')

        self.apply_btn.clicked.connect(self.filter1)
        self.apply_btn3.clicked.connect(self.filter2) 
        self.apply_btn2.clicked.connect(self.orderby)

        self.display()  
        
    def display(self):

        dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\rating.csv")

        l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]
        

        m1=[dr['College Code'][i] for i in l ]
        if(len(m1)>10):
            m1=m1[:10]
        else:
            m1=m1[:]

        m2=[dr['College Name'][i] for i in l ]
        if(len(m2)>10):
            m2=m2[:10]
        else:
            m2=m2[:]

        m3=[dr['Region'][i] for i in l]
        if(len(m3)>10):
            m3=m3[:10]
        else:
            m3=m3[:]

        m4=[dr['Location'][i] for i in l]
        if(len(m4)>10):
            m4=m4[:10]
        else:
            m4=m4[:]

        m5=[dr['Rating'][i] for i in l]
        if(len(m5)>10):
            m5=m5[:10]
        else:
            m5=m5[:]
        
        m6=[dr['College Infrastucture'][i] for i in l]
        if(len(m6)>10):
            m6=m6[:10]
        else:
            m6=m6[:]

        m7=[dr['Academics'][i] for i in l]
        if(len(m7)>10):
            m7=m7[:10]
        else:
            m7=m7[:]

        m8=[dr['Placements'][i] for i in l]
        if(len(m8)>10):
            m8=m8[:10]
        else:
            m8=m8[:]

        m9=[dr['Campus Life'][i] for i in l]
        if(len(m9)>10):
            m9=m9[:10]
        else:
            m9=m9[:]

        m10=[dr['Value for Money'][i] for i in l]
        if(len(m10)>10):
            m10=m10[:10]
        else:
            m10=m10[:]

        m11=[dr['Address'][i] for i in l]
        if(len(m11)>10):
            m11=m11[:10]
        else:
            m11=m11[:]

        
        m12=[dr['WebsiteLink'][i] for i in l]
        if(len(m12)>10):
            m12=m12[:10]
        else:
            m12=m12[:]

        m13=[dr['Fees'][i] for i in l]
        if(len(m13)>10):
            m13=m13[:10]
        else:
            m13=m13[:]


        c=1
        for i in range(0,len(m1)):
            self.message_label.append('\n'+"College Code:-"+str(m1[i])+
            '\n'+'\n'+"College Name:-"+m2[i]+
            '\n'+"City:-"+m4[i]+
            '\n'+"Address:-"+m11[i]+
            '\n'+'\n'+"Ratings:-"+" Overall Rating    : "+str(m5[i])+
            '\n'+'\n'+'\t'+" Infrastucture      : "+str(m6[i])+
            '\n'+'\t'+" Academics         : "+str(m7[i])+
            '\n'+'\t'+" Placement         : "+str(m8[i])+
            '\n'+'\t'+" Campus Life      : "+str(m9[i])+
            '\n'+'\t'+" Value Of Money : "+str(m10[i])+
            '\n'+'\n'"Fees:-"+str(m13[i])+'\n')

            self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
            self.message_label.setOpenExternalLinks(True)
    
            self.message_label.append("Website:- " +'<a href="{}" style="color:skyblue">{}</a>'.format(m12[i],m12[i]))

            self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
            self.message_label.setOpenExternalLinks(True)
    

            self.message_label.setStyleSheet("font-size:20px solid;color:white;background-color: rgb(52, 52, 52);")
            
            if c<len(m1):
                self.message_label.append(" ________________________________________________________________________________")
                c=c+1
        
    def filter1(self,location):

            dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\rating.csv")

            location = self.location.currentText() 

            self.message_label.clear()

            if(location=='-NONE-'):
                l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j] 
                
                m1=[dr['College Code'][i] for i in l ]
                if(len(m1)>10):
                    m1=m1[:10]
                else:
                    m1=m1[:]
        
                m2=[dr['College Name'][i] for i in l ]
                if(len(m2)>10):
                    m2=m2[:10]
                else:
                    m2=m2[:]

                m3=[dr['Region'][i] for i in l]
                if(len(m3)>10):
                    m3=m3[:10]
                else:
                    m3=m3[:]

                m4=[dr['Location'][i] for i in l]
                if(len(m4)>10):
                    m4=m4[:10]
                else:
                    m4=m4[:]

                m5=[dr['Rating'][i] for i in l]
                if(len(m5)>10):
                    m5=m5[:10]
                else:
                    m5=m5[:]

                m6=[dr['College Infrastucture'][i] for i in l]
                if(len(m6)>10):
                    m6=m6[:10]
                else:
                    m6=m6[:]

                m7=[dr['Academics'][i] for i in l]
                if(len(m7)>10):
                    m7=m7[:10]
                else:
                    m7=m7[:]

                m8=[dr['Placements'][i] for i in l]
                if(len(m8)>10):
                    m8=m8[:10]
                else:
                    m8=m8[:]

                m9=[dr['Campus Life'][i] for i in l]
                if(len(m9)>10):
                    m9=m9[:10]
                else:
                    m9=m9[:]

                m10=[dr['Value for Money'][i] for i in l]
                if(len(m10)>10):
                    m10=m10[:10]
                else:
                    m10=m10[:]

                m11=[dr['Address'][i] for i in l]
                if(len(m11)>10):
                    m11=m11[:10]
                else:
                    m11=m11[:]

                
                m12=[dr['WebsiteLink'][i] for i in l]
                if(len(m12)>10):
                    m12=m12[:10]
                else:
                    m12=m12[:]

                m13=[dr['Fees'][i] for i in l]
                if(len(m13)>10):
                    m13=m13[:10]
                else:
                    m13=m13[:]



            else:

                if(location=='MUMBAI'):
                    l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]
                    temp='Mumbai'


                elif(location=='NEW MUMBAI'):
                    l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]
                    temp='New Mumbai'

                    
                elif(location=='THANE'):
                    l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]
                    temp='Thane'



                m1=[dr['College Code'][i] for i in l if dr['Region'][i]==temp]
                if(len(m1)>10):
                    m1=m1[:10]
                else:
                    m1=m1[:]

                m2=[dr['College Name'][i] for i in l if dr['Region'][i]==temp]
                if(len(m2)>10):
                    m2=m2[:10]
                else:
                    m2=m2[:]

                m3=[dr['Region'][i] for i in l if dr['Region'][i]==temp]
                if(len(m3)>10):
                    m3=m3[:10]
                else:
                    m3=m3[:]

                m4=[dr['Location'][i] for i in l if dr['Region'][i]==temp]
                if(len(m4)>10):
                    m4=m4[:10]
                else:
                    m4=m4[:]

                m5=[dr['Rating'][i] for i in l if dr['Region'][i]==temp]
                if(len(m5)>10):
                    m5=m5[:10]
                else:
                    m5=m5[:]

                m6=[dr['College Infrastucture'][i] for i in l if dr['Region'][i]==temp]
                if(len(m6)>10):
                    m6=m6[:10]
                else:
                    m6=m6[:]

                m7=[dr['Academics'][i] for i in l if dr['Region'][i]==temp]
                if(len(m7)>10):
                    m7=m7[:10]
                else:
                    m7=m7[:]

                m8=[dr['Placements'][i] for i in l if dr['Region'][i]==temp]
                if(len(m8)>10):
                    m8=m8[:10]
                else:
                    m8=m8[:]

                m9=[dr['Campus Life'][i] for i in l if dr['Region'][i]==temp]
                if(len(m9)>10):
                    m9=m9[:10]
                else:
                    m9=m9[:]

                m10=[dr['Value for Money'][i] for i in l if dr['Region'][i]==temp]
                if(len(m10)>10):
                    m10=m10[:10]
                else:
                    m10=m10[:]

                m11=[dr['Address'][i] for i in l if dr['Region'][i]==temp]
                if(len(m11)>10):
                    m11=m11[:10]
                else:
                        m11=m11[:]

                    
                m12=[dr['WebsiteLink'][i] for i in l if dr['Region'][i]==temp]
                if(len(m12)>10):
                    m12=m12[:10]
                else:
                    m12=m12[:]

                m13=[dr['Fees'][i] for i in l if dr['Region'][i]==temp]
                if(len(m13)>10):
                    m13=m13[:10]
                else:
                    m13=m13[:]


            

            if len(m1)==0:
                Message(self, "WARNING", "- No Matching Found -")

            c=1
            for i in range(0,len(m1)):
                self.message_label.append('\n'+"College Code:-"+str(m1[i])+
                    '\n'+'\n'+"College Name:-"+m2[i]+
                    '\n'+"City:-"+m4[i]+
                    '\n'+"Address:-"+m11[i]+
                    '\n'+'\n'+"Ratings:-"+" Overall Rating    : "+str(m5[i])+
                    '\n'+'\n'+'\t'+" Infrastucture      : "+str(m6[i])+
                    '\n'+'\t'+" Academics         : "+str(m7[i])+
                    '\n'+'\t'+" Placement         : "+str(m8[i])+
                    '\n'+'\t'+" Campus Life      : "+str(m9[i])+
                    '\n'+'\t'+" Value Of Money : "+str(m10[i])+
                    '\n'+'\n'"Fees:-"+str(m13[i])+'\n')

                self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
                self.message_label.setOpenExternalLinks(True)
            
                self.message_label.append("Website:- " +'<a href="{}" style="color:skyblue">{}</a>'.format(m12[i],m12[i]))

                self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
                self.message_label.setOpenExternalLinks(True)
            
                self.message_label.setStyleSheet("font-size:20px solid;color:white;background-color: rgb(52, 52, 52);")
                if c<len(m1):
                    self.message_label.append(" ________________________________________________________________________________")
                    c=c+1

    def filter2(self,priority):

        
            dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\rating.csv")

            priority = self.priority.currentText() 
            

            self.message_label.clear()
            
            dict={}
     
            if(priority=='-NONE-'):
                l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j] 

            elif(priority=='INFRASTUCTURE'):  
                for i in self.result:
                    for j in range(0,31):
                        if dr['College Code'][j]==i:
                            key=dr['College Infrastucture'][j]
                    dict[i]=key
                l=sorted(dict.items(),key=lambda x:x[1],reverse=True)
                dict={i:j for i,j in l}
                l=[i for i in dict.keys()]
                l=[i for j in l for i in range(0,31) if dr['College Code'][i]==j]
            

            elif(priority=='PLACEMENT'):              
                for i in self.result:
                    for j in range(0,31):
                        if dr['College Code'][j]==i:
                            key=dr['Placements'][j]
                    dict[i]=key
                l=sorted(dict.items(),key=lambda x:x[1],reverse=True)
                dict={i:j for i,j in l}
                l=[i for i in dict.keys()]
                l=[i for j in l for i in range(0,31) if dr['College Code'][i]==j]
            

            elif(priority=='ACADEMICS'):             
                for i in self.result:
                    for j in range(0,31):
                        if dr['College Code'][j]==i:
                            key=dr['Academics'][j]
                    dict[i]=key
                l=sorted(dict.items(),key=lambda x:x[1],reverse=True)
                dict={i:j for i,j in l}
                l=[i for i in dict.keys()]
                l=[i for j in l for i in range(0,31) if dr['College Code'][i]==j]
                

            elif(priority=='FACULTY'):
                for i in self.result:
                    for j in range(0,31):
                        if dr['College Code'][j]==i:
                            key=dr['Campus Life'][j]
                    dict[i]=key
                l=sorted(dict.items(),key=lambda x:x[1],reverse=True)
                dict={i:j for i,j in l}
                l=[i for i in dict.keys()]
                l=[i for j in l for i in range(0,31) if dr['College Code'][i]==j]
        

            m1=[dr['College Code'][i] for i in l ]
            if(len(m1)>10):
                m1=m1[:10]
            else:
                m1=m1[:]
        
            m2=[dr['College Name'][i] for i in l ]
            if(len(m2)>10):
                m2=m2[:10]
            else:
                m2=m2[:]

            m3=[dr['Region'][i] for i in l]
            if(len(m3)>10):
                m3=m3[:10]
            else:
                m3=m3[:]

            m4=[dr['Location'][i] for i in l]
            if(len(m4)>10):
                m4=m4[:10]
            else:
                m4=m4[:]

            m5=[dr['Rating'][i] for i in l]
            if(len(m5)>10):
                m5=m5[:10]
            else:
                m5=m5[:]

            m6=[dr['College Infrastucture'][i] for i in l]
            if(len(m6)>10):
                m6=m6[:10]
            else:
                m6=m6[:]

            m7=[dr['Academics'][i] for i in l]
            if(len(m7)>10):
                m7=m7[:10]
            else:
                m7=m7[:]

            m8=[dr['Placements'][i] for i in l]
            if(len(m8)>10):
                m8=m8[:10]
            else:
                m8=m8[:]

            m9=[dr['Campus Life'][i] for i in l]
            if(len(m9)>10):
                m9=m9[:10]
            else:
                m9=m9[:]

            m10=[dr['Value for Money'][i] for i in l]
            if(len(m10)>10):
                m10=m10[:10]
            else:
                m10=m10[:]

            m11=[dr['Address'][i] for i in l]
            if(len(m11)>10):
                m11=m11[:10]
            else:
                m11=m11[:]

                
            m12=[dr['WebsiteLink'][i] for i in l]
            if(len(m12)>10):
                m12=m12[:10]
            else:
                m12=m12[:]

            m13=[dr['Fees'][i] for i in l]
            if(len(m13)>10):
                m13=m13[:10]
            else:
                m13=m13[:]



            if len(m1)==0:
                Message(self, "WARNING", "- No Matching Found -")

            c=1
            for i in range(0,len(m1)):
                self.message_label.append('\n'+"College Code:-"+str(m1[i])+
                    '\n'+'\n'+"College Name:-"+m2[i]+
                    '\n'+"City:-"+m4[i]+
                    '\n'+"Address:-"+m11[i]+
                    '\n'+'\n'+"Ratings:-"+" Overall Rating    : "+str(m5[i])+
                    '\n'+'\n'+'\t'+" Infrastucture      : "+str(m6[i])+
                    '\n'+'\t'+" Academics         : "+str(m7[i])+
                    '\n'+'\t'+" Placement         : "+str(m8[i])+
                    '\n'+'\t'+" Campus Life      : "+str(m9[i])+
                    '\n'+'\t'+" Value Of Money : "+str(m10[i])+
                    '\n'+'\n'"Fees:-"+str(m13[i])+'\n')

                self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
                self.message_label.setOpenExternalLinks(True)
            
                self.message_label.append("Website:- " +'<a href="{}" style="color:skyblue">{}</a>'.format(m12[i],m12[i]))

                self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
                self.message_label.setOpenExternalLinks(True)
            
                self.message_label.setStyleSheet("font-size:20px solid;color:white;background-color: rgb(52, 52, 52);")
                if c<len(m1):
                    self.message_label.append(" ________________________________________________________________________________")
                    c=c+1



               

    def orderby(self,order):

            dr=pd.read_csv("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\Dataset\\rating.csv")

            order = self.order.currentText() 

            self.message_label.clear()
  
            if(order=='-NONE-'):

                l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j] 
                
    #SORTED BY NAME
            
            elif(order=="SORT BY NAME"):
                
                l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]            # Finding position of college code in position 
                l=[dr['College Name'][i] for i in l ]                                                  # Evaluate college name for obtained position
                l=[i for j in sorted(l) for i in range(0,31) if dr['College Name'][i]==j]
                
                
    #SORTED BY FEES

            elif(order=="SORT BY FEES"):
                
                l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]
                l=[dr['Fees'][i] for i in l ]
                l=[i for j in sorted(l) for i in range(0,31) if dr['Fees'][i]==j]
                
    
    #SORTED BY CITY
            
            elif(order=="SORT BY CITY"):
                
                l=[i for j in self.result for i in range(0,31) if dr['College Code'][i]==j]
                l=[dr['Location'][i] for i in l ]
                l=[i for j in sorted(l) for i in range(0,31) if dr['Location'][i]==j]
                

            
            m1=[dr['College Code'][i] for i in l ]
            if(len(m1)>10):
                m1=m1[:10]
            else:
                m1=m1[:]
        
            m2=[dr['College Name'][i] for i in l ]
            if(len(m2)>10):
                m2=m2[:10]
            else:
                m2=m2[:]

            m3=[dr['Region'][i] for i in l]
            if(len(m3)>10):
                m3=m3[:10]
            else:
                m3=m3[:]

            m4=[dr['Location'][i] for i in l]
            if(len(m4)>10):
                m4=m4[:10]
            else:
                m4=m4[:]

            m5=[dr['Rating'][i] for i in l]
            if(len(m5)>10):
                m5=m5[:10]
            else:
                m5=m5[:]

            m6=[dr['College Infrastucture'][i] for i in l]
            if(len(m6)>10):
                m6=m6[:10]
            else:
                m6=m6[:]

            m7=[dr['Academics'][i] for i in l]
            if(len(m7)>10):
                m7=m7[:10]
            else:
                m7=m7[:]

            m8=[dr['Placements'][i] for i in l]
            if(len(m8)>10):
                m8=m8[:10]
            else:
                m8=m8[:]

            m9=[dr['Campus Life'][i] for i in l]
            if(len(m9)>10):
                m9=m9[:10]
            else:
                m9=m9[:]

            m10=[dr['Value for Money'][i] for i in l]
            if(len(m10)>10):
                m10=m10[:10]
            else:
                m10=m10[:]

            m11=[dr['Address'][i] for i in l]
            if(len(m11)>10):
                m11=m11[:10]
            else:
                m11=m11[:]

                
            m12=[dr['WebsiteLink'][i] for i in l]
            if(len(m12)>10):
                m12=m12[:10]
            else:
                m12=m12[:]

            m13=[dr['Fees'][i] for i in l]
            if(len(m13)>10):
                m13=m13[:10]
            else:
                m13=m13[:]
    

            c=1
            for i in range(0,len(m1)):
                self.message_label.append('\n'+"College Code:-"+str(m1[i])+
                '\n'+'\n'+"College Name:-"+m2[i]+
                '\n'+"City:-"+m4[i]+
                '\n'+"Address:-"+m11[i]+
                '\n'+'\n'+"Ratings:-"+" Overall Rating    : "+str(m5[i])+
                '\n'+'\n'+'\t'+" Infrastucture      : "+str(m6[i])+
                '\n'+'\t'+" Academics         : "+str(m7[i])+
                '\n'+'\t'+" Placement         : "+str(m8[i])+
                '\n'+'\t'+" Campus Life      : "+str(m9[i])+
                '\n'+'\t'+" Value Of Money : "+str(m10[i])+
                '\n'+'\n'"Fees:-"+str(m13[i])+'\n')

                self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
                self.message_label.setOpenExternalLinks(True)
        
                self.message_label.append("Website:- " +'<a href="{}" style="color:skyblue">{}</a>'.format(m12[i],m12[i]))

                self.message_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
                self.message_label.setOpenExternalLinks(True)
        
                self.message_label.setStyleSheet("font-size:20px solid;color:white;background-color: rgb(52, 52, 52);")
                if c<len(m1):
                    self.message_label.append(" ________________________________________________________________________________")
                    c=c+1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Ui Files\\Images\\Student_Icon"))
    result_window=Result_Window()

    result_window.show()
    sys.exit(app.exec_())
