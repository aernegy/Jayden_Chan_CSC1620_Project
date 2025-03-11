import json
from misc.clear import clear
from add import add
from delete import delete
from update import update


def view():
    with (open("./files/Jayden_Chan_Project/misc/student_records.json", "r+") 
          as student_records_json):
        
        student_records = json.load(student_records_json)

    list_records(student_records)

    open_view = True
    error = False
    error_message = "Error message"

    while open_view:
        list_records(student_records)

        if error:
            print(error_message)
            error = False

        user_input = input("Choose an option: ").upper()

        if user_input in student_records:
            student_details(user_input, student_records)

        elif user_input == "A":
            student_records = add(student_records)

        elif user_input == "Q":
            open_view = False


def list_records(student_records):
    clear()
    student_no = 1
    column_1 = True

    for student in student_records:
        if column_1:
            print(f"{student + " - " + student_records[student]["NAME"]:50}", 
                  end="")
            # print(student_no, "-", student_records[student]["NAME"])
            column_1 = False

        else:
            print(f"{student + " - " + student_records[student]["NAME"]:50}")
            column_1 = True

    print("\nA - Add new student",
          "\nQ - Return to main menu")

    print("STUDENT RECORDS\n")


def student_details(student, student_records):
    details_menu_options = {"U": update, 
                            "D": delete}

    average_marks = (sum(student_records[student]["GRADES"].values())
                     / len(student_records[student]["GRADES"])) 

    if average_marks >= 85:
        grade = "A"

    elif 70 <= average_marks < 85:
        grade = "B"

    elif 50 <= average_marks < 70:
        grade = "C"

    elif average < 50:
        grade = "F"
    

    open_details = True
    error = False
    error_message = "Error message"

    while open_details:
        clear()

        print("NAME:", student_records[student]["NAME"],
            "\nID:", student_records[student]["ID"],
            "\n\nGRADE:", grade)

        for subject in student_records[student]["GRADES"]:
            print(f"{subject}: {student_records[student]["GRADES"][subject]}")

        print("\nU - Update details",
            "\nD - Delete student record",
            "\nQ - Return to student records")

        if error:
            print(error_message)
            error = False

        user_input = input("\nChoose an option: ").upper()

        if user_input in details_menu_options:
            details_menu_options[user_input]()

        elif user_input == "Q":
            open_details = False
