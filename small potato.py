#/usr/bin/python3 "/Users/student/Yiss hacker united/small potato.py"
import sys
import socket
import threading
import pickle
import GUI
useGui = True
guiHandler = GUI.GUI()
guiHandler.InitializeGUI()

Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST= "localhost"#'192.168.22.204'
PORT= 5000

our_drivetrain_broke_again=False

def GetNewListData():  
    listUpdating.clear()
    while guiHandler.processing:
        Soncket.send("reloadls".encode('utf-8'))
        userList = pickle.loads(Soncket.recv(1024))
        userList.remove(name)
        guiHandler.selectDialog.UpdateList(userList)
    listUpdating.set()

userListReloadThread = threading.Thread(target=GetNewListData)

listUpdating = threading.Event()

readyToReceive = threading.Event()
readyToReceive.clear()

disconnectEvent = threading.Event()
def Disconnect():
    Soncket.close()
    disconnectEvent.set()
    sys.exit()

class Pennyworth(GUI.QThread):
    
    listUsers = GUI.pyqtSignal(object)
    
    def __init__(self):
        super().__init__()
        self.waitForInput = threading.Event()
        
        self.waitForInput.clear()
        self.selectedUser = None


    def Run(self):
        print("Thread pennyworth started")
#        message=input("Who would u like to talk to:")
#       while True:
#           #who clients want to talk to
#            Soncket.send(message.encode('utf-8'))
#            to_who=(Soncket.recv(1024).decode('utf-8'))
#            if to_who == "invalid user":
#                message=input("Does not exist, type again:")
#           else:# if invalid user, repeat the loop until valid user is type in
#               break
#       recieve.set()

        userList = pickle.loads(Soncket.recv(1024))

        guiHandler.processing = True
        userListReloadThread.start()

        self.listUsers.emit(self)
        
        self.waitForInput.wait()

        Soncket.send(self.selectedUser.encode('utf-8'))

        readyToReceive.set()

        listUpdating.wait()

        print("Ready to chat")
        receiveThread.start()

        guiHandler.app.exec()
        Disconnect()

    def ReceiveSelection(self, selection):
        print(f"GUI: Selection received from user: {selection}")
        self.selectedUser = selection
        self.waitForInput.set() #Unpause

    def Stop(self):
        self.quit()

class Albert_Tesla(GUI.QThread):

    def __init__(self):
        super.__init__()

        self.readyToReceive = threading.Event()
        self.readyToReceive.clear()

    def Run(self):
        print("Thread albert tesla started")
        message=input("Members of the group chat?(seperate by comma)")
        Soncket.send(message.encode('utf-8'))
        while True:
            Sonion=Soncket.recv(1024).decode('utf-8')
            if "does not exist" in Sonion:
                message=input("Invalids members, make sure they exist:")
                Soncket.send(message.encode('utf-8'))
            else:
                break
        self.readyToReceive.set()
        
        while True:
            data=(Soncket.recv(1024).decode('utf-8'))
            print(data)
            if not data:
                break

def sendDataLoop():
    print("waiting")
    readyToReceive.wait()

    print("send loop")
    while not disconnectEvent.is_set():
        #message=input("Message:")
        guiHandler.window.submittingEvent.wait()
        message = guiHandler.window.GetMessageInBox()#what user want to text to opposing client.

        message = name + ": "+ message

        Soncket.send(message.encode("utf-8"))#sent to server so that server could bring that to targeted user.
        guiHandler.window.UpdateChatHistory(message)
sendThread = threading.Thread(target=sendDataLoop)

def receiveDataLoop():
    while not disconnectEvent.is_set(): #recieve data from another user
        data=(Soncket.recv(1024).decode('utf-8'))
        print(data)
        guiHandler.window.UpdateChatHistory(data)
        if not data:
            break
receiveThread = threading.Thread(target=receiveDataLoop)

#---------------------------------------------------------------------------------------------------------------------------------
try:
    Soncket.connect((HOST,PORT))
except:
    GUI.QMessageBox.warning(None, "Connection Error", f"Unable to connect to server\nIP: {HOST}\nPORT: {PORT}")
    sys.exit(f"ERROR: Host not found IP: {HOST} PORT: {PORT}")

name = guiHandler.NameInputPopup()

Soncket.send(name.encode("utf-8"))

method = guiHandler.ChatSelect()

if method=="DM": #Single Chat
    print("GUI: User Selected DM")
    Soncket.sendall("1".encode('utf-8'))
    mainThread=Pennyworth()

elif method=="GC": #Group Chat
    print("GUI: User Selected GC")
    Soncket.sendall("2".encode('utf-8'))
    mainThread=Albert_Tesla()

sendThread.start() #This thread wits before the acctuall function is run

mainThread.listUsers.connect(guiHandler.DMUserSelect)
mainThread.Run()