import csv
import base64

class Database():
    def __init__(self, file_path):
        self.file_path = file_path


    def get_message(self, key):
        """
        Gets the encrypted message accociated with its key from the database
        """
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == key:
                        bytes_object = base64.urlsafe_b64decode(row[1])
                        return bytes_object
        except IndexError:
            raise IndexError("No key was inputted")


    def save_message(self, key, message):
        """
        Saves the encrypted message to the database with its key linked to it
        To improve safety a password and username should be used to lock the message into a safe database!
        """
        with open(self.file_path, "a") as file:
            base64_string = base64.urlsafe_b64encode(message).decode()
            base64_key = base64.urlsafe_b64encode(key).decode()
            writer = csv.writer(file)
            writer.writerow([base64_key, base64_string])


    def get_key(self):
        """
        Returns the key that was most recently added to the user when user adds a new message to encrypt.
        """
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                last_key = None
                for row in reader:
                    last_key = row[0]
                return last_key
        except IndexError:
            raise IndexError("Not a valid message, please provide a message as text.")
