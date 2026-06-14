import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

    @staticmethod
    def from_dict(d):
        return Contact(str(d.get("name", "")), str(d.get("phone", "")))


class ContactBook:
    def __init__(self):
        self.contacts = []

    def load(self):
        """Load contacts from disk. Missing / corrupt files produce a warning
        and leave the book empty rather than raising."""
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: could not read {DATA_FILE} ({e}). Starting with an empty contact book.")
            return
        if not isinstance(data, list):
            print("Warning: contacts file did not contain a list. Starting with an empty contact book.")
            return
        for item in data:
            if isinstance(item, dict) and "name" in item and "phone" in item:
                self.contacts.append(Contact.from_dict(item))

    def save(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump([c.to_dict() for c in self.contacts], f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"Warning: failed to save contacts ({e}).")

    def find_by_name(self, name):
        target = name.strip().lower()
        for c in self.contacts:
            if c.name.strip().lower() == target:
                return c
        return None

    def add(self, name, phone):
        if self.find_by_name(name):
            print(f"Contact '{name}' already exists. Use option 4 to update the phone number.")
            return False
        self.contacts.append(Contact(name, phone))
        self.save()
        print(f"Added contact: {name}  {phone}")
        return True

    def show_all(self):
        if not self.contacts:
            print("No contacts.")
            return
        print("\nContacts:")
        for i, c in enumerate(self.contacts, 1):
            print(f"{i}. {c.name}  {c.phone}")

    def search(self, query):
        q = query.strip().lower()
        results = [c for c in self.contacts if q in c.name.lower() or q in c.phone]
        if not results:
            print(f"No contacts matching '{query}'.")
            return
        print(f"\nSearch results for '{query}':")
        for i, c in enumerate(results, 1):
            print(f"{i}. {c.name}  {c.phone}")

    def update_phone(self, name, new_phone):
        c = self.find_by_name(name)
        if not c:
            print(f"Contact '{name}' not found.")
            return False
        old = c.phone
        c.phone = new_phone
        self.save()
        print(f"Updated {name}: {old} -> {new_phone}")
        return True

    def delete(self, name):
        c = self.find_by_name(name)
        if not c:
            print(f"Contact '{name}' not found.")
            return False
        self.contacts.remove(c)
        self.save()
        print(f"Deleted contact: {name}")
        return True


def main():
    book = ContactBook()
    book.load()
    if book.contacts:
        print(f"Loaded {len(book.contacts)} contact(s) from {DATA_FILE}.")

    while True:
        print("\nContact Book Menu:")
        print("1. View all contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Update phone number")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if not choice:
            print("Please enter a menu number.")
            continue

        if choice == "1":
            book.show_all()
        elif choice == "2":
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            phone = input("Phone: ").strip()
            if not phone:
                print("Phone cannot be empty.")
                continue
            book.add(name, phone)
        elif choice == "3":
            q = input("Search keyword: ").strip()
            if not q:
                print("Search keyword cannot be empty.")
                continue
            book.search(q)
        elif choice == "4":
            name = input("Contact name to update: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            new_phone = input("New phone number: ").strip()
            if not new_phone:
                print("Phone cannot be empty.")
                continue
            book.update_phone(name, new_phone)
        elif choice == "5":
            name = input("Contact name to delete: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            book.delete(name)
        elif choice == "6":
            book.save()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
