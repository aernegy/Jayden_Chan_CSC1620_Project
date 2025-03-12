from view import view
from search import search
from misc.clear import clear


def main():
    with open("./misc/main_menu.txt") as main_menu:
        main_menu = main_menu.read()

    with (open("./misc/menu_error.txt") 
          as error_message):
        error_message = error_message.read()

    clear()

    main_menu_options = {"1": view, 
                         "2": search
                         }
                         
    open_main = True
    error = False

    while open_main:
        clear()
        print(main_menu)

        if error:
            print(error_message)
            error = False
            
        user_input = input("Choose an option: ").upper()

        if user_input in main_menu_options:
            main_menu_options[user_input]()
            clear()
            print(main_menu)

        elif user_input == "Q":
            open_main = False
            clear()
            print("Program shutdown \nHasta la vista!")

        else:
            error = True
    

main()