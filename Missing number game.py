import tkinter as tk
from tkinter import messagebox
import random

class MissingNumberGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Find the Missing Number Game")
        self.window.attributes('-fullscreen', True)

        self.sequence_length = 10
        self.life_points = 4
        self.timer_running = False

        self.create_widgets()
        self.generate_sequence()
        self.start_timer()

    def create_widgets(self):
        self.label_instruction = tk.Label(self.window, text="Find the Missing Number in the sequence:", font=("Arial", 24))
        self.label_instruction.pack(pady=20)

        self.label_sequence = tk.Label(self.window, text="", font=("Arial", 24))
        self.label_sequence.pack(pady=20)

        self.entry_guess = tk.Entry(self.window, font=("Arial", 24))
        self.entry_guess.pack(pady=20)

        self.button_guess = tk.Button(self.window, text="Guess", command=self.check_guess, font=("Arial", 24))
        self.button_guess.pack(pady=20)

        self.label_life_points = tk.Label(self.window, text=f"Life Points: {self.life_points}", font=("Arial", 24))
        self.label_life_points.pack(pady=20)

        self.label_timer = tk.Label(self.window, text="", font=("Arial", 24))
        self.label_timer.pack(pady=20)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart_game, font=("Arial", 24))
        self.restart_button.pack(pady=20)

    def generate_sequence(self):
        self.missing_number = random.randint(1, self.sequence_length)
        sequence = [str(i) for i in range(1, self.sequence_length + 1) if i != self.missing_number]
        random.shuffle(sequence)
        self.sequence_str = " ".join(sequence)
        self.label_sequence.config(text=self.sequence_str)

    def start_timer(self):
        self.timer_running = True
        self.remaining_time = 6  # 3 seconds

        def update_timer():
            self.remaining_time -= 1
            self.label_timer.config(text=f"Time Left: {self.remaining_time}")
            if self.remaining_time <= 0:
                self.timer_running = False
                self.label_timer.config(text="Too slow, Study Math")
                self.life_points -= 1
                self.label_life_points.config(text=f"Life Points: {self.life_points}")
                if self.life_points == 0:
                    messagebox.showinfo("Game Over", "Study Maths.")
                    self.restart_game()
            else:
                self.window.after(1000, update_timer)  # Update every 1 second

        update_timer()

    def check_guess(self):
        if not self.timer_running:
            messagebox.showinfo("Time's Up", "You ran out of time!")
            return

        guess = self.entry_guess.get()
        self.entry_guess.delete(0, tk.END)

        if guess.lower() == 'q':
            self.quit_game()
            return

        if not guess.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        guess = int(guess)

        if guess == self.missing_number:
            messagebox.showinfo("Congratulations", "You get chocolate!")
            self.restart_game()
        else:
            self.life_points -= 1
            self.label_life_points.config(text=f"Life Points: {self.life_points}")
            if self.life_points == 0:
                messagebox.showinfo("Game Over", "Study Maths.")
                self.restart_game()

    def quit_game(self):
        self.window.destroy()

    def restart_game(self):
        self.life_points = 4
        self.label_life_points.config(text=f"Life Points: {self.life_points}")
        self.generate_sequence()
        self.label_timer.config(text="")
        self.start_timer()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = MissingNumberGame()
    game.run()
