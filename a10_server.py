import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Server is waiting...")

conn, addr = s.accept()
msg = conn.recv(1024).decode()
print("Client says:", msg)

conn.send("Hello from Server".encode())
conn.close()