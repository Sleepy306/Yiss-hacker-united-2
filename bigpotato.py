import socket
import threading
HOST= '192.168.22.204'
PORT= 5000
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Soncket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Soncket.bind((HOST,PORT))
Soncket.listen(67)
eggies={}
print('Server is listening')
def Alfred(con, addr):
    keys_string = ", ".join(eggies.keys())
    for client_con in eggies.values():
         client_con.send(keys_string.encode("utf-8"))
    to_who=(con.recv(1024).decode('utf-8'))
    while True:
         data=con.recv(1024)
         if not data:
             print("not data recieved")
             con.close()
             break
         message=data
         eggies[to_who].send(message)
        
try:
     while True: 
         con, addr= Soncket.accept() 
         data=con.recv(1024)
         name=data.decode("utf-8")
         eggies[name] = con
         print("Connected", name, eggies[name])
         thread=threading.Thread(target=Alfred, args=(con,addr))
         thread.start()
finally:
     Soncket.close()
     
     


