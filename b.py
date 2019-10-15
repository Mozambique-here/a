import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,  QMessageBox, QLabel
from PyQt5 import uic
from math import *
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui',self)

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
        
        try:
            self.label_2.setText(str(round(eval(s+n), 10)))
        except:
            self.label_2.setText('')
        

                
        
    def dell(self):
        self.label.setText('')
        self.label_2.setText('')
        
    def eq(self):
        s = str(self.label.text())
        try:
            self.label.setText(str(round(eval(s), 10)))
            self.label_2.setText(str(round(eval(s), 10)))
        except:
            self.label.setText('ERROR')
    
    def keyPressEvent(self, event):

        if event.text() == '\r':
            s = str(self.label.text())
            try:
                if type(eval(s)) == int:
                    self.label.setText(str(round(eval(s), 10)))
                    print(1)
            except:
                self.label.setText('ERROR')
                
            
        if event.text() == '':
            s = str(self.label.text())
            try:
                self.label.setText(s[:-1])
                self.label_2.setText(s[:-1])

            except:
                self.label.setText('ERROR')
                
        if event.text() in '1234567890)(*/+-//%**.':
            n = event.text()
            s = self.label.text()
            self.label.setText(s + n)        
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
                print(2)
            
        #if event.text() not in '1234567890)(*/+-//%**.\r':
            #self.label_2.setText('')
            #self.label.setText('')
                
        #if event.key() == 92:
            #self.label.setText('')
            #try:
                #self.label_2.setText(str(round(eval(s+n), 10)))
            #except:
                #self.label_2.setText('')
                
        #if event.key() == 93:
            #s = str(self.label.text())[:-1]
            #self.label.setText(s)
            #try:
                #self.label_2.setText(str(round(eval(s+n), 10)))
            #except:
                #self.label_2.setText('')
            
        if event.text() == 's':
            n = 'sin('
            s = self.label.text()
            self.label.setText(s + n)            
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
        
        
        if event.text() == 'c':
            n = 'cos('
            s = self.label.text()
            self.label.setText(s + n)            
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
                
        
        if event.text() == 't':
            n = 'tan('
            s = self.label.text()
            self.label.setText(s + n)            
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
                
        if event.text() == 'l':
            n = 'log('
            s = self.label.text()
            self.label.setText(s + n)            
            
            try:
                self.label_2.setText(str(round(eval(s+n), 10)))
            except:
                self.label_2.setText('')
 
                
        
            
        
            
            
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())