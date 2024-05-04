import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt
from Search_data import Search
from conversion_rate import Conversion
import numpy as np
from GraphPlot import GraphPlot
"""This is a class App."""
class App(tk.Tk):
    def __init__(self):
        """
        This is a class to create main window.
        """
        super().__init__()
        self.title('EV insight')
        self.configure(bg="#DDDDDD")
        self.search = Search()
        self.currency = Conversion()
        self.GraphPlot = GraphPlot(self)
        self.resizable(False, False)
        self.current_text = self.search.get_defaut_data()
        self.old_rate = 1
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
                  relief="flat", width=20, height=2, command=self.switch_insight_menu).\
            grid(row=1, column=0, padx=10, pady=10, sticky="EW")

        # Create Button to swift to function Compare price
        tk.Button(self, text="Compare EV cars",
                  relief="flat", width=20, height=2, command=self.swift_compare_menu). \
            grid(row=1, column=1, padx=10, pady=10, sticky="EW")

        # Create Button to swift to function Show statistic
        tk.Button(self, text="Show Statistic of data",
                  relief="flat", width=20, height=2, command=self.swift_stat_menu). \
            grid(row=2, column=0, padx=10, pady=10, sticky="EW")

        # Create Button to swift to quit App
        tk.Button(self, text="Quit",
                  relief="flat", width=20, height=2, command=self.quit). \
            grid(row=2, column=1, padx=10, pady=10, sticky="SEW")

    def insight_menu(self):
        self.geometry('1250x600')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        """ The function for estimate main menu """

        tk.Button(self, text='Cheapest', width=20, height=2, command=self.button_cheapest). \
            grid(row=0, column=0, padx=10, pady=10)

        tk.Button(self, text='Fast Charge', width=20, height=2, command=self.button_fast_charge) \
            .grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self, text='Most Efficient', width=20, height=2, command=self.button_most_efficient) \
            .grid(row=0, column=2, padx=10, pady=10)

        tk.Button(self, text='Longest Range', width=20, height=2, command=self.button_longest_range) \
            .grid(row=0, column=3, padx=10, pady=10)

        tk.Label(self, text='Change Price', width=10, height=2, background="#DDDDDD") \
            .grid(row=0, column=4, padx=10, pady=10)

        self.combo_price = ttk.Combobox(self, width=20, height=10, values=self.currency.get_currency_names())
        self.combo_price.grid(row=0, column=5, padx=10, pady=10)
        self.combo_price.bind("<<ComboboxSelected>>", self.combobox_clicked)
        self.combo_price.current(0)

        tk.Label(self, text='Search Car name', width=15, height=1, background="#DDDDDD") \
            .grid(row=1, column=0, pady=10)

        self.Entry_search = tk.Entry(self, width=20)
        self.Entry_search.grid(row=1, column=1, columnspan=4, sticky="EW")

        tk.Button(self, text='Search', width=20, height=1, command=lambda: self.button_search()) \
            .grid(row=1, column=5, padx=10, pady=10)

        # SHOW ALL DATA
        self.databox = tk.Text(self, width=50, height=20)
        self.databox.grid(row=2, columnspan=6, padx=10, pady=10, sticky="SEW")
        self.databox.config(state=tk.DISABLED)
        self.update_databox(self.search.get_defaut_data())

        tk.Button(self, text='Back to Main Menu', width=20, height=2, command=self.switch_main_menu) \
            .grid(row=3, columnspan=5, padx=10, pady=10)

        tk.Button(self, text='Reset', width=20, height=2, command=self.reset) \
            .grid(row=3, column=5, padx=10, pady=10)

    def reset(self):
        self.update_databox(self.search.get_defaut_data())
        self.combo_price.current(0)

    def combobox_clicked(self, event):
        conversion_rate = self.currency.get_conversion(self.combo_price.get())
        updated_price = self.search.get_price(conversion_rate, self.old_rate)
        self.old_rate = conversion_rate
        self.update_databox(updated_price)

    def button_search(self):
        if self.Entry_search.get().lower():
            update_txt = self.search.search_data(self.Entry_search.get().lower())
            self.update_databox(update_txt)
        else:
            messagebox.showwarning("Search", "Please enter a Car name.")

    def button_most_efficient(self):
        efficient = self.search.search_most_efficient()
        self.update_databox(efficient)

    def button_longest_range(self):
        longest = self.search.search_longest_range()
        self.update_databox(longest)

    def button_cheapest(self):
        cheapest = self.search.search_cheapest()
        self.update_databox(cheapest)

    def button_fast_charge(self):
        fast_charge = self.search.search_fast_charge()
        self.update_databox(fast_charge)

    def update_databox(self, data):
        self.databox.config(state=tk.NORMAL)
        self.databox.delete("1.0", tk.END)
        self.current_text = data
        self.databox.insert(tk.END, data)
        self.databox.config(state=tk.DISABLED)

    def compare_menu(self):
        self.geometry('1800x700')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        default1 = tk.StringVar(value='---')
        default2 = tk.StringVar(value='---')

        """ The function for display compare menu """

        # Create Combobox to select car
        self.car1 = ttk.Combobox(self, textvariable=default1, values=self.search.get_car_name_list())
        self.car1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")
        self.car1.bind("<<ComboboxSelected>>", self.car_clicked)
        self.car2 = ttk.Combobox(self, textvariable=default2, values=self.search.get_car_name_list())
        self.car2.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="NSEW")
        self.car2.bind("<<ComboboxSelected>>", self.car_clicked)

        # Create Label to show what car be selected
        tk.Label(self, textvariable=default1, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2). \
            grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="EW")
        tk.Label(self, textvariable=default2, font=("Helvetica", 20),
                 background="#F6FFDE", foreground="black",
                 borderwidth=10, highlightthickness=2). \
            grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  command=self.switch_main_menu) \
            .grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")
        # Plot graph

    def car_clicked(self, event):
        if not self.car1.get() or self.car2.get():
            self.GraphPlot.plot_price_comparison(self.car1.get(),
                                                 self.car2.get()).get_tk_widget(). \
                grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")
            self.GraphPlot.plot_battery_comparison(self.car1.get(),
                                                 self.car2.get()).get_tk_widget(). \
                grid(row=2, column=1, padx=10, pady=10, sticky="NSEW")
            self.GraphPlot.plot_charge_comparison(self.car1.get(),
                                                 self.car2.get()).get_tk_widget(). \
                grid(row=2, column=2, padx=10, pady=10, sticky="NSEW")
            self.GraphPlot.plot_range_comparison(self.car1.get(),
                                                   self.car2.get()).get_tk_widget(). \
                grid(row=2, column=3, padx=10, pady=10, sticky="NSEW")
            self.GraphPlot.plot_top_speed_comparison(self.car1.get(),
                                                 self.car2.get()).get_tk_widget(). \
                grid(row=3, column=0, padx=10, pady=10, sticky="NSEW")
            self.GraphPlot.plot_acceleration_comparison(self.car1.get(),
                                                   self.car2.get()).get_tk_widget(). \
                grid(row=3, column=1, padx=10, pady=10, sticky="NSEW")
            self.GraphPlot.plot_efficiency_comparison(self.car1.get(),
                                                        self.car2.get()).get_tk_widget(). \
                grid(row=3, column=2, padx=10, pady=10, sticky="NSEW")

    def stat_menu(self):
        """ The function for create statistic menu """

        tk.Label(self, text="Statistic of Data", font=("Helvetica", 20),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2). \
            grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  command=self.switch_main_menu) \
            .grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        self.GraphPlot.plot_histogram("Price.DE.").get_tk_widget(). \
            grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

        self.GraphPlot.plot_correlation().get_tk_widget(). \
            grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

        # # Describe Histogram
        # tk.Label(self, text="Mean : 6412613.17 | Std : 5027061.92 |"
        #                     " Min : 110000.00 | Max : 28907325.00",
        #          font=("Helvetica", 9),
        #          background="#bae8e8", foreground="black",
        #          borderwidth=5, highlightthickness=2). \
        #     grid(row=2, column=0, columnspan=2, padx=10, sticky="EW")
        #
        # # Describe Bar graph
        # tk.Label(self, text="The most expensive type of is "
        #                     "Detected House, followed by Townhouse, Land, "
        #                     "and Condo respectively.",
        #          font=("Helvetica", 9),
        #          background="#bae8e8", foreground="black",
        #          borderwidth=5, highlightthickness=2). \
        #     grid(row=2, column=2, columnspan=2, padx=10, sticky="EW")
        #
        # # Create Button to swift to main menu
        # tk.Button(self, text="Go back to Main Menu",
        #           relief="flat", width=20, height=2,
        #           command=self.swift_main_menu) \
        #     .grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

    def switch_main_menu(self):
        """ The function for swift to main menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.main_menu()

    def switch_insight_menu(self):
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

    def swift_stat_menu(self):
        """ The function for swift to compare menu """
        for widget in self.winfo_children():
            widget.destroy()
            plt.close('all')
        self.stat_menu()


if __name__ == "__main__":
    app = App()
    app.mainloop()