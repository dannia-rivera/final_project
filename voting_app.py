import tkinter as tk
from tkinter import messagebox
import random
from vote_counter import Candidate, VoteSystem

def back_to_main_menu(root):
    '''Destroy the current window and show the main menu window'''
    root.destroy()
    root.main_menu.deiconify()
    root.main_menu.lift()

class VotingApp(tk.Tk):
    def __init__(self, input_mode=True, candidate_names=None, main_menu=None):
        super().__init__()
        self.title("Voting System")
        self.geometry("400x300")
        self.configure(bg="#F0F0F0")

        self.input_mode = input_mode
        self.vote_system = VoteSystem()
        self.previous_votes = []
        self.candidate_names = candidate_names if candidate_names is not None else []
        self.main_menu = main_menu  # Store a reference to the main menu window

        self.main_frame = tk.Frame(self, bg="#F0F0F0")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        if self.input_mode:
            self.create_input_screen()
        else:
            self.generate_candidates()

        restart_button = tk.Button(self.main_frame, text="Restart", command=self.restart_voting, bg="#007ACC",
                                   fg="white", font=("Helvetica", 10, "bold"), relief=tk.FLAT)
        restart_button.pack(pady=10)

        back_button = tk.Button(self.main_frame, text="Back to Main Menu", command=self.back_to_menu, bg="#007ACC",
                                fg="white", font=("Helvetica", 10, "bold"), relief=tk.FLAT)
        back_button.pack(pady=5)

        self.scoreboard_button = tk.Button(self.main_frame, text="Show Scoreboard", command=self.show_scoreboard,
                                           bg="#007ACC", fg="white", font=("Helvetica", 10, "bold"), relief=tk.FLAT)
        self.scoreboard_button.pack(pady=5)

    def create_input_screen(self):
        '''Create the input screen for entering Candidate names'''
        label = tk.Label(self.main_frame, text="Enter candidate names (separated by commas):", bg="#F0F0F0", font=("Helvetica", 10))
        label.pack(pady=10)

        self.entry = tk.Entry(self.main_frame, font=("Helvetica", 10))
        self.entry.pack(pady=5)

        submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_names, bg="#007ACC", fg="white", font=("Helvetica", 10, "bold"), relief=tk.FLAT)
        submit_button.pack(pady=5)

    def submit_names(self):
        '''Submit the entered candidate names'''
        names = self.entry.get().split(',')
        if not (2<= len(names) <=5):
            messagebox.showerror("Error", "Please enter 2-5 names seperated by commas.")
            return
        for name in names:
            if name in self,candidate_names:
                messagebox.showerror("Error", "{name} has been used before. Try using a different name.")
                return
        self.canidate_names.extend(names)
        self.generate_candidates()

    def generate_candidates(self):
        '''Generate the random candidates form the entered names.'''
