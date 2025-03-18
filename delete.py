from time import sleep


def delete(student, student_records, *error_message):
    '''
    Handles the logic of deleting a student
    '''
    user_input = input("Enter Y to confirm deletion: ").upper()

    if user_input == "Y":
        #Delete student from local records
        del student_records[student]

        print("DELETED SUCCESSFULLY!")

        sleep(2)

    else:
        print("DELETION CANCELLED!")

        sleep(2)

    #Update the local record in student_details.py
    return student_records