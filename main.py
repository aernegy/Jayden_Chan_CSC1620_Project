from view import main as view
from clear import clear


def main():
    clear()

    main_menu_options = {"1": view, 
                         "2": search, 
                         "3": add, 
                         "Q": quit}
                         
    with open("./files/Jayden_Chan_Project/main_menu.txt") as main_menu:
        print(main_menu.read())

        open_main = True

        error_message = "Error message"

        while open_main:
            user_input = input("Choose an option: ").upper()

            if user_input in main_menu_options:
                open_main = False

            else:
                clear()
                print(main_menu)
                print(error_message)
    
    main_menu_options[user_input]()    


def search():
    print("Searching")


def add():
    print("adding")
    

def quit():
    print("quitting")


main()