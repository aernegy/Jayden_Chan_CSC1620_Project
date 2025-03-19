from misc.clear import clear
from add import add
from student_details import student_details


def view(student_records, error_message):
    '''
    A function to handle the logic of viewing all records
    '''
    open_view = True
    error = False

    #To assist checking whether user_input is one of the options in the menu
    student_options = [f"{num}" for num in range(1, len(student_records) + 1)]


    while open_view:
        list_records(student_records)

        #Only triggered if user entered invalid input
        if error:
            print(error_message)
            error = False

        user_input = input("Choose an option: ").upper()

        #If user did enter a valid option to view a student,
        #open up that student's records using student_details().
        #The first parameter is to inform the function which student
        #the user wishes to view.
        if user_input in student_options:
            student_details(
                int(user_input) - 1, 
                student_records,
                error_message
                )
                
        elif user_input == "A":
            student_records = add(student_records)

        #To exit the program loop
        elif user_input == "Q":
            open_view = False

        else:
            error = True


def list_records(student_records):
    '''
    A function to streamline printing the menu & options.
    student_records is passed into function for efficiency,
    rather than reading the json file every time the menu is opened.
    '''
    clear()
    student_no = 1
    column_1 = True

    print("STUDENT RECORDS\n")

    #A loop for printing two columns of information dynamically
    for student in student_records:
        row = str(student_no) + " - " + student["NAME"]

        if column_1:
            print(f"{row:50}", end="")

        else:
            print(f"{row:50}")
        
        student_no += 1
        column_1 = not column_1

    #For cleaner presentation of the menu        
    if not column_1:
        print()

    print("\nA - Add new student",
          "\nQ - Return to main menu\n")
