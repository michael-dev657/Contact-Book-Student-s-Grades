contacts = {"michael": "01212008607",
            "jackson": "012120469",
            "will": "01213009305"}
print(contacts.keys())
while True:
    name = input("Please enter a contact (or 'exit' to quit): ").strip().lower()
    if name.lower() == 'exit':
        print("Goodbye!")
        break
    if name in contacts:
        print(contacts[name])
    if name not in contacts:
        print("Sorry! Contact not found.")