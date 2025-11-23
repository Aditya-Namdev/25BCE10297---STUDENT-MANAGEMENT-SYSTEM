
import pandas as pd
import numpy as np

# Global dictionaries and DataFrame to store application data

# credentials: Stores user ID and password pairs for login (User ID as key, Password as value).

credentials = {}

# df: The main pandas DataFrame to store student records and their task grades.
df = pd.DataFrame()

# --- Authentication/Account Management Functions ---

def signup(user_id, passd):
    """
    Registers a new user account.
    
    Args:
        user_id (str): The desired unique username.
        passd (str): The password for the new account.
    """
    # Stores the new user ID and password in the global credentials dictionary.
    credentials[user_id] = passd
    
    print("---Sign up successfully---")
    print("---Please Login with your new user id and password---")
    print("---------------------------------------------------------------------------------")
    
def login(in_user_id, in_passd):
    """
    Authenticates a user against the stored credentials.
    
    Args:
        in_user_id (str): The user ID entered for login.
        in_passd (str): The password entered for login.
    """
    # Checks if the user ID exists in credentials and if the corresponding password matches.
    if in_user_id in credentials and credentials[in_user_id] == in_passd:
        
        print("---Logged in successfully---")
        print("---------------------------------------------------------------------------------")
        # Calls the main operational menu upon successful login.
        menu()
    
    else :
        
        print("---Ivalid Credentials---")
        print("---------------------------------------------------------------------------------")
        
def forgot_passd(in_user_id, in_passd):
    """
    Changes the password for an existing user ID.
    
    Args:
        in_user_id (str): The existing user ID to change the password for.
        in_passd (str): The new password to be set.
    """
    # Checks if the user ID exists in the credentials dictionary.
    if in_user_id in credentials :
        
        # Updates the password associated with the user ID.
        credentials[in_user_id]= in_passd
        print("---Password changed successfully---")
        print("---------------------------------------------------------------------------------")
        
    else:
        print("---Invalid User id ---")
        print("---------------------------------------------------------------------------------")
        
def delete_user_id(in_user_id, in_passd):
    """
    Deletes a user account after validating the user ID and password.
    
    Args:
        in_user_id (str): The user ID of the account to be deleted.
        in_passd (str): The password for the account to confirm deletion.
    """
    # Checks if the user ID exists and the password is correct.
    if ( in_user_id in credentials ) and ( credentials[in_user_id] == in_passd ) :
        # Removes the user ID and password pair from the global credentials dictionary.
        del credentials[in_user_id]
        print("---Account deleted successfully---")
        print("---------------------------------------------------------------------------------")
        
    else :
        print("---Ivalid Credentials---")
        print("---------------------------------------------------------------------------------")
        
# --- Student/Grade Management Functions ---
        
def add_student(name, reg_no):
    """
    Adds a new student record (Name and Registration_no) to the global DataFrame 'df'.
    
    Args:
        name (str): The name of the student.
        reg_no (str): The registration number of the student.
    """
    global df
    # Creates a new temporary DataFrame with the student's details.
    nsd = {"Name":[name], "Registration_no":[reg_no]}
    ndf = pd.DataFrame(nsd)
    
    # Concatenates the new student DataFrame with the existing global DataFrame.
    # ignore_index=True resets the index after concatenation.
    df = pd.concat([df, ndf], ignore_index=True)
    
def task_(task):
    """
    Adds a new task column to the DataFrame and collects marks for this task
    from all currently registered students, including input validation.
    
    Args:
        task (str): The name of the new task (e.g., 'Midterm', 'Assignment 1').
    """
    global df
    marks_lst = []
    
    print("\n --- Entering Marks for Students")
    print("---------------------------------------------------------------------------------")
    
    # Iterates over each student record (row) in the DataFrame.
    for index, row in df.iterrows():
        student_name = row['Name']
        
        while True :
            
            try:
                # Prompts the user to enter marks for the current student.
                marks = int(input(f"Enter marks for {student_name} : "))
                print("---------------------------------------------------------------------------------")
                
                # Input validation: marks must be non-negative.
                if marks >= 0 :
                    marks_lst.append(marks)
                    break
                
                else:
                    print("Marks cannot be negative. Please enter a valid score. ")
                    print("---------------------------------------------------------------------------------")
                    
            except ValueError:
                # Handles non-integer input.
                print("Ivalid input . please enter a whole number for the marks : ")
                print("---------------------------------------------------------------------------------")
                
    # Adds the collected list of marks as a new column named after the task.
    df[f"{task}"] = marks_lst
    
def view_students():
    """
    Presents a submenu for viewing and analyzing student data and grades.
    Includes options to view individual students, all students, task statistics, and total marks.
    """
    global df
    
    while True:
        print("1.View a Student")
        print("2.View all students")
        print("3.View average and standard deviation of each task")
        print("4.view total marks of the students")
        print("5.Exit")
        print("---------------------------------------------------------------------------------")
        
        try:
            choice_view = int(input("Enter your choice : "))
            print("---------------------------------------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice_view == 1:
            name = input("Enter students name : ")
            print("---------------------------------------------------------------------------------")
            # Filters the DataFrame to find rows where the 'Name' column matches the input name.
            rw = df[df['Name'] == name]
            
            if rw.empty:
                print(f"Student name {name} not found")
                print("---------------------------------------------------------------------------------")
                
            else:
                print(rw)
                print("---------------------------------------------------------------------------------")
                
        elif choice_view == 2:
            # Prints the entire student DataFrame.
            print(df)
            print("---------------------------------------------------------------------------------")
            
        elif choice_view == 3 :
            # Calculates the mean (average) for all numeric columns (tasks).
            print("Average of each task")
            mean = df.mean(numeric_only=True)
            print(mean)
            print("---------------------------------------------------------------------------------")
            
            # Calculates the standard deviation for all numeric columns (tasks).
            print("Standard deviation of each class")
            std = df.std(numeric_only=True)
            print(std)
            print("---------------------------------------------------------------------------------")
            
        elif choice_view == 4 :
            # Calculates the sum of marks row-wise (axis=1) for each student.
            print("Total marks of each student ")
            sum_marks = df.sum(axis=1, numeric_only=True)
            # Combines name and total marks for clear output.
            total_marks_df = pd.DataFrame({'Name': df['Name'], 'Total Marks': sum_marks})
            print(total_marks_df)
            print("---------------------------------------------------------------------------------")
        
        elif choice_view == 5:
            print("---Exiting the View option---")
            print("---------------------------------------------------------------------------------")
            break
        
        else :
            print("Ivalid choice")
            print("---------------------------------------------------------------------------------")
            
def delete():
    """
    Presents a submenu to remove either a student (row) or a task (column) from the DataFrame.
    """
    while True:
        
        global df
        
        print("1.Remove a Student")
        print("2.Remove A Task")
        print("3.Exit")
        print("---------------------------------------------------------------------------------")
        
        try:
            choice_del = int(input("Enter your choice : "))
            print("---------------------------------------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice_del == 1 :
            
            name_to_delete = input("Enter the of the student to remove : ")
            print("---------------------------------------------------------------------------------")
            # Finds the index of the row(s) matching the student name.
            student_index = df[df["Name"] == name_to_delete].index
            
            if student_index.empty:
                print(f"Student {name_to_delete} not found")
                print("---------------------------------------------------------------------------------")
                continue
            
            # Drops the row(s) based on the index.
            df = df.drop(student_index)
            # Resets the DataFrame index for a clean sequence.
            df = df.reset_index(drop=True)
            print(f"Successfully removed student {name_to_delete} ")
            print("---------------------------------------------------------------------------------")
            
        elif choice_del == 2 :
            
            column_to_delete = input("Enter the name of the task to remove : ")
            print("---------------------------------------------------------------------------------")
            
            # Checks if the specified column name exists in the DataFrame.
            if column_to_delete in df.columns :
                
                # Drops the column.
                df = df.drop(columns=[column_to_delete])
                print(f"Successfully removed the column {column_to_delete}")
                print("---------------------------------------------------------------------------------")
                
            else :
                print(f"Error: Column {column_to_delete} not found")
                print("---------------------------------------------------------------------------------")
                
        elif choice_del == 3 :
            
            print("---Exiting the delete option---")
            print("---------------------------------------------------------------------------------")
            break
        
        else :
            print("Ivalid choice")
            print("---------------------------------------------------------------------------------")
            
# --- Main Application Menus ---
            
def menu():
    """
    The main menu for student grade management, accessible after login.
    Directs to functions for adding students, adding tasks (grades), viewing data, and deleting records.
    """
    while True :
        
        print("1.Add Students")
        print("2.Add Task")
        print("3.View Students")
        print("4.Remove Student/Task")
        print("5.Exit")
        print("---------------------------------------------------------------------------------")
        
        try:
            choice = int(input("Enter your choice : "))
            print("---------------------------------------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
        if choice == 1 :
            name = input("Enter students name : ")
            reg_no = input("Enter registration number : ")
            print("---------------------------------------------------------------------------------")
            add_student(name, reg_no)
            
        elif choice == 2:
            task = input("Enter task name : ")
            print("---------------------------------------------------------------------------------")
            # Check if there are any students before adding tasks
            if not df.empty:
                task_(task)
            else:
                print("Please add students before adding tasks.")
                print("---------------------------------------------------------------------------------")
            
        elif choice == 3 :
            if not df.empty:
                view_students()
            else:
                print("No student data available to view.")
                print("---------------------------------------------------------------------------------")
            
        elif choice == 4 :
            if not df.empty:
                delete()
            else:
                print("No student data available to delete.")
                print("---------------------------------------------------------------------------------")
            
        elif choice == 5 :
            
            print("---Exiting---")
            print("---------------------------------------------------------------------------------")
            break
        else :
            print("Ivalid choice")
            print("---------------------------------------------------------------------------------")
            
            
        
def home_page():
    """
    The initial application entry point providing account management options
    (Create, Login, Forgot Password, Delete Account).
    """
    while True :
        
        print("1. Create new account ")
        print("2. Login ")
        print("3. Forgot Password ")
        print("4. Delete Account ")
        print("5. Exit ")
        print("---------------------------------------------------------------------------------")
        
        try:
            choice1 = int(input("Enter your choice :"))
            print("---------------------------------------------------------------------------------")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice1 == 1 :
            user_id = input("Enter User id :")
            passd = input("Enter Password :")
            print("---------------------------------------------------------------------------------")
            signup(user_id,passd)
            
        elif choice1 == 2:
            in_user_id = input("Enter User id :")
            in_passd = input("Enter Password :")
            print("---------------------------------------------------------------------------------")
            login(in_user_id,in_passd)
            
        elif choice1 == 3:
            in_user_id = input("Enter User id :")
            in_passd = input("Enter new Password :")
            print("---------------------------------------------------------------------------------")
            forgot_passd(in_user_id,in_passd)
            
        elif choice1 == 4:
            in_user_id = input("Enter User id :")
            in_passd = input("Enter Password :")
            print("---------------------------------------------------------------------------------")
            delete_user_id(in_user_id,in_passd)
        
        elif choice1 == 5:
            print("Closng the program.....")
            print("---------------------------------------------------------------------------------")
            break
        
        else:
            print("Invalid choice")
            print("---------------------------------------------------------------------------------")
            
# Starts the application by calling the home_page function.
home_page()