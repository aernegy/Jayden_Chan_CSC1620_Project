from misc.clear import clear
from update import update
from delete import delete


def student_details(student, student_records, error_message):
    '''
    Handles the logic of the student details menu, inlcuding input handling
    '''
    open_details = True
    error = False

    details_menu_options = {"U": update, 
                            "D": delete}


    while open_details:
        #Every time student details menu is refreshed, recalculate grade.
        #To handle updates in marks and subjects.
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


        student_details_menu(student, student_records, grade)

        if error:
            print(error_message)
            error = False

        user_input = input("\nChoose an option: ").upper()

        #Pass local records to function as well as the student's index
        #in the local records and json array.
        if user_input in details_menu_options:
            details_menu_options[user_input](
                student, 
                student_records, 
                error_message
                )

            #Stops the program from trying to reopen student details
            #menu when user tries deleting the record, to prevent errors
            #when the student is deleted. 
            if user_input == "D":
                break

        #To exit the program loop
        elif user_input == "Q":
            open_details = False

        else:
            error = True


def student_details_menu(student, student_records, grade):
    '''
    A function for printing the menu & options.
    '''
    clear()

    print("NAME:", student_records[student]["NAME"],
        "\nID:", student_records[student]["ID"],
        "\n\nGRADE:", grade)

    column_1 = True

    #A loop for printing two columns of information dynamically
    for subject in student_records[student]["GRADES"]:
        row = f"{subject}: {student_records[student]['GRADES'][subject]}"

        if column_1:
            print(f"{row:30}", end="")

        else:
            print(f"{row:30}")

        column_1 = not column_1

    #For cleaner presentation of the menu
    if not column_1:
        print()

    print("\nU - Update details",
        "\nD - Delete student record",
        "\nQ - Return")