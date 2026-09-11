import socket
import threading
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST= '192.168.22.204'
PORT= 5000
our_drivetrain_broke_again=0
Soncket.connect((HOST,PORT))
name=input("Name?")
Soncket.send(name.encode("utf-8"))
def Pennyworth():
    Soncket.settimeout(0.5)
    while True:
        if our_drivetrain_broke_again>0:
            break
        try:
            client_list=Soncket.recv(1024)
        except socket.timeout:
            continue
        if not client_list:
            break
        names=[client_list.decode('utf-8')]
        print("List of current users:", names, end="\r", flush=True)
        #print("\033[A\033[2K","List of current users:", names, end="", flush=True)
        print("recieved")
    message=input("")
    Soncket.send(message.encode("utf-8"))
    while True:
        data=(Soncket.recv(1024).decode('utf-8'))
        print(data)
        if not data:
            break
    
thread=threading.Thread(target=Pennyworth)
thread.start()      
print("who would u like to talk too?")
connection=input("")
Soncket.send(connection.encode('utf-8'))
our_drivetrain_broke_again=1
while True:
    message=input("")
    Soncket.send(message.encode("utf-8"))


    
    


