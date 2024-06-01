import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result_label.config(text=f"User: {user_choice}\nComputer: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "Hey, it's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "Hurray!You won"
        score['user'] += 1
    else:
        result = "Oh no you lost!"
        score['computer'] += 1
        
    result_label.config(text=f"User: {user_choice}\nComputer: {computer_choice}\n{result}")
    score_label.config(text=f"Score - User: {score['user']}  Computer: {score['computer']}")
    
# Reset the game for another round
def reset_game():
    result_label.config(text="")
    play_again_button.pack_forget()

# Function to handle user choice
def user_choice(choice):
    play(choice)
    play_again_button.pack(pady=10)

# Initialize score
score = {'user': 0, 'computer': 0}

# Create the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and place widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

tk.Button(buttons_frame, text="Rock", command=lambda: user_choice("Rock")).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Paper", command=lambda: user_choice("Paper")).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Scissors", command=lambda: user_choice("Scissors")).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - User: 0  Computer: 0")
score_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", command=reset_game)

# Start the Tkinter main loop
root.mainloop()
