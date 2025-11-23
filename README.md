# 25BCE10297---STUDENT-MANAGEMENT-SYSTEM
Student Grade Management System based on python with pandas dataframe.

# *Student Grade Management System*

## *Overview*

The Student Grade Management System (SGMS) is a simple terminal-based Python program that helps store and manage student academic records. It allows teachers or administrators to add students, enter marks, view records, and calculate basic statistics such as averages and totals.
The project uses pandas for managing the data and numpy for calculations.

---

## *Features*

### 1. User Authentication

* Create account (Sign Up)
* Login using stored username and password
* Reset password
* Delete account

### 2. Student Management

* Add new students (name and registration number)
* View a single student’s details
* View all students
* Remove students

### 3. Task / Grade Management

* Add tasks (assignments, tests, exams, labs, etc.)
* Enter marks for each student
* Validate numeric inputs and prevent negative values
* Delete task columns

### 4. Analysis Tools

* Calculate average marks
* Calculate standard deviation
* Calculate total marks per student

### 5. Error Handling

* Handles invalid menu options
* Prevents incorrect or non-numeric mark entries
* Gives clear instructions for users

---

## *Tools Used*

* Python 3
* pandas
* numpy
* Dictionary-based authentication
* Terminal/Command Prompt

---

## *How to Install and Run*

1. Install Python 3.
2. Install required libraries:

   
   pip install pandas numpy
   
3. Download the .py file.
4. Run the program:

   
   python filename.py
   

---

## *How to Test the Program*

1. Create a new user account.
2. Login using valid credentials.
3. Add multiple students.
4. Add tasks like assignments or tests and enter marks.
5. View:

   * One student
   * All students
   * Averages and standard deviation
   * Total marks
6. Delete students or tasks.
7. Exit using the menu.

---

## *Screenshots*

*1. Main Menu* – 
<img width="692" height="686" alt="Screenshot 2025-11-23 172053" src="https://github.com/user-attachments/assets/28a2817d-bf3a-4322-9028-c2c717c4b6d2" />

*2. Adding Students* –
<img width="411" height="334" alt="Screenshot 2025-11-23 205646" src="https://github.com/user-attachments/assets/f761bb71-a50a-4540-91fd-eb5823ed7aa1" />

*3. Adding Tasks and Marks* –
<img width="431" height="653" alt="Screenshot 2025-11-23 210056" src="https://github.com/user-attachments/assets/c072c248-4cf8-438e-94b3-0fc0632de00b" />

*4. Viewing All Students* – 
<img width="599" height="836" alt="Screenshot 2025-11-23 210137" src="https://github.com/user-attachments/assets/74c5b3f1-8202-48d5-a3fe-b5de439c2a0b" />
 

---

## *Future Scope*

Several small upgrades can be added in the future to improve the project:

* Export student records as an *Excel (.xlsx) file*.
* Import existing student lists from an Excel or CSV file.
* Auto-save the student DataFrame whenever changes are made.
* Create a *CSV backup* after each update.
* Add search functionality (by name or registration number).
* Update marks without deleting the whole task.
* Generate a simple summary report for individual students.
* Rank students based on total marks.
* Add basic color highlights in the terminal for readability.

These enhancements are easy to add later and keep the project beginner-friendly.
