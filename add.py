from misc.clear import clear
from time import sleep
from json import dump, load


def add(student_records):
    clear()

    name = input("Enter student name: ")
    id = input("Enter student id: ")

    #Input validation. The while loop only breaks
    #when the input is an integer
    while True:
        try:
            num_subjects = int(input("\nEnter number of subjects: "))
            break

        except ValueError:
            print("ERROR: Please enter a positive integer")
            pass
    
    subjects = ()

    for num in range(1, num_subjects + 1):
        subjects += input(f"Enter subject {num} name: "),

    print()

    marks = ()

    #Input validation. The same idea as the validation above
    for subject in subjects:
        while True:
            try:
                marks += float(input(f"Enter {subject} grade: ")),
                break

            except ValueError:
                print("ERROR: Please enter a positive number")
                pass

    #Collect all the data into a dictionary
    grades = dict(zip(subjects, marks))
    new_student = {"NAME": name, "ID": id, "GRADES": grades}

    #Update the local records
    student_records.append(new_student)

    #Update the json records
    with open("./misc/student_records.json", "w") as records_json:
        dump(student_records, records_json, indent=4)
            

    clear()

    print("STUDENT ADDED!")

    sleep(2)

    #Update the local records in view.py
    return student_records