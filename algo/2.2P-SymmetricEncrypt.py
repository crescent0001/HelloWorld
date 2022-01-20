# ************************************************************************************
# This sample code to demonstrate AES encryption and decryption is extracted from
# https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/
# and
# https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-aes
# ************************************************************************************
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

# A safe place to store a key. Can be on a USB or even locally on the machine (not recommended unless it has been further encrypted)
KEY_LOCATION = "my_key.bin"

# Generate the key using get_random_bytes
##key = get_random_bytes(32) # 32 bytes * 8 = 256 bits (1 byte = 8 bits)
##print(key)

# Better way to generate the key using PBKDF2
# Note that PBKDF1 can only generate keys up to 160 bits
#
# A salt is random data that is used as an additional input
# to a one-way function that "hashes" data
salt_str = "abcde123"
salt_byte = bytes(salt_str, "utf-8") # convert string to bytes
password = "Password123"

#dkLen specifies length of key in bytes, 32 x 8 = 256 bits
key = PBKDF2(password, salt_byte, dkLen=32)

# Save the key to a file
file_out = open(KEY_LOCATION, "wb") # wb = write bytes
file_out.write(key)
file_out.close()

# Later on ... (assume we no longer have the key)
file_in = open(KEY_LOCATION, "rb") # Read bytes
key_from_file = file_in.read() # This key should be the same
file_in.close()

# Test key to confirm they have not een tampered with
if key == key_from_file:
    print("Key generated =", key)
    print("Key saved to file", KEY_LOCATION, "and verified successfully")
else:
    print("There is a problem with the key!")


#Encrypt
plaintext = input("Enter plaintext to be encrypted - ")
OUTPUT_FILE = "encrypted.bin"

cipher = AES.new(key, AES.MODE_EAX) # EAX mode using the same key
ciphered_data, tag = cipher.encrypt_and_digest(bytes(plaintext, "utf-8")) # Encrypt and digest to get the ciphered data and tag

file_out = open(OUTPUT_FILE, "wb")
file_out.write(cipher.nonce) # Write the nonce to the output file (will be required for decryption - fixed size)
file_out.write(tag) # Write the tag out after (will be required for decryption - fixed size)
file_out.write(ciphered_data)
file_out.close()

#Decrypt
INPUT_FILE = 'encrypted.bin' # Input file (encrypted)

file_in = open(INPUT_FILE, 'rb')
nonce = file_in.read(16) # Read the nonce out - this is 16 bytes long
tag = file_in.read(16) # Read the tag out - this is 16 bytes long
ciphered_data = file_in.read() # Read the rest of the data out
file_in.close()

# Decrypt and verify
cipher = AES.new(key, AES.MODE_EAX, nonce)
original_data = cipher.decrypt_and_verify(ciphered_data, tag) # Decrypt and verify with the tag

if original_data.decode("utf-8") == plaintext:
    print("Decryption is successful using EAX mode for plaintext - ", original_data)
else:
    print("Decrypted data does not match original plaintext!!")
