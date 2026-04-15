import socket

c = socket.socket()
c.connect(('localhost', 12345))

c.send("Hello from Client".encode())
reply = c.recv(1024).decode()
print("Server says:", reply)

c.close()