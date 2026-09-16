#UI files

import sys, threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QInputDialog

class GUI:
    def __init__(self):
        self.app: QApplication = None
        self.window: QWidget = None

    def InitializeGUI(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setGeometry(100, 100, 800, 400)

        #Define name input window
        #self.namelayout = QVBoxLayout()

        #self.window.setWindowTitle("Yiss Hacker Network")

        #self.inputTextField = QLineEdit(self.window)
        #self.inputTextField.setPlaceholderText("Enter name...")
        #self.namelayout.addWidget(self.inputTextField)

        #self.submitButton = QPushButton("Submit", self.window)
        #self.submitButton.clicked.connect(self.ReadName)
        #self.namelayout.addWidget(self.submitButton)
        #----------------------------------------------------

    def ReadName(self):
        userInput = self.inputTextField.text().strip()
        if userInput:
            QMessageBox.information(self.window, "Name set", f"Set name to: {userInput}")
            return userInput
        else:
            QMessageBox.warning(self.window, "Name not set.", "Please reenter name")
            return

    def NameInputPopup(self):
        #self.window.setLayout(self.namelayout)
        #elf.window.show()
        name = None
        while not name:
            name, ok = QInputDialog.getText(None, "Enter Name", "Enter your name:")
            if name:
                QMessageBox.information(self.window, "Name set", f"Set name to: {name}")
            else:
                QMessageBox.warning(self.window, "Name not set.", "Please re-enter name")

        return name


    def CloseAppSetup(self):
        sys.exit(self.app.exec())
        return

#Test code
guiHandler = GUI()
guiHandler.InitializeGUI()

#guiHandler.window.setLayout(guiHandler.namelayout)
#guiHandler.window.show()

name = guiHandler.NameInputPopup()

print(name)
