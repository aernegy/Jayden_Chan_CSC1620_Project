from misc.clear import clear
from time import sleep
from json import dump, load


def add(student_records):
    clear()

    name = input("Enter student name: ")
    id = input("Enter student id: ")

    while True:
        try:
            num_subjects = int(input("\nEnter number of subjects: "))
            break

        except ValueError:
            pass
    
    subjects = ()

    for num in range(1, num_subjects + 1):
        subjects += input(f"Enter subject {num} name: "),

    print()

    marks = ()

    for subject in subjects:
        while True:
            try:
                marks += float(input(f"Enter {subject} grade: ")),
                break

            except ValueError:
                print("ERROR: Please enter a positive number")
                pass

    grades = dict(zip(subjects, marks))

    new_student = {"NAME": name, "ID": id, "GRADES": grades}

    student_records.append(new_student)

    with open("./misc/student_records.json", "w") as records_json:
        dump(student_records, records_json, indent=4)
            

    clear()

    print("STUDENT ADDED!")

    sleep(2)

    return student_records