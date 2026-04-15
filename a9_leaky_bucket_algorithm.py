bucket_size = int(input("Enter bucket size: "))
output_rate = int(input("Enter output rate: "))
n = int(input("Enter number of incoming packets: "))

current_bucket_content = 0

for i in range(n):
    packet_size = int(input(f"Enter size of packet {i+1}: "))
    
    if packet_size + current_bucket_content <= bucket_size:
        current_bucket_content += packet_size
        print(f"Packet accepted. Current bucket: {current_bucket_content}")
    else:
        print("Bucket overflow! Packet discarded.")
    
    current_bucket_content -= output_rate
    if current_bucket_content < 0:
        current_bucket_content = 0
    
    print(f"After leaking, bucket contains: {current_bucket_content}")