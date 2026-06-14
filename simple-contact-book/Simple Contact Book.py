import json
import os
import sys
import tempfile

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


class ContactBook:
    def __init__(self):
        self.contacts = []

    def load(self, data_file=DATA_FILE):
        if not os.path.exists(data_file):
            return
        try:
            with open(data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: contact data could not be read. Starting with an empty book.")
            return
        if not isinstance(data, list):
            print("Warning: contact data is invalid. Starting with an empty book.")
            return
        contacts = []
        for item in data:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", "")).strip()
            phone = str(item.get("phone", "")).strip()
            if name and phone:
                contacts.append({"name": name, "phone": phone})
        self.contacts = contacts

    def save(self, data_file=DATA_FILE):
        try:
            with open(data_file, "w", encoding="utf-8") as file:
                json.dump(self.contacts, file, ensure_ascii=False, indent=2)
        except OSError:
            print("Warning: failed to save contacts.")

    def find_exact(self, name):
        target = name.strip().lower()
        for contact in self.contacts:
            if contact["name"].lower() == target:
                return contact
        return None

    def search(self, query):
        key = query.strip().lower()
        return [
            contact for contact in self.contacts
            if key in contact["name"].lower() or key in contact["phone"]
        ]

    def add_contact(self, name, phone, data_file=DATA_FILE):
        clean_name = name.strip()
        clean_phone = phone.strip()
        if not clean_name:
            print("Name cannot be empty.")
            return False
        if not clean_phone:
            print("Phone cannot be empty.")
            return False
        if self.find_exact(clean_name):
            print(f"Contact '{clean_name}' already exists.")
            return False
        self.contacts.append({"name": clean_name, "phone": clean_phone})
        self.contacts.sort(key=lambda item: item["name"].lower())
        self.save(data_file)
        print(f"Added contact: {clean_name}")
        return True

    def update_contact(self, name, new_phone, data_file=DATA_FILE):
        contact = self.find_exact(name)
        if not contact:
            print(f"Contact '{name}' not found.")
            return False
        clean_phone = new_phone.strip()
        if not clean_phone:
            print("Phone cannot be empty.")
            return False
        contact["phone"] = clean_phone
        self.save(data_file)
        print(f"Updated contact: {contact['name']}")
        return True

    def delete_contact(self, name, data_file=DATA_FILE):
        contact = self.find_exact(name)
        if not contact:
            print(f"Contact '{name}' not found.")
            return False
        self.contacts.remove(contact)
        self.save(data_file)
        print(f"Deleted contact: {contact['name']}")
        return True


def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. {contact['name']} - {contact['phone']}")


def display_menu():
    print("\nContact Book Menu:")
    print("1. View all contacts")
    print("2. Add contact")
    print("3. Search contacts")
    print("4. Update phone number")
    print("5. Delete contact")
    print("6. Exit")


def run_self_test():
    with tempfile.TemporaryDirectory() as temp_dir:
        data_file = os.path.join(temp_dir, "contacts.json")
        book = ContactBook()
        if not book.add_contact("Alice", "111", data_file):
            print("SELF-TEST FAILED: add")
            return 1
        book = ContactBook()
        book.load(data_file)
        if not book.find_exact("Alice"):
            print("SELF-TEST FAILED: reload")
            return 1
        if not book.update_contact("Alice", "222", data_file):
            print("SELF-TEST FAILED: update")
            return 1
        if len(book.search("Ali")) != 1:
            print("SELF-TEST FAILED: search")
            return 1
        if not book.delete_contact("Alice", data_file):
            print("SELF-TEST FAILED: delete")
            return 1
        book = ContactBook()
        book.load(data_file)
        if book.contacts:
            print("SELF-TEST FAILED: deletion persistence")
            return 1
    print("SELF-TEST PASSED")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        raise SystemExit(run_self_test())

    book = ContactBook()
    book.load()
    if book.contacts:
        print(f"Loaded {len(book.contacts)} contact(s).")

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if not choice:
            print("Please enter a menu number.")
            continue
        if choice == "1":
            print_contacts(book.contacts)
        elif choice == "2":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            book.add_contact(name, phone)
        elif choice == "3":
            query = input("Search keyword: ").strip()
            if not query:
                print("Search keyword cannot be empty.")
                continue
            print_contacts(book.search(query))
        elif choice == "4":
            name = input("Contact name to update: ").strip()
            new_phone = input("New phone number: ").strip()
            book.update_contact(name, new_phone)
        elif choice == "5":
            name = input("Contact name to delete: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            book.delete_contact(name)
        elif choice == "6":
            book.save()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
