from json import dump, load
from time import sleep


def delete(student, student_records):
    user_input = input("Enter Y to confirm deletion: ").upper()

    if user_input == "Y":
        #Delete student from local records
        del student_records[student]

        #Delete student from json records
        with open("./misc/student_records.json", "w") as records_json:
            dump(student_records, records_json, indent=4)

        print("DELETED SUCCESSFULLY!")

        sleep(2)

    else:
        print("DELETION CANCELLED!")

        sleep(2)

    #Update the local record in student_details.py
    return student_records