#UI files

import sys, threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QInputDialog, QDialog, QComboBox, QListWidget, QListView
from PyQt5.QtCore import pyqtSignal, QThread, QStringListModel

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat")
        self.resize(400, 400)

        self.submittingEvent = threading.Event()
        self.submittingEvent.clear()

        self.chatHistory = ["History Begins Here"]

        self.chatHistoryDisplay = QListView(self)
        self.inputField = QLineEdit(self)
        self.submitButton = QPushButton("Send", self)

        self.model = QStringListModel()
        self.model.setStringList(self.chatHistory)
        self.chatHistoryDisplay.setModel(self.model)

        layout = QVBoxLayout(self)
        layout.addWidget(self.chatHistoryDisplay)
        layout.addWidget(self.inputField)
        layout.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.Submit)
        self.inputField.returnPressed.connect(self.Submit)

    def UpdateChatHistory(self, newLine):
        print(newLine)
        addedLines = self.model.stringList()
        addedLines.append(newLine)
        self.model.setStringList(addedLines)

    def Submit(self):
        self.submittingEvent.set()

    def GetMessageInBox(self):
        message = self.inputField.text()
        self.inputField.setText("")

        self.submittingEvent.clear()

        if not message:
            return "..."
        return message

class UserList(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list = list()

        self.setWindowTitle("DM Select")
        self.resize(300, 200)

        self.layout = QVBoxLayout(self)
        self.label = QLabel("Select User you'd like to connect to:")
        self.inputBox = QComboBox(self)
        self.reloadButton = QPushButton("Reload", self)
        self.submit = QPushButton("Ok", self)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.inputBox)
        self.layout.addWidget(self.reloadButton)
        self.layout.addWidget(self.submit)

        self.reloadButton.clicked.connect(self.ReloadList)
        self.submit.clicked.connect(self.accept)

    def ReloadList(self):
        self.inputBox.clear()
        self.inputBox.addItems(self.list)

    def UpdateList(self, newListData):
        self.list = newListData

    def GetSubmittedData(self):
        return self.inputBox.currentText()
class GUI:
    def __init__(self):
        self.app: QApplication = None
        self.window: QWidget = None
        self.processing = False

    def InitializeGUI(self):
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Yiss Hackers United Networking")

        self.window = ChatWindow()
        self.window.show()

        self.selectDialog = UserList()

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
        print("GUI: Name popup")
        #self.window.setLayout(self.namelayout)
        #elf.window.show()
        name = None
        while not name:
            name, ok = QInputDialog.getText(None, "Enter Name", "Enter your name:")

            if not ok:
                sys.exit()

            if name:
                QMessageBox.information(None, "Name set", f"Set name to: {name}")
            else:
                QMessageBox.warning(None, "Name not set.", "Please re-enter name")

        return name

    def ChatSelect(self):
        print("GUI: Chat Mode Select")
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

    def DMUserSelect(self, threadObject):
        print("GUI: User DM select")
#        user, ok = QInputDialog.getItem(None, "DM Select", "Select user",users, 0, False)

#        if not ok:
#            sys.exit()
#           threadObject.Stop()
        self.processing = True

        self.selectDialog.ReloadList()
        result = self.selectDialog.exec_()

        user = self.selectDialog.GetSubmittedData()

        print(user)
        threadObject.ReceiveSelection(user)

        self.processing = False

#    def CloseAppSetup(self):
#        sys.exit(self.app.exec())
#        return


#Test code
if __name__ == "__main__":

    guiHandler = GUI()
    guiHandler.InitializeGUI()

    sys.exit(guiHandler.app.exec())

    #name = guiHandler.NameInputPopup()

    #connection = guiHandler.ChatSelect()

    #print(name)
    #print(connection)