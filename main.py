from auth import log_in, register
import utils
from task_manager import *


#########################################################################################
def login():
    print(
        """
=========================== LOGIN ===========================
Welcome to the Task Tracker application!
Please enter your username and password to access your tasks.
If you don't have an account, please register first.
1.login
2.register
3.exit          
=============================================================       
"""
    )


#########################################################################################
def menu():
    print(
        """
=========================== MENU ===========================      
1.Add Task 
2.View Tasks 
3.Search for Task (By Task name or ID)
4.Mark Task as Done
5.Edit Task 
6.Delete Task 
7.exit           
=============================================================
  """
    )


#########################################################################################
def main():
    while True:
        login()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        if choice == 1:
            if log_in():
                break
        elif choice == 2:
            if register():
                break
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")
    while True:
        menu()
        try:
            op = int(input("Chose an Option : "))
        except ValueError:
            print("Invalid input...")

        if op == 1:
            title = input("Enter the Task Title :")
            description = input("Enter the task description ")
            add_task(title, description)
        elif op == 2:
            view_tasks()
        elif op == 3:
            query = input("Enter the task id or Title :")
            search_task(query)
        elif op == 4:
            try:
                task_id = int(input("Enter the Task Id"))
            except ValueError:
                print("invalid input")
            mark_done(task_id)
        elif op == 5:
            try:
                task_id = int(input("Enter the Task id u want to Edit :"))
            except ValueError:
                print("invalid input...")
            new_title = input("Enter the new Title :")
            new_desc = input("Enter the new desc : ")
            edit_task(task_id, new_title, new_desc)
        elif op == 6:
            try:
                task_id = int(input("Enter the Task id u want to Delete :"))
            except ValueError:
                print("invalid input...")
            delete_task(task_id)
        elif op == 7:
            print("Exiting the program..")
            break
        else:
            print("invalid input...try again...")


#########################################################################################
if __name__ == "__main__":
    main()
#########################################################################################
