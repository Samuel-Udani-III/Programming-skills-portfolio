import tkinter as tk
import random
import os

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa, tell me a Joke")
        
        # This creates the joke file needed for this code to work
        self.create_jokes_file("randomJokes.txt")
        
        # Jokes are loaded from the .txt file and see the contents of the filled up file
        self.jokes = self.load_jokes("randomJokes.txt")
        
        # Label function so you can see the text in the window prompting the user to press the button
        self.setup_label = tk.Label(root, text="Press the button to hear a joke!", font=("Arial", 16))
        self.setup_label.pack(pady=10)
        
        # Button to make the program useable by presenting this button
        self.joke_button = tk.Button(root, text="Alexa, tell me a joke", font=("Arial", 14), command=self.show_setup)
        self.joke_button.pack(pady=10)
        
        # This button will reveal the punchline from the joke when pressed
        self.punchline_button = tk.Button(root, text="Show Punchline", font=("Arial", 14), command=self.show_punchline, state=tk.DISABLED)
        self.punchline_button.pack(pady=10)
        
        # So you can see the text file for the punchline after pressing the button
        self.punchline_label = tk.Label(root, text="", font=("Arial", 14))
        self.punchline_label.pack(pady=10)

    def create_jokes_file(self, file_path):
        # These are sample jokes inside the txt file after it was created. You can add and delete jokes and punchlines from here when needed
        if not os.path.exists(file_path):
            jokes = [
                "Why did the chicken cross the road?To get to the other side.",
                "What happens if you boil a clown?You get a laughing stock.",
                "Why did the scarecrow win an award?Because he was outstanding in his field.",
                "How does a penguin build its house?Igloos it together.",
                "Why don’t scientists trust atoms?Because they make up everything.",
                "What did the big flower say to the little flower?Hey, bud!",
                "Why do cows have hooves instead of feet?Because they lactose.",
                "What’s orange and sounds like a parrot?A carrot.",
                "Why did the bicycle fall over?Because it was two-tired.",
                "How do you organize a space party?You planet.",
                "Why don’t skeletons fight each other?They don’t have the guts.",
                "What kind of music do mummies listen to?Wrap music.",
                "How does a vampire start a letter?Tomb it may concern.",
                "What do you call fake spaghetti?An impasta.",
                "Why did the golfer bring two pairs of pants?In case he got a hole in one.",
                "Why was the math book sad?Because it had too many problems.",
                "What did one ocean say to the other ocean?Nothing, they just waved.",
                "Why can’t you give Elsa a balloon?Because she’ll let it go.",
                "What did the grape do when it got stepped on?It let out a little wine.",
                "Why did the tomato turn red?Because it saw the salad dressing."
            ]
            #The file path when reading the txt file is here. When the file path is wrong or the file is not created it will cause an erro when running
            with open(file_path, 'w') as file:
                for joke in jokes:
                    file.write(joke + "\n")
    #Loads jokes from the txt file from the path where it was created from
    def load_jokes(self, file_path):
        with open(file_path, 'r') as file:
            jokes = [line.strip().split('?') for line in file if '?' in line]
        return jokes
    #this shows the setup and pulls up random jokes from the list created in the file
    def show_setup(self):
        self.setup, self.punchline = random.choice(self.jokes)
        self.setup_label.config(text=self.setup + '?')
        self.punchline_label.config(text="")
        self.punchline_button.config(state=tk.NORMAL)
    #this shows the setup and pulls up the punchline from the specific joke when it was chosen
    def show_punchline(self):
        self.punchline_label.config(text=self.punchline)
        self.punchline_button.config(state=tk.DISABLED)

# So everything runs perfectly after making the code
root = tk.Tk()
app = JokeApp(root)
root.mainloop()
