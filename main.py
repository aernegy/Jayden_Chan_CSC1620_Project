from json import load, dump
from view import view
from search import search
from misc.clear import clear


from os.path import dirname
from contextlib import chdir


def main():
    main_menu_options = {"1": view, 
                         "2": search
                         }
                         
    open_main = True
    error = False


    with chdir(dirname(__file__)):
        with (
            open("misc/student_records.json", "r+") as records_json,
            open("misc/main_menu.txt") as main_menu,
            open("misc/menu_error.txt") as error_message
        ):

            student_records = load(records_json)
            main_menu = main_menu.read()
            error_message = error_message.read()

            #Main menu always printed unless a valid option is entered
            while open_main:
                clear()
                print(main_menu)




                #Only triggered if user entered invalid input
                if error:
                    print(error_message)
                    error = False
                    
                user_input = input("Choose an option: ").upper()

                if user_input in main_menu_options:
                    student_records = main_menu_options[user_input](
                        student_records, 
                        error_message
                        )

                #To exit the program loop
                elif user_input == "Q":
                    open_main = False
                    clear()
                    print("Program shutdown \nHasta la vista!")

                else:
                    error = True

            records_json.seek(0)
            dump(student_records, records_json, indent=4)
            records_json.truncate()
        

main()