from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64

def load_public_key(filename):
    with open(filename, "rb") as f:
        pem_data = f.read()
        public_key = serialization.load_pem_public_key(pem_data)
        return public_key

def encrypt_info(public_key, info):
    encrypted_info = public_key.encrypt(
        info.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_info

def main():
    public_key_filename = "public_key.pem"

    # Load the public key from file
    public_key = load_public_key(public_key_filename)

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    student_id = input("Enter your student ID: ")

    # Combining the user's information into a single string
    info_string = f"{name},{email},{student_id}"

    # Encrypting the user's information with the public key
    encrypted_info = encrypt_info(public_key, info_string)

    # Encoding the encrypted information in base64
    base64_encoded_info = base64.b64encode(encrypted_info).decode()

    print("Base64 encoded encrypted information:")
    print(base64_encoded_info)

if __name__ == "__main__":
    main()
