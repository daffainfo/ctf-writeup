import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

plaintext = input("text to encrypt:\n")
ciphertext = ""

key = [random.randint(1, len(alphabet)) for _ in range(len("vikeCTF"))]
print("key:", *key)

for i, c in enumerate(plaintext):
	if not c.isalpha():
		ciphertext += c
		continue

	offset = alphabet.find(c.lower())
	rotation = key[i % len(key)]

	result = alphabet[(offset + rotation) % len(alphabet)]
	if c.islower():
		ciphertext += result
	else:
		ciphertext += result.upper()

print("ciphertext:")
print(ciphertext)