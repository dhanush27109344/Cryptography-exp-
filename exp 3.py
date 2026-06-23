from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generate RSA Private Key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Generate Public Key
public_key = private_key.public_key()

message = input("Enter message to sign: ").encode()

# Create Digital Signature using Private Key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature Generated Successfully!")
print("Signature:", signature.hex())

# Verify Signature using Public Key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\nVerification Successful!")
    print("Message is authentic and has not been modified.")

except Exception:
    print("\nVerification Failed!")
    print("Message may have been modified or signature is invalid.")