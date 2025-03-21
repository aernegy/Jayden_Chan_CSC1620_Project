from misc.clear import clear
from student_details import student_details
from time import sleep


def search(student_records, error_message):
    '''
    Handles the logic of searching for a student
    '''
    clear()

    print("STUDENT RECORDS SEARCH",
          "\n\nSearch for Student ID or Name:")

    user_search = input().upper()

    #To store the dictionaries containing the corresponding students 
    #who resulted from the search.
    results = []

    #To store the json array index of the resulting students 
    #from the search.  
    idx = []

    for student in student_records:
        #If the user's search matches a part of either a student's
        #name or ID
        if (user_search in student["NAME"].upper() 
                or user_search in student["ID"].upper() 
                and student not in results
            ):
            results.append(student)
            idx.append(student_records.index(student))

    #If there are search results:
    if results:
        open_results = True
        error = False

        #To help validate user input when selecting a particular student
        student_options = [f"{num}" for num in range(1, len(results) + 1)]

        while open_results:
            search_results(results)

            if error:
                print(error_message)
                error = False

            user_input = input("Choose an option: ").upper()

            #When the user enters a valid input to view a student,
            #open that student's details in the student_details menu.
            if user_input in student_options:
                student_details(
                    idx[int(user_input) - 1], 
                    student_records, 
                    error_message
                    )

            #To exit the search menu
            elif user_input == "Q":
                open_results = False

            else:
                error = True

    #If there are no search results:
    else:
        clear()
        print("NO RESULTS")
        sleep(1.5)


def search_results(results):
    '''
    A function to streamline printing the search results and options.
    Here, only the dicionaries of the resulting students from the search
    is passed into the function for efficiency.
    '''
    clear()

    print("SEARCH RESULTS\n")

    student_no = 1
    column_1 = True

    #A loop for printing two columns of information dynamically
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
    
    #For cleaner presentation of the menu
    if not column_1:
        print()

    print("\nQ - Return to main menu")