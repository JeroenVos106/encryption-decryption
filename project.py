import sys
from encryption import Crypt
from database import Database


database = Database("msg_database.csv")
crypt = Crypt()

def main():
    while True:
        user_choice: str = get_user_input()
        if user_choice == "0":
            print(handle_too_many_args(user_choice))
        elif user_choice == "1":
            print(handle_cli_input())
        elif user_choice == "2":
            print(handle_manual_input())
        elif user_choice == "3":
            print(handle_retrieve_message())


def handle_too_many_args(user_choice):
    if user_choice == "0":
        return "Too many command-line arguments!"


def handle_cli_input(user_choice):
    if user_choice == "1":
        user_input = cli_input()
        encoded_input = encode_bytes(user_input)
    return encoded_input


def handle_manual_input(user_choice):
    if user_choice == "2":
        user_manual = manual_input()
        saving_message(user_manual)
        key = (
            database.get_key()
        )  # Gets the key from the database that is accociated with the most recent input message, see Database.py for more information
        print(
            f"{key}\nKeep this safe! If you lose your key you will not be able to retrieve your message every again!"
        )


def handle_retrieve_message(user_choice):
    if user_choice == "3":
        message = retrieve_message(user_choice)
        return message.decode()



def retrieve_message(raw_text):
    """
    If user input in choice_menu() was 3, this function retrieves the encrypted message using the user-specific key.
    Takes the Key as input.
    If the input is not a key, an IndexError will be raised from the Database class
    """
    if raw_text == "3":
        key = input("Insert key: ")
        message = database.get_message(key)
        decrypted_message = crypt.decrypt(key, message)
        return decrypted_message
    else:
        return


def saving_message(raw_text):
    """
    Saves the message that user gave as input into the database.
    Takes the original text, encodes it to bytes and then encrypts it using encryption()
    """
    raw_data = encode_bytes(raw_text)
    key, message = encryption(raw_data)
    database.save_message(key, message)


def encode_bytes(text):
    """
    Takes text and returns that same text encoded as bytes.
    """
    text_to_bytes = text.encode()
    return text_to_bytes


def encryption(raw_text):
    """
    Encrypts raw text with the use of the Crypt class
    returns encrypted text and passes it to saving_message()
    returns key and passes it to saving_message()
    """
    encrypted_text = crypt.encrypt(raw_text)
    key = crypt.key
    return key, encrypted_text


def get_user_input():
    """
    Uses sys.argv as guideline for final user input
    Gets the user input that is created in the choice-menu and uses it to perform the next step in program.
    returns a number as str
    """
    if len(sys.argv) == 1:
        user_choice = choice_menu()
        if user_choice == 2:
            return "2"
        if user_choice == 3:
            return "3"
    elif len(sys.argv) == 2:
        return "1"
    elif len(sys.argv) > 2:
        return "0"


def cli_input():
    """
    Takes the Command-Line input of User and passes it to a Variable(conversion)
    """
    conversion = sys.argv[1]
    return conversion


def manual_input():
    """
    Takes user input as str, returns that input as a variable(answer/new_answer).
    Exeption for when user inputs 4, then complete program will be terminated.
    """
    answer = input("Input Text: ")
    if answer == "":
        new_answer = input(
            "Please input text, or to terminate program press 4 and hit enter\nInput Text:"
        )
    elif answer != "":
        return answer
    if new_answer == "4":
        sys.exit("Goodbye!")
    else:
        return new_answer


def choice_menu():
    """
    Prints a multiple-choice menu on the terminal and returns the user choice as an int
    Exeption for return when user inputs 4, then the complete program will be terminated.
    """
    while True:
        try:
            print("No Command-Line input, for key input and only encoded key, on Command-Line press 1 and hit enter")
            print("___________________________________________________________________________________________________")
            print("For manual text input press 2 and hit enter")
            print("___________________________________________________________________________________________________")
            print("For retrieval of message press 3 and hit enter")
            print("___________________________________________________________________________________________________")
            print("To exit the program press 4 and hit enter")
            print("___________________________________________________________________________________________________")
            num: int = int(input("Input: "))
            if num == 1:
                sys.exit("Please run program again with: python project.py your_file_here")
            if num == 2:
                return 2
            if num == 3:
                return 3
            if num == 4:
                sys.exit("Goodbye!")
        except ValueError:
            print("\nPlease input a number")


if __name__ == "__main__":
    main()
