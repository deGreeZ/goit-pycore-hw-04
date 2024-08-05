def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name_is_in_contacts(name, contacts):
        return f"User \"{name}\" is already exist."
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if not name_is_in_contacts(name, contacts):
        return f"User \"{name}\" does not exist."
    contacts[name] = phone
    return "Contact changed."

def find_contact(args, contacts):
    name = args.pop()
    if not name_is_in_contacts(name, contacts):
        return f"User \"{name}\" does not exist"
    return contact_info(name, contacts[name])

def show_all_contacts(contacts):
    return "\n".join([contact_info(name, phone) for name, phone in contacts.items()])

def name_is_in_contacts(name, contacts):
    return name in contacts.keys()

def contact_info(name, phone):
    return f"{name}: {phone}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
