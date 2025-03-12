from json import load
from misc.clear import clear
from student_details import student_details
from time import sleep


def search():
    with (open("./misc/student_records.json", "r+") 
          as records_json):
        student_records = load(records_json)

    clear()

    print("STUDENT RECORDS SEARCH",
          "\n\nSearch for Student ID or Name:")

    user_search = input().upper()

    results = []
    idx = []

    for student in student_records:
        if (user_search in student["NAME"].upper() 
                or user_search in student["ID"].upper() 
                and student not in results
            ):
            results.append(student)
            idx.append(student_records.index(student))

    if not results:
        clear()
        print("NO RESULTS")
        sleep(1.5)

        return
        

    with (open("./misc/menu_error.txt") 
          as error_message):
        error_message = error_message.read()

    open_results = True
    error = False
    student_options = [f"{num}" for num in range(1, len(results) + 1)]

    while open_results:
        search_results(results)

        print(idx)

        if error:
            print(error_message)
            error = False

        user_input = input("Choose an option: ").upper()

        if user_input in student_options:
            student_records = student_details(idx[int(user_input) - 1], 
                                                student_records
                                                )
                
        # elif user_input == "A":
        #     student_records = add(student_records)

        elif user_input == "Q":
            open_results = False

        else:
            error = True



def search_results(results):
    clear()

    print("SEARCH RESULTS\n")

    student_no = 1
    column_1 = True

    for student in results:
        row = (str(student_no) + " - " + results[student_no - 1]["NAME"] 
               + f" ({results[student_no - 1]["ID"]})"
               )

        if column_1:
            print(f"{row:50}", end="")

        else:
            print(f"{row:50}")
        
        student_no += 1
        column_1 = not column_1
    
    if not column_1:
        print()

    print("\nQ - Return to main menu")