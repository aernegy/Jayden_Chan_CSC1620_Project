from json import dump, load
from time import sleep


def delete(student):
    user_input = input("Enter Y to confirm deletion: ").upper()

    if user_input == "Y":
        with open("./misc/student_records.json", "r+") as student_records_json:
            student_records = load(student_records_json)

        del student_records[student]

        with open("./misc/student_records.json", "w") as student_records_json:
            dump(student_records, student_records_json, indent=4)

        print("DELETED SUCCESSFULLY!")

        sleep(2)

    else:
        print("DELETION CANCELLED!")

        sleep(2)