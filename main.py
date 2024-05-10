import tkinter
from tkinter import messagebox
from voting_app import VotingApp

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voting System")
        self.geometry("400x300")
        self.configure(bg="#F0F0F0")

        self.main_menu = None

