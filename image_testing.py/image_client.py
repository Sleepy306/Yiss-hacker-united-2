#/usr/bin/python3 "/Users/student/Yiss hacker united/image_testing.py/image_client.py"
import socket
import threading
import pickle
import subprocess
HOST= "localhost"#'192.168.22.204'
PORT= 5000
Soncket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Soncket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Soncket.connect((HOST, PORT))
Vmax=0
data=b''
Size = int.from_bytes(Soncket.recv(8), 'big')
while not Vmax==Size:
    chunk=Soncket.recv(Size)
    data+=chunk
    Vmax+=len(chunk)
file_name=input("name the file")
file_name+=".jpg"
file=open(file_name,'wb')
file.write(data)
print("Received:", len(data), "bytes")
print("Expected:", Size, "bytes")
file.close()
subprocess.run(["open", file_name])
