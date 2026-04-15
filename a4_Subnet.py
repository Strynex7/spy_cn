ip_addr = input("Enter IP (e.g. 192.168.1.0): ")
num_subnets = int(input("How many subnets? "))

import math
borrowed_bits = math.ceil(math.log2(num_subnets))
hosts_per_subnet = 256 // (2**borrowed_bits)

mask = 256 - hosts_per_subnet
print(f"Subnet Mask: 255.255.255.{mask}")

prefix = ip_addr.rsplit('.', 1)[0]
for i in range(num_subnets):
    low = i * hosts_per_subnet
    high = low + hosts_per_subnet - 1
    print(f"Subnet {i+1}: {prefix}.{low} to {prefix}.{high}")