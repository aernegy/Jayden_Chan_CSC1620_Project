from json import dump, load
from time import sleep


def delete(student, student_records):
    user_input = input("Enter Y to confirm deletion: ").upper()

    if user_input == "Y":
        del student_records[student]

        with open("./misc/student_records.json", "w") as records_json:
            dump(student_records, records_json, indent=4)

        print("DELETED SUCCESSFULLY!")

        sleep(2)

    else:
        print("DELETION CANCELLED!")

        sleep(2)

    return student_records