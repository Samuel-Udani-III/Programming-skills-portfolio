import tkinter as tk
import random

# Constants for the difficulty levels
LEVELS = {
    1: (1, 9),       # Easy has Single-digit numbers
    2: (10, 99),     # Moderate has Double-digit numbers
    3: (1000, 9999)  # Advanced has Four-digit numbers
}

# This is the main quiz class 
class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        self.score = 0
        self.question_count = 0
        self.current_answer = None
        self.attempts = 0
        self.difficulty = 1
        
        self.create_widgets()

    def create_widgets(self):
        # You can see the difficulty settings here 
        self.frame_menu = tk.Frame(self.root)
        tk.Label(self.frame_menu, text="Select Difficulty Level", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.frame_menu, text="1. Easy", command=lambda: self.start_quiz(1)).pack(pady=5)
        tk.Button(self.frame_menu, text="2. Moderate", command=lambda: self.start_quiz(2)).pack(pady=5)
        tk.Button(self.frame_menu, text="3. Advanced", command=lambda: self.start_quiz(3)).pack(pady=5)
        self.frame_menu.pack()

        # Layout of the quiz when started
        self.frame_quiz = tk.Frame(self.root)
        self.question_label = tk.Label(self.frame_quiz, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)
        self.answer_entry = tk.Entry(self.frame_quiz, font=("Arial", 16))
        self.answer_entry.pack(pady=10)
        self.submit_button = tk.Button(self.frame_quiz, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)
        self.feedback_label = tk.Label(self.frame_quiz, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        # Shows the test result after finishing the quest
        self.frame_results = tk.Frame(self.root)
        self.results_label = tk.Label(self.frame_results, text="", font=("Arial", 16))
        self.results_label.pack(pady=20)
        self.play_again_button = tk.Button(self.frame_results, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=5)
    
    #This starts the quiz    
    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.question_count = 0
        self.frame_menu.pack_forget()
        self.frame_results.pack_forget()
        self.frame_quiz.pack()
        self.next_question()

    #Thus will proceed to the next question and checks the difficulty and current answer 
    def next_question(self):
        if self.question_count >= 10:
            self.display_results()
            return
        self.question_count += 1
        self.attempts = 0
        num1, num2 = self.random_int(self.difficulty)
        operation = self.decide_operation()
        self.current_answer = num1 + num2 if operation == '+' else num1 - num2
        self.question_label.config(text=f"{num1} {operation} {num2} = ?")
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    
    def random_int(self, difficulty):
        min_val, max_val = LEVELS[difficulty]
        return random.randint(min_val, max_val), random.randint(min_val, max_val)

    def decide_operation(self):
        return random.choice(['+', '-'])

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.current_answer:
                self.give_feedback(True)
            else:
                self.give_feedback(False)
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number")

    def give_feedback(self, correct):
        if correct:
            points = 10 if self.attempts == 0 else 5
            self.score += points
            self.feedback_label.config(text="Correct! Moving to the next question.")
            self.root.after(1000, self.next_question)
        else:
            self.attempts += 1
            if self.attempts < 2:
                self.feedback_label.config(text="Incorrect. Try again.")
                self.answer_entry.delete(0, tk.END)
            else:
                self.feedback_label.config(text=f"Incorrect. The correct answer was {self.current_answer}.")
                self.root.after(1000, self.next_question)

    def display_results(self):
        self.frame_quiz.pack_forget()
        self.results_label.config(text=f"Your final score: {self.score}/100\nGrade: {self.get_grade()}")
        self.frame_results.pack()

    def get_grade(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "D"

    def reset_game(self):
        self.frame_results.pack_forget()
        self.frame_menu.pack()

# Run the Math Quiz Application
root = tk.Tk()
app = MathQuiz(root)
root.mainloop()
