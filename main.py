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

        self.main_frame = tk.Frame(self, bg"#F0F0F0")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.create_widgets()

    def set_main_menu(self, main_menu):
