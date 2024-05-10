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

        