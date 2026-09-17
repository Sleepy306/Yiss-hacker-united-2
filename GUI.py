#UI files

import sys, threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QInputDialog, QDialog

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

            if not ok:
                break

            if name:
                QMessageBox.information(None, "Name set", f"Set name to: {name}")
            else:
                QMessageBox.warning(None, "Name not set.", "Please re-enter name")

        return name

    def ChatSelect(self):
        groupChat = False
        connectionName = None
        options = ["Single Chat", "Group Chat"]
        
        while not connectionName:
            groupChat, ok = QInputDialog.getItem(None, "Chat Mode", "Select chat mode:" ,options, 0, False)

            if not ok:
                break

            if groupChat == "Single Chat":
                connectionName, ok = QInputDialog.getText(None, "Single Chat", "Enter user you'd like to connect to:")
                if not connectionName:
                    if ok:
                        QMessageBox.warning(None, "Name not set.", "Please re-enter information")
                    pass
            elif groupChat == "Group Chat":
                connectionName, ok = QInputDialog.getText(None, "Group Chat", "Enter group chat you'd like to connect to:")
                if not connectionName:
                    if ok:
                        QMessageBox.warning(None, "Name not set.", "Please re-enter information")
                    pass

            if not ok:
                break
        
        return connectionName

#    def CloseAppSetup(self):
#        sys.exit(self.app.exec())
#        return

#Test code
guiHandler = GUI()
guiHandler.InitializeGUI()

#guiHandler.window.setLayout(guiHandler.namelayout)
#guiHandler.window.show()

name = guiHandler.NameInputPopup()

connection = guiHandler.ChatSelect()

print(name)
print(connection)