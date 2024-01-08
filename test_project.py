from project import retrieve_message, encode_bytes, choice_menu, manual_input, encryption, cli_input, saving_message
import pytest
from unittest.mock import patch



def test_retrieveMessage():
    class MockDatabase:
        @staticmethod
        def get_message(key):
            message = "Hello World"
            return "Z0FBQUFBQmxtXzFjUl9SWkR1Z01ad2Jvai02X0E2Z1dqU1gyaEJDaHZRUWc2MzJHSVVWVGV2WS0xa1ducVd4X1c0RHRfOFhWaTNiTzl2bzZsdXp1c2Jkbzhad1QzTzh3VFE9PQ=="

    class MockCrypt:
        @staticmethod
        def decrypt(key, message):
            encrypted_message = "Z0FBQUFBQmxtXzFjUl9SWkR1Z01ad2Jvai02X0E2Z1dqU1gyaEJDaHZRUWc2MzJHSVVWVGV2WS0xa1ducVd4X1c0RHRfOFhWaTNiTzl2bzZsdXp1c2Jkbzhad1QzTzh3VFE9PQ=="
            return "Hello World"

    with patch("builtins.input", return_value="Z0FBQUFBQmxtXzFjUl9SWkR1Z01ad2Jvai02X0E2Z1dqU1gyaEJDaHZRUWc2MzJHSVVWVGV2WS0xa1ducVd4X1c0RHRfOFhWaTNiTzl2bzZsdXp1c2Jkbzhad1QzTzh3VFE9PQ=="),\
         patch("project.database", MockDatabase()),\
         patch("project.crypt", MockCrypt()):
             result = retrieve_message("3")
             assert result == "Hello World"



def test_encodeBytes():
    assert encode_bytes("Hello") == b"\x48\x65\x6c\x6c\x6f"
    assert encode_bytes("Hello") == b"Hello"
    assert encode_bytes("Hello") != "Hello"


def test_choiceMenu():
    with patch("builtins.input", return_value="1"):
        with pytest.raises(SystemExit):
            choice_menu()
    with patch("builtins.input", return_value="4"):
        with pytest.raises(SystemExit):
            choice_menu()
    with patch("builtins.input", return_value="2"):
        assert choice_menu() == 2
    with patch("builtins.input", return_value="3"):
        assert choice_menu() == 3

def test_savingMessage():
    ...

def test_encryption():
    ...

def test_cliInput():
    ...

def test_manualInput():
    ...

