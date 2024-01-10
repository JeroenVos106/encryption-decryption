# Encrypted Message Creation and Retrieval Program

**Overview**

Video demo: <URL HERE>

This program is designed to:
- Let a user make an encrypted message that will be stored in a database.
- Retrieve an encrypted message stored in a database using a, in this instance: message-specific key.
- The encryption and decryption are handled by a crypt module that I have written myself, and the messages are stored and retrieved using a database module.

**The `crypt` module**

The encryption module I have written for this program is not sufficient for real-world use! To use this program for modern security, it is advised to use another more sophisticated encryption module.

**The `database` module**

The database module I have written for this program makes use of files such as a CSV. This is also not a safe way for storing encrypted data. To safely store encrypted data, a real database should be used.

**Project.py**

This project was made as a final project for the course CS50P from Harvard. This project is not meant to be used as a real encryption tool. But because it is structured with classes like `crypt` and `database`, it is possible to make this program more secure. You could add the functionality of a username and password that is linked to a database. The password also needs to be handled safely and, of course, should minimally be encrypted as well (This is still not the safest method but better than storing passwords as plain text). So, the classes that are specified at the top of the `project.py` folder could be replaced with classes/libraries that handle encryption-decryption and databases a lot better. You could implement a profile structure with unique usernames and passwords, passwords which also should meet a reasonably high standard of complexity. I know that this project is far from perfect, but to implement the above-specified methods and functions it would take too many hours to complete because the complexity that comes with those implementations is too much for what I, at this moment, am capable of.

**One final important note for this program:**

When encrypting and decrypting data, the keys that are generated should not be used in a printing manner. Keys should be passed around (safely) inside of your program and/or database.

**Installation:**

- Clone the repository: `git clone https://github.com/ninja2002vw/encryption-decryption.git`
- Install the required dependencies: `pip install -r requirements.txt`

**Usage:**

Run the main program by executing the `main.py` script:

```bash
python main.py
```

Follow the on-screen instructions to interact with the program.
- If you choose option 1, the program will exit so you can rerun now with command-line input.
- If you choose option 2 you will be prompted for input of a message, after hitting enter you will receive your key and a warning message.
- If you choose option 3 to retrieve an encrypted message, you will be prompted to enter a key. The program will then decrypt the corresponding message using the key.
- If you choose option 4 the program will quit.

**Testing:**

Tests for the program are written using pytest. To run the tests, use the following command:

```bash
pytest test_project.py
```

This will execute the test cases in the tests directory, ensuring the functionality of the `retrieve_message` function. I only created 3 tests for this program. This is not because of negligence, but because it is not needed in the scope of this project. The other functions that could be (and should be!) tested for are in `test_project.py` but do not have functionality as of right now.

**Contributing:**

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. This could help me improve my future code and projects!

**License:**

This program is licensed under the MIT License.
```

Please make sure to check the formatting and adjust as needed.
