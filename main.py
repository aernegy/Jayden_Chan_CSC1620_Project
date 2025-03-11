from view import view
from search import search
from misc.clear import clear


def main():
    clear()

    main_menu_options = {"1": view, 
                         "2": search
                         }
                         
    with open("./files/Jayden_Chan_Project/misc/main_menu.txt") as main_menu:
        main_menu = main_menu.read()

        open_main = True
        error = False
        error_message = "Error message"

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
                print("quitting")

            else:
                clear()
                print(main_menu)
                print(error_message)    


def search():
    print("Searching")
    

main()