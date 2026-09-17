#UI files

import sys, threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QInputDialog, QDialog
from PyQt5.QtCore import pyqtSignal, QThread

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

    def NameInputPopup(self):
        #self.window.setLayout(self.namelayout)
        #elf.window.show()
        name = None
        while not name:
            name, ok = QInputDialog.getText(None, "Enter Name", "Enter your name:")

            if not ok:
                QMessageBox.warning(None, "No", "That is not an option")
                continue

            if name:
                QMessageBox.information(None, "Name set", f"Set name to: {name}")
            else:
                QMessageBox.warning(None, "Name not set.", "Please re-enter name")

        return name

    def ChatSelect(self):
        groupChat = None
        options = ["Single Chat", "Group Chat"]
        
        while True:
            groupChat, ok = QInputDialog.getItem(None, "Chat Mode", "Select chat mode:" ,options, 0, False)

            if not ok:
                QMessageBox.warning(None, "No", "That is not an option")
                continue

            if groupChat == "Single Chat":
                return "DM"
            elif groupChat == "Group Chat":
                return "GC"

    def UserSelect(self, users, threadObject):
        user, ok = QInputDialog.getItem(None, "DM Select", "Select user",users, 0, False)

        if not ok:
            QMessageBox.warning(None, "No", "That is not an option")
            pass

        threadObject.ReceiveSelection(user)
        #return user

#    def CloseAppSetup(self):
#        sys.exit(self.app.exec())
#        return


#Test code
#guiHandler = GUI()
#guiHandler.InitializeGUI()

#guiHandler.window.setLayout(guiHandler.namelayout)
#guiHandler.window.show()

#name = guiHandler.NameInputPopup()

#connection = guiHandler.ChatSelect()

#print(name)
#print(connection)