from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit ,QPushButton ,QSpinBox , QRadioButton , QLabel
from PyQt5 import uic
import sys
import random
import pyperclip as pc

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load the ui file
        uic.loadUi("passwordgenerate.ui", self)

        # Definition of buttons
        self.spin = self.findChild(QSpinBox, "spinBox")
        self.spin.setRange(8,64)
        self.line = self.findChild(QLineEdit,"lineEdit")
        self.generate = self.findChild(QPushButton,"pushButton_generate")
        self.radioButton_normal = self.findChild(QRadioButton,"radioButton_normal")
        self.radioButton_medium = self.findChild(QRadioButton,"radioButton_medium")
        self.radioButton_hard = self.findChild(QRadioButton,"radioButton_hard")
        self.copy = self.findChild(QPushButton,"pushButton_copy")
        self.l_copy = self.findChild(QLabel,"label_copy")

        # By clicking the generate button, you will be connected to the function of creating a password
        self.generate.clicked.connect(self.generator)
        # Copy button
        self.copy.clicked.connect(self.copying)
        # Police Holder line edit
        self.line.setText("Your New Password")

        # set medium button for default
        self.radioButton_medium.setChecked(True)

        # show the app
        self.show()

    # definition copynig
    def copying(self):
        a1 = self.line.text()
        pc.copy(a1)
        a2 = pc.paste()
        self.l_copy.setText("Password Copied")


    # definition generator
    def generator(self):
        numbers = "0123456789"
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        symbol = "!@#$%^&*()>_+"
        Ambiguous = "[]{}|\/<>~"',:'

        if self.radioButton_normal.isChecked():
            string = numbers + lower + symbol + lower
            len = self.spin.value()
            password = "".join(random.sample(string,len))

            self.line.setText(str(password))

        if self.radioButton_medium.isChecked():
            string = numbers + lower + symbol + upper
            len = self.spin.value()
            password = "".join(random.sample(string,len))

            self.line.setText(str(password))

        if self.radioButton_hard.isChecked():
            string = numbers + lower + symbol + upper + Ambiguous
            len = self.spin.value()
            password = "".join(random.sample(string,len))

            self.line.setText(str(password))

        self.l_copy.setText("")







# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()