import tkinter as tk
from tkinter import messagebox, simpledialog
import os

#All the studentsworks are here such as exam and course marks as well as ID codes and names
class Student:
    def __init__(self, code, name, course_marks, exam_mark):
        self.code = code
        self.name = name
        self.course_marks = course_marks
        self.exam_mark = exam_mark
        self.total_coursework = sum(course_marks)
        self.total_score = self.total_coursework + exam_mark
        self.percentage = (self.total_score / 160) * 100
        self.grade = self.calculate_grade()

#This is for caculating the grades of the students and it will return the resutl after calculating how many points has the student got after the calculation
    def calculate_grade(self):
        if self.percentage >= 70: #shows when the overall is less than or equal to 70 and grades it an A
            return 'A'
        elif self.percentage >= 60: #shows when the overall is less than or equal to 60 and grades it a B
            return 'B'
        elif self.percentage >= 50: #shows when the overall is less than  or equal to 50 and grades it a C
            return 'C'
        elif self.percentage >= 40: #shows when the overall is less than or equal to 40 and grades it a D
            return 'D'
        else:
            return 'F' #if all those overalls have never exceeded above 40 it will all result to F
        
#This will display after every data is inputted and calculated after every calculation
    def to_string(self):
        return f"{self.name} ({self.code}): Total Coursework={self.total_coursework}, Exam={self.exam_mark}, Overall %={self.percentage:.2f}%, Grade={self.grade}"


#This shows the name of the program when running the program
class StudentManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.students = []
        self.load_data()

        # This is for displaying the menus with all the options labelled with the corressponding rows and coloumns which will display in the right layout
        menu_frame = tk.Frame(root)
        menu_frame.pack()
        tk.Button(menu_frame, text="View All Records", command=self.view_all_records).grid(row=0, column=0)
        tk.Button(menu_frame, text="View Individual Record", command=self.view_individual_record).grid(row=0, column=1)
        tk.Button(menu_frame, text="Highest Total Score", command=self.show_highest_score).grid(row=0, column=2)
        tk.Button(menu_frame, text="Lowest Total Score", command=self.show_lowest_score).grid(row=0, column=3)
        tk.Button(menu_frame, text="Sort Records", command=self.sort_records).grid(row=1, column=0)
        tk.Button(menu_frame, text="Add Record", command=self.add_record).grid(row=1, column=1)
        tk.Button(menu_frame, text="Delete Record", command=self.delete_record).grid(row=1, column=2)
        tk.Button(menu_frame, text="Update Record", command=self.update_record).grid(row=1, column=3)
        
        # This will show the result of the calculations and display them in the bottom half of the window and it will be displayed on a list where it can show added records and previous student records also can add update records
        self.result_text = tk.Text(root, height=15, width=80)
        self.result_text.pack()
        
        # This will load and check the data inside the studentMarks.txt file
    def load_data(self):
        if not os.path.exists("studentMarks.txt"):
            with open("studentMarks.txt", "w") as file:
                file.write("0\n")  # This will make the student count to zero unless being added to the manager manually
            messagebox.showinfo("File Created", "The file 'studentMarks.txt' was created.")
            return
        
        #With the studentMarks.txt file open and created it will read the lines from these different critereas.
        with open("studentMarks.txt", "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.strip().split(',')
                code = int(parts[0])
                name = parts[1]
                course_marks = list(map(int, parts[2:5]))
                exam_mark = int(parts[5])
                student = Student(code, name, course_marks, exam_mark)
                self.students.append(student)
    
    #This will help save the data when saving for the student file in the program and it will write through the following critereas
    def save_data(self):
        with open("studentMarks.txt", "w") as file:
            file.write(f"{len(self.students)}\n")
            for student in self.students:
                file.write(f"{student.code},{student.name},{','.join(map(str, student.course_marks))},{student.exam_mark}\n")


    #This is used when writing off the marks for the student when inserted and now displayed
    def display_students(self, students):
        self.result_text.delete(1.0, tk.END)
        total_percentage = 0
        for student in students:
            self.result_text.insert(tk.END, student.to_string() + "\n")
            total_percentage += student.percentage
        average_percentage = total_percentage / len(students) if students else 0
        self.result_text.insert(tk.END, f"\nTotal Students: {len(students)}, Average Percentage: {average_percentage:.2f}%")


    #This function will view all the records of the students that where inserted within the manager
    def view_all_records(self):
        self.display_students(self.students)
    
    
    #This function will view all the records of individual students
    def view_individual_record(self):
        selected_name = simpledialog.askstring("Input", "Enter student's name:") #Input by user to type the user's name to track a specific person's marks
        found_student = next((s for s in self.students if s.name == selected_name), None)
        if found_student:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, found_student.to_string()) #If student name was found it will display the student's marks
        else:
            messagebox.showinfo("Not Found", "Student not found.") #If the student wasn't found it will display this error message that says 'Student not found'


    #This function will show the student with the highest marks on the list 
    def show_highest_score(self):
        if not self.students:
            messagebox.showinfo("No Data", "No student data available.") #If the data is not available it will simply display this text box saying "No student dsts available" when there is no data available
            return
        highest_student = max(self.students, key=lambda s: s.total_score)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Highest Score:\n" + highest_student.to_string())

    def show_lowest_score(self):
        if not self.students:
            messagebox.showinfo("No Data", "No student data available.") #It also haas the same function as the highest scoring student when displaying the lowest rated score in the student manager
            return
        lowest_student = min(self.students, key=lambda s: s.total_score)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Lowest Score:\n" + lowest_student.to_string())
        
        
    #This is used for sorting students in order
    def sort_records(self):
        order = simpledialog.askstring("Input", "Enter 'asc' for ascending or 'desc' for descending:") #These are input prompts provided if the user wants to rank it in ascending order or descending order
        #This checks whether or not the inputted commands are exactly as as they are in the prompt
        if order.lower() == 'asc':
            self.students.sort(key=lambda s: s.total_score)
        elif order.lower() == 'desc':
            self.students.sort(key=lambda s: s.total_score, reverse=True)
        #if neither typed in 'asc' or 'desc' when promted to it will display this error message
        else:
            messagebox.showerror("Invalid Input", "Please enter 'asc' or 'desc'.")
            return
        self.display_students(self.students)


    #This will allow the user to input the necessary data needed for the manager to read, input to the text file, and display.
    def add_record(self):
        code = simpledialog.askinteger("Input", "Enter student code:")
        name = simpledialog.askstring("Input", "Enter student's name:")
        course_marks = [simpledialog.askinteger("Input", f"Enter course mark {i+1} (out of 20):") for i in range(3)]
        exam_mark = simpledialog.askinteger("Input", "Enter exam mark (out of 100):")
        new_student = Student(code, name, course_marks, exam_mark)
        self.students.append(new_student)
        self.save_data()
        self.view_all_records()
    
    #This function will delete the record in the manager by using the code that the user inserted in the manager. It also checks whether or not the code is inside the list of the student manager
    def delete_record(self):
        code = simpledialog.askinteger("Input", "Enter student code to delete:") #User prompt for putting in the code of the student code for the record of the student that the user wants to delete
        self.students = [s for s in self.students if s.code != code]
        self.save_data()
        self.view_all_records()


    #This function will update the record of the current student and will overwrite the prevoius record from the student manager.
    def update_record(self):
        code = simpledialog.askinteger("Input", "Enter student code to update:") #prompts the user to input the code inside the manager 
        student = next((s for s in self.students if s.code == code), None)
        if student:
            field = simpledialog.askstring("Input", "Enter field to update (name, mark1, mark2, mark3, exam):") #prompts the user to input the name, mark 1, mark 2, mark 3, and exam data for updating
            if field == "name":
                student.name = simpledialog.askstring("Input", "Enter new name:") #prompts user to put a new name for the student record
            elif field in ["mark1", "mark2", "mark3", "exam"]:
                new_mark = simpledialog.askinteger("Input", f"Enter new value for {field}:") #This is used to insert the new data and replace the old data in the student manager
                if field == "mark1":
                    student.course_marks[0] = new_mark
                elif field == "mark2":
                    student.course_marks[1] = new_mark
                elif field == "mark3":
                    student.course_marks[2] = new_mark
                elif field == "exam":
                    student.exam_mark = new_mark
                student.total_coursework = sum(student.course_marks)
                student.total_score = student.total_coursework + student.exam_mark
                student.percentage = (student.total_score / 160) * 100
                student.grade = student.calculate_grade()
            else:
                messagebox.showerror("Invalid Field", "Invalid field selected.") #if some of the inputs are invalid this will pop up as an error message in the screen
            self.save_data()
            self.view_all_records()
        else:
            messagebox.showinfo("Not Found", "Student not found.") #If the student is not found in the manager it will show this error message 

if __name__ == "__main__":
    
    #The last step whenever the code needs to run
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()
