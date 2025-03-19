from time import sleep
from misc.clear import clear


def update(student, student_records, error_message):
    '''
    A function to handle the logic of updating student records
    '''    
    open_update = True
    error = False

    #Menu options for updating name or ID
    details_options = {"1": "NAME", "2": "ID"}

    #Menu options for updating about existing subjects
    subject_options = [f"{num}" for num in 
                      range(3, len(student_records[student]["GRADES"]) + 3)]
                      

    while open_update:
        clear()

        list_fields(student, student_records)

        print()

        if error:
            print(error_message)
            error = False

        user_input = input("Choose field to update: ").upper()

        if user_input in details_options or user_input in subject_options:
            #To update details about name and id.
            if user_input in details_options:
                val = input("\nEnter new value: ")
                
                student_records[student][details_options[user_input]] = val

            #To update details about existing subjects
            elif user_input in subject_options:
                sub_update = subject_update()

                #A dictionary to help choose the correct index corresponding
                #to the correct subject in the student's record.
                sub_corr = dict(enumerate(
                                student_records[student]["GRADES"], 3
                                    )
                                )

                #Delete the existing record
                del (student_records[student]["GRADES"]
                                    [sub_corr[int(user_input)]])

                #Add the new record
                student_records[student]["GRADES"].update(sub_update)

            clear()

            print("UPDATED SUCCESSFULLY")
            
            sleep(1.5)


        elif user_input == "A":
            #A list of existing subjects under a student's name to help
            #check for duplicates
            sub_list = [name.upper() for name in student_records[student][
                "GRADES"].keys()]
                
            new_sub = subject_update()

            for key in new_sub:
                if key.upper() in sub_list:
                    print("ERROR: Subject already exists")
                    sleep(2)
            
                else:
                    #Update local records
                    student_records[student]["GRADES"].update(new_sub)

                    clear()

                    print("UPDATED SUCCESSFULLY")

                    sleep(1.5)
                
                break

        
        #To delete a subject
        elif len(user_input) > 1 and user_input[0] == "D":
            #A dictionary to help index subjects that a student has taken
            sub_corr = dict(zip([f"{num}" for num in range(
                                    3, 
                                    len(student_records[student]["GRADES"]) + 3
                                    )
                                 ], 
                                student_records[student]["GRADES"]
                                )
                            )

            #If the user entered a valid index that
            #refers to a certain subject.
            if user_input[1:] in sub_corr:
                cnfm = input("Enter Y to confirm deletion: ").upper()
                
                if cnfm == "Y":
                    #Delete local records
                    del student_records[student]["GRADES"][
                        sub_corr[user_input[1:]]
                        ]

                    print("DELETED SUCCESSFULLY")

                    sleep(2)

                else:
                    print("DELETION CANCELLED")

                    sleep(2)

            else:
                error = True

        #To exit the program loop
        elif user_input == "Q":
            open_update = False

        else:
            error = True


def list_fields(student, student_records):
    '''
    A function for printing the menu & options.
    '''
    print(f"1 - NAME: {student_records[student]["NAME"]}",
          f"\n2 - ID: {student_records[student]["ID"]}",
          "\n\nGRADES:")

    menu_counter = 3
    column_1 = True

    #A loop for printing two columns of information dynamically
    for subject in student_records[student]["GRADES"]:
        row = (f"{menu_counter} - {subject}: " + 
               f"{student_records[student]["GRADES"][subject]}")

        if column_1:
            print(f"{row:30}", end="")

        else:
            print(f"{row:30}")

        menu_counter += 1
        column_1 = not column_1

    #For cleaner presentation of the menu
    if not column_1:
        print()

    print("\nA - Add subject",
          "\nQ - Return to student details",
          "\nTo delete subject, type D[option number]. E.g. D3, D4..."
          )


def subject_update():
    '''
    A function to streamline gathering user input for updating existing or
    add new subjects to a student.
    '''
    sub = input("\nEnter subject name: ")

    #Input validation.
    while True:
        try:
            mark = float(input(f"Enter {sub} grade: "))
            break

        except ValueError:
            print("ERROR: Please enter a positive number")
            pass

    return {sub: mark}