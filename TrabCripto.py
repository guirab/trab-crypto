

alice = open('alice29.txt', 'r')


alice_str = alice.read()
aliceBytes = bytes(alice_str, 'utf-8')

## Convert aliceBytes to bits and print
aliceBits = aliceBytes.to_bits()
print(aliceBits)

# # Unary code encoding
# N = aliceBytes
# A = []

# for i in range(N):
# 	A.append(1)
	
# A.append(0)

# B = [str(k) for k in A]

# C = "".join(B)

# print("Unary code for", N,
# 	'is', C)

