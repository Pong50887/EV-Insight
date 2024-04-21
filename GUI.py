import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt


"""This is a class App."""
class App(tk.Tk):
    def __init__(self):
        """
        This is a class to create main window.

        Attributes:
            estimate (Estimate): Estimate Class.
            graph_plot (GraphPlot): GraphPlot Class.
        """
        super().__init__()
        self.title('Bangkok Real-Estate')
        self.geometry('1000x700')
        self.configure(bg="#DDDDDD")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.main_menu()

    def main_menu(self):
        """ The function for display main menu """

        # Create Label Select Menu
        tk.Label(self, text="Select Menu", font=("Helvetica", 48),
                 background="#767676", foreground="#fcfcfc",
                 borderwidth=20).\
            grid(row=0, column=0, columnspan=4, pady=10, sticky="EW")

        # Create Button to swift to function Insight
        tk.Button(self, text="EV insight",
                  relief="flat", width=20, height=2).\
            grid(row=1, column=0, padx=10, pady=10, sticky="EW")

        # Create Button to swift to function Compare price
        tk.Button(self, text="Compare EV cars",
                  relief="flat", width=20, height=2). \
            grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        # Create Button to swift to function Show statistic
        tk.Button(self, text="Show Statistic of data",
                  relief="flat", width=20, height=2). \
            grid(row=2, column=0, padx=10, pady=10, sticky="EW")

        # Create Button to swift to quit App
        tk.Button(self, text="Quit",
                  relief="flat", width=20, height=2). \
            grid(row=2, column=1, padx=10, pady=10, sticky="SEW")


if __name__ == "__main__":
    app = App()
    app.mainloop()
