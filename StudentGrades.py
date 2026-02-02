michael = {"Name": "Michael",
           "Subjects": ["English", "Math", "Physics"],
           "Grades": [98, 99, 97]}
alex = {"Name": "Alex",
           "Subjects": ["English", "Math", "Physics"],
           "Grades": [96, 97, 95]}
jake = {"Name": "Jake",
           "Subjects": ["English", "Math", "Physics"],
           "Grades": [94, 98, 94]}
all_dicts = { "michael": michael,
              "alex": alex,
              "jake": jake,}
while True:
    name = input("Please enter a name (or 'exit' to quit): ").strip().lower()
    if name == "exit":
        print("Goodbye!")
        break
    if name not in all_dicts:
        print("Not found.")
        continue
    grades = all_dicts[name]["Grades"]
    average = sum(grades) / len(grades)
    print(f"Average for {name.title()} is {average:.2f}")

