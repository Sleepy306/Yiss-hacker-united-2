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

try:
    Soncket.connect((HOST,PORT))
except:
    GUI.QMessageBox.warning(None, "Connection Error", f"Unable to connect to server\nIP: {HOST}\nPORT: {PORT}")
    sys.exit(f"ERROR: Host not found IP: {HOST} PORT: {PORT}")

if useGui:
    name = guiHandler.NameInputPopup()
else:
    name=input("Name?")#ask for user name 
Soncket.send(name.encode("utf-8"))

while True:
    if useGui:
        method = guiHandler.ChatSelect()
    else:
        method=input("Group chat or DM?(GC or DM)(exact wording pls))")

    if method=="GC":
        Soncket.sendall("2".encode('utf-8'))
        break
    elif method=="DM":
        Soncket.sendall("1".encode('utf-8'))
        break
    else:
        print("invalid method, pelase type in the correct one")
recieve= threading.Event()


class Pennyworth(GUI.QThread):
    listUsers = GUI.pyqtSignal(list, object)
    
    def __init__(self):
        super().__init__()
        self.waitForInput = threading.Event()
        self.waitForInput.clear()
        self.selectedUser = None

    def Run(self):

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
        print(userList)
        self.listUsers.emit(userList, self)
        self.waitForInput.wait() #Wait for process to finish
        Soncket.send(self.selectedUser.encode('utf-8'))
        recieve.set()

        while True: #recieve data from another user
            data=(Soncket.recv(1024).decode('utf-8'))
            print(data)
            if not data:
                break

    def ReceiveSelection(self, selection):
        self.selectedUser = selection
        self.waitForInput.set() #Unpause

class Albert_Tesla(GUI.QThread):
    def Run(self):
        message=input("Members of the group chat?(seperate by comma)")
        Soncket.send(message.encode('utf-8'))
        while True:
            Sonion=Soncket.recv(1024).decode('utf-8')
            if "does not exist" in Sonion:
                message=input("Invalids members, make sure they exist:")
                Soncket.send(message.encode('utf-8'))
            else:
                break
        recieve.set()
        while True:
            data=(Soncket.recv(1024).decode('utf-8'))
            print(data)
            if not data:
                break
        
if method=="DM":
    print("GUI: User Selected DM")
    thread=Pennyworth() #Single Chat
if method=="GC":
    print("GUI: User Selected GC")
    thread=Albert_Tesla() #Group Chat

thread.listUsers.connect(guiHandler.UserSelect)
thread.Run()
recieve.wait()

while True:
    message=input("Message:")#what user want to text to opposing client.
    Soncket.send(message.encode("utf-8"))#sent to server so that server could bring that to targeted user.

    
    


