from json import load
from misc.clear import clear
from add import add
from student_details import student_details


def view():
    with (open("./misc/student_records.json", "r+") 
          as records_json):
        student_records = load(records_json)

    with (open("./misc/menu_error.txt") 
          as error_message):
        error_message = error_message.read()

    open_view = True
    error = False
    student_options = [f"{num}" for num in range(1, len(student_records) + 1)]


    while open_view:
        list_records(student_records)

        if error:
            print(error_message)
            error = False

        user_input = input("Choose an option: ").upper()

        if user_input in student_options:
            student_records = student_details(int(user_input) - 1, 
                                                student_records
                                                )
                
        elif user_input == "A":
            student_records = add(student_records)

        elif user_input == "Q":
            open_view = False

        else:
            error = True


def list_records(student_records):
    clear()
    student_no = 1
    column_1 = True

    print("STUDENT RECORDS\n")

    for student in student_records:
        row = str(student_no) + " - " + student_records[student_no - 1]["NAME"]
        if column_1:
            print(f"{row:50}", end="")

        else:
            print(f"{row:50}")
        
        student += 1
        column_1 = not column_1
            
    if not column_1:
        print()

    print("\nA - Add new student",
          "\nQ - Return to main menu\n")
