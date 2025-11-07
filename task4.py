
from typing import Tuple

CONTACTS: dict[str, str] = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return str(e) or "Contact not found."
        except ValueError as e:
            return str(e) or "Give me name and phone please."
        except IndexError as e:
            return str(e) or "Enter the argument for the command"
    return inner


def parse_input(user_input: str) -> Tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]



def hello() -> str:
    return "How can I help you?"

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args[0], args[1]
    if name not in contacts:
        raise KeyError("Contact not found.")
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) < 1:
        raise IndexError("Enter user name")
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found.")
    return contacts[name]

@input_error
def show_all(_: list[str], contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts yet."
    lines = [f"{name}: {phone}" for name, phone in sorted(contacts.items())]
    return "\n".join(lines)


def main() -> None:
    contacts = CONTACTS 
    print("Welcome to the assistant bot! Type 'help' to see commands.")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command in ("help", "?"):
            print(
                "Commands:\n"
                "  hello                      → How can I help you?\n"
                "  add <name> <phone>         → add new contact\n"
                "  change <name> <phone>      → update contact phone\n"
                "  phone <name>               → show contact phone\n"
                "  all                        → list all contacts\n"
                "  close | exit               → quit"
            )
        elif command == "":
            print("Enter the argument for the command")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
