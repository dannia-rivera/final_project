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
            if name in self.candidate_names:
                messagebox.showerror("Error", "{name} has been used before. Try using a different name.")
                return
        self.canidate_names.extend(names)
        self.generate_candidates

    def generate_candidates(self):
        '''Generate the random candidates form the entered names.'''
        if not self.candidate_names:
            messagebox.showerror("Error", "No candidate names available")
            return

        random.shuffle(self.candidate_names)
        num_names = random.randint(2, min(5, len(self.candidate_names)))
        selected_names = self.cadidate_names[:num_names]

        for name in selected_names:
            candidate = Candidate(name)
            self.vote_system.candidates.append(candidate)

        num_rows = (len(selected_names) + 1) // 2
        for i in range(num_rows):
            row_frame = tk.Frame(self.main_frame, bg="#F0F0F0")
            row_frame.pack(fill=tk.X)
            for j in range(2):
                index = i*2 + j
                if index < len(selected_names):
                    candidate = self.vote_system.candidates[index]
                    button = tk.Button(row_frame, text=candidate.name, command=lambda c=candidate: self.vote(c), bg="#007ACC", fg="white", font=("helvetica", 10, "bold"), relief=tk.FLAT)
                    button.pack(side=tk.LEFT, padx=5, pady=5)

    def vote(self, candidate: Candidate):
        '''Vote for the selected candidate'''
        messagebox.showinfo("Success", f'You have voted for {candidate.name}!')
        candidate.vote()
        self.previous_votes.append(candidate.name)

    def restart_voting(self):
        '''Restart the voting process'''
        self.previous_votes = []
        self.destroy()
        app = VotingApp(input_mode=self.input_mode, candidate_names=self.candidate_names, main_menu=self.main_menu)
        app.mainloop()

    def back_to_menu(self):
        '''Again would destroy current window and the main menu would pop up'''
        self.destroy()
        import main
        app = main.MainScreen()
        app.mainloop()

    def show_scoreboard(self):
        '''Show the scoreboard'''

        if not self.vote_system.candidates:
            messagebox.showinfo("Scoreboard", "No votes recorded yet")
            return

        scoreboard_window = tk.Toplevel(self)
        scoreboard_window.title("Scoreboard")
        scoreboard_window.geometry("300x200")
        scoreboard_window.configure(bg="#F0F0F0")

        scoreboard_frame = tk.Frame(scoreboard_window, bg="#F0F0F0")
        scoreboard_frame.pack(expand=True, fill=tk.BOTH)

        for idx, candidate in enumerate(self.vote_system.candidates, 1):
            label = tk.Label(scoreboard_frame, text=f"{idx}. {candidate.name}: {candidate.votes} votes", bg="#F0F0F0", font=("Helvetica", 10))
            label.pack()


if __name__ == "__main__":
    app = VotingApp()
    app.mainloop()