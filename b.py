import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,  QMessageBox, QLabel
from PyQt5 import uic
from math import *
from PyQt5.QtGui import QIcon
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui',self)
        self.setWindowTitle('A-calc')  
        self.setWindowIcon(QIcon('a.png')) 
        
        self.pushButton1.clicked.connect(self.run)
        self.pushButton2.clicked.connect(self.run)
        self.pushButton3.clicked.connect(self.run)
        self.pushButton4.clicked.connect(self.run)
        self.pushButton5.clicked.connect(self.run)
        self.pushButton6.clicked.connect(self.run)
        self.pushButton7.clicked.connect(self.run)
        self.pushButton8.clicked.connect(self.run)
        self.pushButton9.clicked.connect(self.run)
        self.pushButton0.clicked.connect(self.run)
        self.pushButtonc.clicked.connect(self.dell)
        self.pushButtond.clicked.connect(self.run)
        self.pushButtonm.clicked.connect(self.run)
        self.pushButtona.clicked.connect(self.run)
        self.pushButtoneq.clicked.connect(self.eq)
        self.pushButtonid.clicked.connect(self.run)
        self.pushButtonmod.clicked.connect(self.run)
        self.pushButton10.clicked.connect(self.run)
        self.pushButtons.clicked.connect(self.run)
        
    def run(self, n):
        n = str(self.sender().text())

        if n[0] == '&':
            n = n[1]
        print(n)
        s = self.label.text()
   
        self.label.setText(s + n)
        self.label_3.setText(s + n)
        
        try:
            self.label_2.setText(str(round(eval(s+n), 10)))
        except:
            self.label_2.setText('')
        

                
        
    def dell(self):
        self.label.setText('')
        self.label_2.setText('')
        self.label_3.setText('')
        
    def eq(self):
        s = str(self.label.text())
        try:
            self.label.setText(str(round(eval(s), 10)))
            self.label_2.setText(str(round(eval(s), 10)))
            self.label_3.setText(str(round(eval(s), 10)))
        except:
            self.label_3.setText('ERROR')
    
    def keyPressEvent(self, event):

        if event.text() == '\r':
            s = str(self.label.text())
            try:
                self.label.setText(str(round(eval(s), 10)))
                self.label_3.setText(str(round(eval(s), 10)))

            except:
                self.label_3.setText('ERROR')
                
            
        if event.text() == '':
            s = str(self.label.text())
            try:
                if len(s) == 1:
                    self.label.setText('')
                    self.label_2.setText('')
                    self.label_3.setText('')                    
                    
                if s[-2] in 'snng':
                    print(s)
                    if len(s) > 4 and s[-5] in 'a' :
                        s = s[:-5]
                        print(1)
                    else:
                        s = s[:-4]
                        print(2)
                else:
                    s = s[:-1]
                    print(3)
                self.label.setText(s)
                self.label_2.setText(s)
                self.label_3.setText(s)
                

            except:
                #self.label_3.setText('ERROR')
                pass
                
        if event.text() in '1234567890)(*/+-//%**.':
            n = event.text()
            s = self.label.text()
            self.label.setText(s + n)
            self.label_3.setText(s + n) 
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
                print(2)
            
            
        if event.text() == 's' or event.text() == 'S':
            if event.text() == 's':
                n = 'sin('
            else:
                n='asin('
            s = self.label.text()
            self.label.setText(s + n)
            self.label_3.setText(s + n) 
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
        
        
        if event.text() == 'c' or event.text() == 'C':
            if event.text() == 'c':
                n = 'cos('
            else:
                n='acos('
            s = self.label.text()
            self.label.setText(s + n)
            self.label_3.setText(s + n) 
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
                
        
        if event.text() == 't' or event.text() == 'T':
            if event.text() == 't':
                n = 'tan('
            else:
                n='atan('
            s = self.label.text()
            self.label.setText(s + n)
            self.label_3.setText(s + n) 
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
                
        if event.text() == 'l':
            n = 'log('
            s = self.label.text()
            self.label.setText(s + n)
            self.label_3.setText(s + n) 
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
 
                
        
            
        
            
            
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())