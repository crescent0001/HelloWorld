# https://pypi.org/project/starkbank-ecdsa/

from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey


# Generate new Keys
privateKey = PrivateKey()
publicKey = privateKey.publicKey()

message = "My test message"

# Generate Signature
signature = Ecdsa.sign(message, privateKey)

# To verify if the signature is valid
print("Verifying validity of signature.")
print(Ecdsa.verify(message, signature, publicKey))

# This library is compatible with OpenSSL, so you can use it to generate keys:
#   openssl ecparam -name secp256k1 -genkey -out privateKey.pem
#   openssl ec -in privateKey.pem -pubout -out publicKey.pem

# Create a message.txt file and sign it:
#   openssl dgst -sha256 -sign privateKey.pem -out signatureDer.txt message.txt


#To verify:
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.signature import Signature
from ellipticcurve.publicKey import PublicKey
from ellipticcurve.utils.file import File

publicKeyPem = File.read("publicKey.pem")
signatureDer = File.read("signatureDer.txt", "rb")
message = File.read("message.txt")

publicKey = PublicKey.fromPem(publicKeyPem)
signature = Signature.fromDer(signatureDer)

print("Verifying signature file <signatureDer.txt> with original message & public key.")
print(Ecdsa.verify(message, signature, publicKey))


# You can also verify it on terminal:
#   openssl dgst -sha256 -verify publicKey.pem -signature signatureDer.txt message.txt

# NOTE: If you want to create a Digital Signature to use with Stark Bank, you need to convert the binary signature to base64.
#   openssl base64 -in signatureDer.txt -out signatureBase64.txt

from ellipticcurve.signature import Signature
from ellipticcurve.utils.file import File

signatureDer = File.read("signatureDer.txt", "rb")

signature = Signature.fromDer(signatureDer)

print("Displaying content of <signatureDer.txt>")
print(signature.toBase64())   
