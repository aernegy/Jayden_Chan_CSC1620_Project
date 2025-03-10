from os import system


def main():
    open_main = True

    clear()

    with open("./files/Jayden_Chan_Project/CSC1620_Project/main_menu.txt") as main_menu:
        main_menu = main_menu.read()
        
        while open_main:
            print(main_menu)
            user_input = input("Choose an option: ").upper()

            match user_input:
                case "1"|"2"|"3"|"Q":
                    open_main = False

                case _:
                    clear()
        
    match user_input:
        case "1":
            clear()
            print("Viewing")

        case "2":
            clear()
            print("Searching")

        case "3":
            clear()
            print("Adding")

        case "Q":
            return


def clear():
    system("clear")


main()