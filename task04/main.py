def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found."
        except ValueError:
            return "Give me a valid name and phone number, please."
        except IndexError:
            return "Insufficient arguments provided."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."

@input_error
def get_phone(args):
    name = args.strip()
    phone = contacts[name]
    return f"The phone number for {name} is {phone}."

@input_error
def show_all(_):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    commands = {
        "add": add_contact,
        "phone": get_phone,
        "all": show_all,
    }

    print("Bot is running. Enter commands:")
    while True:
        user_input = input("Enter a command: ").strip()
        if user_input.lower() in ("exit", "quit", "bye"):
            print("Goodbye!")
            break

        command, *args = user_input.split(maxsplit=1)
        if command in commands:
            handler = commands[command]
            args = args[0] if args else ""
            result = handler(args)
        else:
            result = "Unknown command. Please try again."

        print(result)

if __name__ == "__main__":
    main()