import json
from clear import clear


def main():
    clear()

    with (open("./files/Jayden_Chan_Project/student_records.json", "r+") 
          as student_records):

        student_records = json.load(student_records)

        list_records(student_records)

        open_view = True
        error = False
        error_message = "Error message"

        while open_view:
            user_input = input("Choose an option: ").upper()

            if user_input in [f"{num}" for num in range(1, len(student_records) + 1)]:
                print(student_records[user_input])

            else:
                clear()
                list_records(student_records)
                print(error_message)


def list_records(student_records):
    student_no = 1

    for student in student_records:
        print(student_no, "-", student_records[student]["NAME"])
        student_no += 1

    print("A - Add new student\n")

    print("STUDENT RECORDS\n")