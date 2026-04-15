"""
===============================================================================
                       NETWORKING LAB: VIVA QUESTIONS
===============================================================================

1. LEAKY BUCKET ALGORITHM
Q1: Main purpose? Traffic shaping and congestion control.
Q2: Full bucket? Packets are discarded (Overflow).
Q3: Leak rate? Represents the fixed bandwidth/transmission rate.
Q4: vs Token Bucket? Leaky is fixed rate; Token allows bursty traffic.
Q5: Storage variable? Represents the router's buffer memory.

2. DISTANCE VECTOR ROUTING (DVR)
Q1: Algorithm? Bellman-Ford.
Q2: What is shared? Entire routing table with immediate neighbors.
Q3: Count to Infinity? A routing loop where distances increase indefinitely.
Q4: Unreachable node? Represented by infinity (float('inf')).
Q5: Real protocol? RIP (Routing Information Protocol).

3. CRC (CYCLIC REDUNDANCY CHECK)
Q1: Type? Polynomial-based error detection using binary division.
Q2: Why zeros? To make space for the remainder bits.
Q3: Codeword? The original data bits + the calculated remainder.
Q4: Non-zero remainder? Indicates the data was corrupted.
Q5: Operation? XOR (Exclusive OR).

4. SUBNETTING
Q1: Subnet Mask? 32-bit number distinguishing Network ID and Host ID.
Q2: CIDR? Notation like /24 for network bits.
Q3: Hosts per subnet? Formula: 2^h - 2.
Q4: Why subnet? Reduce broadcast traffic and improve security.
Q5: 2 bits borrowed? Creates 2^2 = 4 subnets.

5. TCP CLIENT-SERVER
Q1: Socket? Endpoint defined by an IP and a Port number.
Q2: TCP? Connection-oriented protocol using a 3-way handshake.
Q3: bind()? Assigns a specific IP and Port to the server socket.
Q4: listen vs accept? Listen waits; Accept connects to the client.
Q5: encode/decode? Converts between Strings and Bytes for transmission.

===============================================================================
"""

import math
import socket

# --- 1. LEAKY BUCKET ---
def leaky_bucket():
    size = int(input("Bucket size: "))
    rate = int(input("Output rate: "))
    n = int(input("Packets: "))
    storage = 0
    for i in range(n):
        p = int(input(f"Packet {i+1} size: "))
        if p + storage <= size:
            storage += p
            print(f"Accepted. Bucket: {storage}")
        else:
            print("Dropped (Overflow)")
        storage -= rate
        if storage < 0: storage = 0
        print(f"After leak: {storage}")

# --- 2. DISTANCE VECTOR ROUTING ---
def distance_vector():
    n = int(input("Nodes: "))
    matrix = []
    for i in range(n):
        row = [float('inf') if x=='inf' else int(x) for x in input(f"Row {i+1}: ").split()]
        matrix.append(row)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    for row in matrix: print(row)

# --- 3. CRC ---
def crc_check():
    data = input("Binary Data: ")
    poly = input("Polynomial (e.g. 1101): ")
    div = list(data + '0'*(len(poly)-1))
    p = list(poly)
    for i in range(len(div)-len(p)+1):
        if div[i] == '1':
            for j in range(len(p)):
                div[i+j] = str(int(div[i+j]) ^ int(p[j]))
    rem = "".join(div[-(len(p)-1):])
    print(f"Remainder: {rem}\nCodeword: {data+rem}")

# --- 4. SUBNETTING ---
def subnetting():
    ip = input("IP: ")
    n = int(input("Subnets: "))
    bits = math.ceil(math.log2(n))
    hosts = 256 // (2**bits)
    print(f"Subnet Mask: 255.255.255.{256-hosts}")
    prefix = ip.rsplit('.', 1)[0]
    for i in range(n):
        print(f"Subnet {i+1}: {prefix}.{i*hosts} to {prefix}.{(i+1)*hosts-1}")

# --- 5. TCP SERVER ---
def tcp_server():
    s = socket.socket()
    s.bind(('localhost', 8080))
    s.listen(1)
    print("Waiting...")
    conn, addr = s.accept()
    print("Client says:", conn.recv(1024).decode())
    conn.send("Hello".encode())
    conn.close()

# TO RUN AN ASSIGNMENT, REMOVE THE '#' FROM THE LINE BELOW:
# leaky_bucket()
# distance_vector()
# crc_check()
# subnetting()
# tcp_server()