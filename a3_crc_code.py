def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*len(divisor), tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*len(divisor), tmp)

    return tmp


def compute_crc(data, generator):
    l = len(generator)
    appended_data = data + '0'*(l-1)
    remainder = mod2div(appended_data, generator)
    codeword = data + remainder
    return remainder, codeword


# -------- Sender Side --------
data = input("Enter binary data: ")

print("\nChoose CRC Type:")
print("1. CRC-12")
print("2. CRC-16")
print("3. CRC-CCIP (CRC-CCITT)")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    generator = "1100000001111"
elif choice == 2:
    generator = "11000000000000101"
elif choice == 3:
    generator = "10001000000100001"
else:
    print("Invalid choice")
    exit()

remainder, codeword = compute_crc(data, generator)

print("\nGenerator Polynomial:", generator)
print("CRC Remainder:", remainder)
print("Final Codeword:", codeword)


received_data = input("\nEnter received data to check error: ")

check_remainder = mod2div(received_data, generator)

print("Remainder after checking:", check_remainder)

if '1' in check_remainder:
    print("Error detected in received data!")
else:
    print("No error detected. Data is correct.")
    
