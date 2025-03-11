from misc.clear import clear
from time import sleep
from json import dump, load


def add():
    clear()

    name = input("Enter student name: ")
    id = input("Enter student id: ")

    while True:
        try:
            num_subjects = int(input("\nEnter number of subjects: "))
            break

        except ValueError:
            pass
    
    subjects = []

    for num in range(1, num_subjects + 1):
        subjects.append(input(f"Enter subject {num} name: "))

    print()

    marks = []

    for subject in subjects:
        while True:
            try:
                marks.append(float(input(f"Enter {subject} grade: ")))
                break

            except ValueError:
                print("ERROR: Please enter a positive number")
                pass

    grades = dict(zip(subjects, marks))

    new_student = {"NAME": name, "ID": id, "GRADES": grades}

    with (open("./files/Jayden_Chan_Project/misc/student_records.json", "r+") 
          as student_records_json):
        student_records = load(student_records_json)

        student_records.update({f"{len(student_records) + 1}": new_student})

        student_records_json.seek(0)

        dump(student_records, student_records_json, indent=4)
            

    clear()

    print("STUDENT ADDED!")

    sleep(2)