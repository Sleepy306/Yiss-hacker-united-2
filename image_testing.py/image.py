
import socket
import threading
import pickle
HOST= "localhost"#'192.168.22.204'
PORT= 5000
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Soncket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Soncket.bind((HOST,PORT))
Soncket.listen(67)
print("server is listening")
path_file=input("image path file:")
con, addr= Soncket.accept()
#path_file=con.recv(1024).decode('utf-8')
skibidi_open_now=open(path_file,'rb')
wallahi=skibidi_open_now.read()
bytes=len(wallahi).to_bytes(8,'big')
print(len(wallahi))
con.sendall(bytes)
con.sendall(wallahi)
skibidi_open_now.close()
con.close()
