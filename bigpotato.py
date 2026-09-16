import socket
import threading
HOST= '192.168.22.204'
PORT= 5000
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Soncket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Soncket.bind((HOST,PORT))
Soncket.listen(67)
eggies={}#dictionary of users names(key) and their conection(value)
bigger_eggies={}
group_number=0
print('Server is listening')
def Alfred(con, addr):#thread that connect clients to 1-1 chat.
    while True:
         name_output = (con.recv(1024).decode('utf-8'))#input who u want to talk with
         if name_output not in eggies:
               con.send("invalid user".encode('utf-8'))
         else:#if name is on the list, connect that person with wanted user, if not tell them to retype user
               to_who=eggies[name_output]
               con.send(("connected to "+ name_output).encode('utf-8'))
               break
    while True:#recieves text messages and sent to targeted client.
         data=con.recv(1024)
         if not data:
             print("not data recieved")
             con.close()
             break
         message=data
         to_who.send(message)
def Heisenburg(con,addr):
    global group_number
    sleepies=[]
    while True:
         Members=(con.recv(1024).decode('utf-8'))
         Members=Members.split(",")
         for users in Members:
             if users not in eggies.keys():
                 con.sendall((users+"does not exist").encode('utf-8'))
         if all(users in eggies for users in Members):
              con.sendall(("you're good to go").encode('utf-8'))
              group_number=group_number+1
              for users in Members:
                  sleepies.append(eggies[users])
              group="Group"+str(group_number)
              bigger_eggies[group]=sleepies
              break
    while True:
        message=con.recv(1024)
        if not message:
            con.close()
            break
        for users in Members:
            if con==eggies[users]:
                continue
            eggies[users].sendall(message)
         
try:
     while True: #main thread, recieve each client's name and starts Alfred thread.
         con, addr= Soncket.accept() 
         name=con.recv(1024).decode('utf-8')
         eggies[name] = con
         method=con.recv(1024).decode('utf-8')
         print("method recieve",repr(method))
         print("Connected", name, eggies[name])
         if method=="1":
            thread=threading.Thread(target=Alfred, args=(con,addr))
            print("method recieve", repr(method))
         if method=="2":
             thread=threading.Thread(target=Heisenburg,args=(con,addr))
             print("method recieve", repr(method)) 
         thread.start()
finally:
    con.close()
    Soncket.close()
     
     


