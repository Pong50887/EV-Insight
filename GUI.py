import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib import pyplot as plt


"""This is a class App."""
class App(tk.Tk):
    def __init__(self):
        """
        This is a class to create main window.
        """
        super().__init__()
        self.title('EV insight')
        self.configure(bg="#DDDDDD")
        self.resizable(False, False)
        self.main_menu()

    def main_menu(self):
        self.geometry('1000x700')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        """ The function for display main menu """

        # Create Label Select Menu
        tk.Label(self, text="Select Menu", font=("Helvetica", 48),
                 background="#767676", foreground="#fcfcfc",
                 borderwidth=20).\
            grid(row=0, column=0, columnspan=4, pady=10, sticky="EW")

        # Create Button to swift to function Insight
        tk.Button(self, text="EV insight",
                  relief="flat", width=20, height=2, command=self.switch_estimate_menu).\
            grid(row=1, column=0, padx=10, pady=10, sticky="EW")

        # Create Button to swift to function Compare price
        tk.Button(self, text="Compare EV cars",
                  relief="flat", width=20, height=2, command=self.swift_compare_menu). \
            grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        # Create Button to swift to function Show statistic
        tk.Button(self, text="Show Statistic of data",
                  relief="flat", width=20, height=2). \
            grid(row=2, column=0, padx=10, pady=10, sticky="EW")

        # Create Button to swift to quit App
        tk.Button(self, text="Quit",
                  relief="flat", width=20, height=2). \
            grid(row=2, column=1, padx=10, pady=10, sticky="SEW")

    def insight_menu(self):
        self.geometry('1000x600')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        """ The function for estimate main menu """

        # Create land type button
        tk.Button(self, text='Cheapest', width=20, height=2). \
            grid(row=0, column=0, padx=10, pady=10)

        # Create condo type button
        tk.Button(self, text='Fast Charge', width=20, height=2,) \
            .grid(row=0, column=1, padx=10, pady=10)

        # Create house type button
        tk.Button(self, text='Most Efficient', width=20, height=2,) \
            .grid(row=0, column=2, padx=10, pady=10)

        # Create townhouse type button
        tk.Button(self, text='Longest Range', width=20, height=2,) \
            .grid(row=0, column=3, padx=10, pady=10)

        tk.Text(self, width=20, height=1). \
            grid(row=1, columnspan=3, padx=10, pady=10, sticky="SEW")

        tk.Button(self, text='Search', width=20, height=2, ) \
            .grid(row=1, column=3, padx=10, pady=10)

        tk.Text(self, width=20, height=20). \
            grid(row=2, columnspan=4, padx=10, pady=10, sticky="SEW")

        tk.Button(self, text='Back to Main Menu', width=20, height=2, command=self.switch_main_menu) \
            .grid(row=3, columnspan=4, padx=10, pady=10)

    def compare_menu(self):
        self.geometry('1000x700')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        """ The function for display compare menu """

        # Create Combobox to select city
        ttk.Combobox(self). \
            grid(row=1, column=0, padx=10, pady=10, sticky="EW")
        ttk.Combobox(self). \
            grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        # Create Label to show what city be selected
        tk.Label(self, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2). \
            grid(row=0, column=0, padx=10, pady=10, sticky="EW")
        tk.Label(self, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2). \
            grid(row=0, column=1, padx=10, pady=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  command=self.switch_main_menu) \
            .grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

    def switch_main_menu(self):
        """ The function for swift to main menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.main_menu()

    def switch_estimate_menu(self):
        """ The function for swift to estimate menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.insight_menu()

    def swift_compare_menu(self):
        """ The function for swift to compare menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.compare_menu()


if __name__ == "__main__":
    app = App()
    app.mainloop()
