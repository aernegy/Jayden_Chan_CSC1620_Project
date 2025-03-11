from json import load
from misc.clear import clear
from update import update
from delete import delete

def student_details(student):
    with open("./misc/student_records.json", "r+") as student_records_json:
        student_records = load(student_records_json)

    average_marks = (sum(student_records[student]["GRADES"].values())
                     / len(student_records[student]["GRADES"])) 

    if average_marks >= 85:
        grade = "A"

    elif 70 <= average_marks < 85:
        grade = "B"

    elif 50 <= average_marks < 70:
        grade = "C"

    elif average_marks < 50:
        grade = "F"
    

    open_details = True
    error = False

    with (open("./misc/menu_error.txt") 
          as error_message):
        error_message = error_message.read()
    
    details_menu_options = {"U": update, 
                            "D": delete}

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
            details_menu_options[user_input](student)

            with (open("./misc/student_records.json", "r+") 
                  as student_records_json):
                student_records = load(student_records_json)

            if user_input == "D":
                break

        elif user_input == "Q":
            open_details = False