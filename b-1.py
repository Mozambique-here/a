import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,  QMessageBox, QLabel
from PyQt5 import uic

from PyQt5.QtGui import QIcon
 
from math import *
from time import *

t1 = 0
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui',self)
        
        self.pushButton7.pressed.connect(self.push)
        
        self.pushButton7.released.connect(self.run)
        
        self.pushButton2.released.connect(self.run)
        self.pushButton2.pressed.connect(self.push)
        self.pushButton3.released.connect(self.run)
        self.pushButton3.pressed.connect(self.push)
        self.pushButton4.released.connect(self.run)
        self.pushButton4.pressed.connect(self.push)
        self.pushButton5.released.connect(self.run)
        self.pushButton5.pressed.connect(self.push)
        self.pushButton6.released.connect(self.run)
        self.pushButton6.pressed.connect(self.push)
        self.pushButton1.released.connect(self.run)
        self.pushButton1.pressed.connect(self.push)
        self.pushButton8.pressed.connect(self.push)
        self.pushButton8.released.connect(self.run)
        self.pushButton9.released.connect(self.run)
        self.pushButton9.pressed.connect(self.push)
        self.pushButton0.clicked.connect(self.run)
        self.pushButtonc.released.connect(self.dell)
        self.pushButtonc.pressed.connect(self.push)
        self.pushButtond.clicked.connect(self.run)
        self.pushButtonm.clicked.connect(self.run)
        self.pushButtona.clicked.connect(self.run)
        self.pushButtoneq.clicked.connect(self.eq)
        self.pushButtonid.clicked.connect(self.run)
        self.pushButtonmod.clicked.connect(self.run)
        self.pushButton10.clicked.connect(self.run)
        self.pushButtons.clicked.connect(self.run)
        
    def run(self):
        n = str(self.sender().text())
        
        

        if n[0] == '&':
            n = n[1]
        print(n)
        s = self.label_3.text()
        global t1
       
        if time() - t1 > 0.3:
        	if n == '7':
        		n = 'sin('
        	if n == '8':
        		n = 'cos('
        	if n == '9':
        		n = 'tan('
        	if n == '4':
        		n = 'asin('
        	if n == '5':
        		n = 'acos('
        	if n == '6':
        		n = 'atan('
        	if  n == '1':
        		n = '('
        	if n == '3':
        		n = 'log('
        	if n == '2':
        		n = ')'
   
        self.label_3.setText(s + n)
        self.label.setText(s + n)
        
        try:
            self.label_2.setText(str(round(eval(s+n), 10)))
        except:
            self.label_2.setText('')
            
    def push(self):
    	#self.label_2.setText('gg')
    	global t1
    	t1 = time()
    	#self.label_2.setText('gggggg')
        

                
    def dell(self):
    	s = self.label.text()
    	if time() - t1 > 0.5:
    		self.label_3.setText('')
    		self.label_2.setText('')
    		self.label.setText('')
    	else:
            try:
                if len(s) == 1:
                    self.label.setText('')
                    self.label_2.setText('')
                    self.label_3.setText('')                    
                    
                if s[-2] in 'snng':
                    if len(s) > 4 and s[-5] in 'a' :
                        s = s[:-5]
                    else:
                        s = s[:-4]
                else:
                    s = s[:-1]
                self.label.setText(s)
                try:
                    self.label_2.setText(str(round(eval(s), 10)))
                except:
                    self.label_2.setText('')
                self.label_3.setText(s)
            except:
                pass
        
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
                    if len(s) > 4 and s[-5] in 'a' :
                        s = s[:-5]
                    else:
                        s = s[:-4]
                else:
                    s = s[:-1]
                self.label.setText(s)
                try:
                    self.label_2.setText(str(round(eval(s), 10)))
                except:
                    self.label_2.setText('')
                self.label_3.setText(s)
            except:
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