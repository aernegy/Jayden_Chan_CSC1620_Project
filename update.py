from json import dump, load
from time import sleep
from misc.clear import clear


def update(student, student_records):
    with open("./misc/menu_error.txt") as error_message:
        error_message = error_message.read()
    
    open_update = True
    error = False
    details_options = {"1": "NAME", "2": "ID"}
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
            if user_input in details_options:
                val = input("\nEnter new value: ")
                
                student_records[student][details_options[user_input]] = val


            elif user_input in subject_options:
                sub_update = subject_update()

                sub_corr = dict(enumerate(
                                student_records[student]["GRADES"], 3
                                    )
                                )

                del (student_records[student]["GRADES"]
                                    [sub_corr[int(user_input)]])

                student_records[student]["GRADES"].update(sub_update)


            with open("./misc/student_records.json", "w") as records_json:
                dump(student_records, records_json, indent=4)

            clear()

            print("UPDATED SUCCESSFULLY")
            
            sleep(1.5)


        elif user_input == "A":
            new_sub = subject_update()

            for key in new_sub:
                if key in [name.upper() for name in student_records[student]["GRADES"].keys()]:
                    print("ERROR: Subject already exists")
                    sleep(2)
                    break
            
                else:
                    student_records[student]["GRADES"].update(new_sub)

                    clear()

                    print("UPDATED SUCCESSFULLY")

                    sleep(1.5)


        elif len(user_input) > 1 and user_input[0] == "D":
            sub_corr = dict(zip([f"{num}" for num in range(
                                    3, 
                                    len(student_records[student]["GRADES"]) + 3
                                    )
                                 ], 
                                student_records[student]["GRADES"]
                                )
                            )

            if user_input[1:] in sub_corr:
                cnfm = input("Enter Y to confirm deletion: ").upper()
                
                if cnfm == "Y":
                    del student_records[student]["GRADES"][
                        sub_corr[user_input[1:]]
                        ]

                    with (open("./misc/student_records.json", "w") 
                          as records_json):
                        dump(student_records, records_json, indent=4)

                    print("DELETED SUCCESSFULLY")

                    sleep(2)

                else:
                    print("DELETION CANCELLED")

                    sleep(2)

            else:
                error = True


        elif user_input == "Q":
            open_update = False

        else:
            error = True

    return student_records


def list_fields(student, student_records):
    print(f"1 - NAME: {student_records[student]["NAME"]}",
          f"\n2 - ID: {student_records[student]["ID"]}",
          "\n\nGRADES:")

    menu_counter = 3
    for subject in student_records[student]["GRADES"]:
        print(f"{menu_counter} - {subject}:",
              f"{student_records[student]["GRADES"][subject]}")

        menu_counter += 1

    print("\nA - Add subject",
          "\nQ - Return to student details",
          "\nTo delete subject, type D[option number]. E.g. D3, D4..."
          )


def subject_update():
    sub = input("\nEnter subject name: ")

    while True:
        try:
            mark = float(input(f"Enter {sub} grade: "))
            break

        except ValueError:
            print("ERROR: Please enter a positive number")
            pass

    return {sub: mark}