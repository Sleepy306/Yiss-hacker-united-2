#/usr/bin/python3 "/Users/student/Yiss hacker united/small potato.py"
import socket
import threading
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST= '192.168.22.204'
PORT= 5000
our_drivetrain_broke_again=False
Soncket.connect((HOST,PORT))
name=input("Name?")#ask for user name 
Soncket.send(name.encode("utf-8"))
while True:
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
def Pennyworth():
    message=input("Who would u like to talk to:")
    while True:
        #who clients want to talk to
        Soncket.send(message.encode('utf-8'))
        to_who=(Soncket.recv(1024).decode('utf-8'))
        if to_who == "invalid user":
            message=input("Does not exist, type again:")
        else:# if invalid user, repeat the loop until valid user is type in
            break
    recieve.set()
    while True: #recieve data from another user
        data=(Soncket.recv(1024).decode('utf-8'))
        print(data)
        if not data:
            break
def Albert_Tesla():
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
    thread=threading.Thread(target=Pennyworth)
if method=="GC":
    thread=threading.Thread(target=Albert_Tesla)
thread.start()  
recieve.wait()
while True:


    
    


