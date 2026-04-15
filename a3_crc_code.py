def crc(data, poly):
    data = list(data + '0' * (len(poly) - 1))
    poly = list(poly)
    
    for i in range(len(data) - len(poly) + 1):
        if data[i] == '1':
            for j in range(len(poly)):
                data[i + j] = str(int(data[i + j]) ^ int(poly[j]))
                
    return "".join(data[-(len(poly)-1):])

msg = input("Enter binary data: ")
print("1. CRC-12 | 2. CRC-16 | 3. CRC-CCIP")
choice = input("Select (1-3): ")

polys = {"1": "1100000001111", "2": "11000000000000101", "3": "10001000000100001"}
p = polys[choice]

check_value = crc(msg, p)
print("CRC Remainder:", check_value)
print("Final Codeword:", msg + check_value)