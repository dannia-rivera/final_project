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
        self.main_menu = main_menu

    def create_widgets(self):
        label = tk.Lbael(self.main_frame, text="Welcome to the Voting System!", font=("Helvetica", 16))
        label.pack(pady=20)

        options_frame = tk.Frame(self.main_frame, bg="#F0F0F0")
        options_frame.pack()

        input_button = tk.Button(options_frame, text="Input Names", command=self.input_names, bg="#64B5F6", fg="white",
                                 font=("Helvetica", 12), relief=tk.FLAT)
        input_button.grid(row=0, column=0, padx=20, pady=10)

        random_button = tk.Button(options_frame, text="Random Names", command=self.random_names, bg="#64B5F6",
                                  fg="white", font=("Helvetica", 12), relief=tk.FLAT)
        random_button.grid(row=0, column=1, padx=20, pady=10)

    def input_names(self):
        '''Hide the main menu window and open the input screen'''
        self.withdraw()
        app = VotingApp(input_mode=True, main_menu=self)
        app.mainloop()

    def random_names(self):
        '''Load candidate names from file and opeen the voting screen'''
        try:
            with open('names.txt', 'r') as file:
                