import tkinter as tk
from tkinter import messagebox
import random
from vote_counter import Candidate, VoteSystem

def back_to_main_menu(root):
    '''Destroy the current window and show the main menu window'''
    root.destroy()
    root.main_menu.deiconify()
    root.main_menu.lift()