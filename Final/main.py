import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import final

pathfile=""
description=""
tags=[]
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Facebook Spammer'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.textbox1=""
        self.textbox2=""
        self.pathfile=""
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Promote.')

        self.textbox1 = QLineEdit(self)#enter description
        self.textbox1.move(120, 220)
        self.textbox1.resize(480,30)

        self.textbox2 = QLineEdit(self)#enter description
        self.textbox2.move(120, 120)
        self.textbox2.resize(480,30)


        button1 = QPushButton('Description', self)#for description
        button1.setToolTip('')
        button1.move(15,120)
        
        button1 = QPushButton('Tags', self)#for description
        button1.setToolTip('')
        button1.move(15,220)
        
        
        button2 = QPushButton('Choose File', self)#for browse
        button2.setToolTip('Click to choose your file to be uploaded')
        button2.move(275,305)
        button2.clicked.connect(self.get_files)

        
        button3 = QPushButton('UPLOAD', self)#for upload
        button3.setToolTip('Click to post your file')
        button3.move(275,405)
        button3.clicked.connect(self.on_click)

        

        self.show()
    @pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        
        self.pathfile=fileName

            
    def get_files(self):
        self.openFileNameDialog()

        
    def on_click(self):
        textboxValue = self.textbox1.text()
        tags=textboxValue
        description=self.textbox2.text()
        f = open("myfile.txt", "w+")
        f.write("%s\n"%description)
        f.write("%s\n"%self.pathfile)
        f.write("%s\n"%tags)
        f.close()
        final.MAIN()


     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.initUI()