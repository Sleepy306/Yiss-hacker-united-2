#/usr/bin/python3 "/Users/student/Yiss hacker united/small potato.py"
import socket
import threading
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST= 'localhost'
PORT= 5000
our_drivetrain_broke_again=False
Soncket.connect((HOST,PORT))
name=input("Name?")#ask for user name 
Soncket.send(name.encode("utf-8"))
recieve= threading.Event()
def Pennyworth():
    while True:
        message=input("Who would u like to talk to:")#who clients want to talk to
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
    
thread=threading.Thread(target=Pennyworth)
thread.start()  
recieve.wait()
while True:
    message=input("Message:")#what user want to text to opposing client.
    Soncket.send(message.encode("utf-8"))#sent to server so that server could bring that to targeted user.


    
    


