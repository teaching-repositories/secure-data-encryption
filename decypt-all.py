import os
import csv
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def load_private_key(filename):
    with open(filename, "rb") as f:
        pem_data = f.read()
        private_key = serialization.load_pem_private_key(
            pem_data,
            password=None  # No password for the private key
        )
        return private_key

def decrypt_info(private_key, encrypted_data):
    decrypted_info = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_info

def main():
    private_key_filename = "private_key.pem"
    directory_path = "./encrypted_files"  # Change to your encrypted files' directory path
    output_csv = "output.csv"
    error_log = "errors.log"

    # Load the private key from file
    private_key = load_private_key(private_key_filename)

    # Open CSV file for writing
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["github-username", "name", "email", "student number"])  # Write header

        # Loop through all files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory_path, filename)
                
                try:
                    # Read the encrypted data from file
                    with open(filepath, "rb") as f:
                        base64_encoded_encrypted_info = f.read()

                    # Decode the base64 encoded encrypted data
                    encrypted_info = base64.b64decode(base64_encoded_encrypted_info)

                    # Decrypt the data using the private key
                    decrypted_info = decrypt_info(private_key, encrypted_info).decode().splitlines()

                    # Extract github-username from the filename and write to CSV
                    github_username = filename.replace(".txt", "")
                    writer.writerow([github_username] + decrypted_info)

                except Exception as e:
                    with open(error_log, 'a') as log_file:
                        log_file.write(f"Error processing {filename}: {str(e)}\n")

if __name__ == "__main__":
    main()

