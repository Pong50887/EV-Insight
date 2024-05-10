import tkinter as tk
import webbrowser
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
        self.current_text = self.search.get_defaut_data()
        self.old_rate = 1
        self.main_menu()

    def main_menu(self):
        self.geometry('1000x700')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.configure(background="#BDBDBD")
        """ The function for display main menu """

        # Create Label Select Menu
        tk.Label(self, text="Select Menu", font=("Arial", 36, "bold"),
                 background="#333333", foreground="#ffffff",
                 borderwidth=10).\
            grid(row=0, column=0, columnspan=4, pady=20, sticky="EW")

        # Create Button to swift to function Insight
        tk.Button(self, text="EV insight",
                  relief="flat", width=20, height=2, command=self.switch_insight_menu,
                  font=("Arial", 14), background="#4CAF50", foreground="#ffffff").\
            grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

        # Create Button to swift to function Compare price
        tk.Button(self, text="Compare EV cars",
                  relief="flat", width=20, height=2, command=self.swift_compare_menu,
                  font=("Arial", 14), background="#FFC107", foreground="#ffffff").\
            grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

        # Create Button to swift to function Show statistic
        tk.Button(self, text="Show Statistic of data",
                  relief="flat", width=20, height=2, command=self.swift_stat_menu,
                  font=("Arial", 14), background="#2196F3", foreground="#ffffff").\
            grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

        # Create Button to quit App
        tk.Button(self, text="Quit",
                  relief="flat", width=20, height=2, command=self.quit,
                  font=("Arial", 14), background="#F44336", foreground="#ffffff").\
            grid(row=2, column=1, padx=10, pady=10, sticky="NSEW")

    def insight_menu(self):
        self.geometry('1250x650')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.configure(background="#E2D5F5")
        """ The function for insight main menu """

        tk.Button(self, text='Cheapest', width=20, height=2, command=self.button_cheapest,
                  relief="flat", font=("fantasy", 11), background="#42CCC9", foreground="#FFFFFF"). \
            grid(row=0, column=0, padx=10, pady=10)

        tk.Button(self, text='Fast Charge', width=20, height=2, command=self.button_fast_charge,
                  relief="flat", font=("fantasy", 11), background="#4C99CF", foreground="#FFFFFF") \
            .grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self, text='Most Efficient', width=20, height=2, command=self.button_most_efficient,
                  relief="flat", font=("fantasy", 11), background="#4873A6", foreground="#FFFFFF") \
            .grid(row=0, column=2, padx=10, pady=10)

        tk.Button(self, text='Longest Range', width=20, height=2, command=self.button_longest_range,
                  relief="flat", font=("fantasy", 11), background="#5A5388", foreground="#FFFFFF") \
            .grid(row=0, column=3, padx=10, pady=10)

        tk.Label(self, text='Change Price', width=10, height=2, background="#E2D5F5",
                 relief="flat", font=("fantasy", 15), foreground="#524364") \
            .grid(row=0, column=4, padx=10, pady=10)

        self.combo_price = ttk.Combobox(self, width=20, height=10, values=self.currency.get_currency_names())
        self.combo_price.grid(row=0, column=5, padx=10, pady=10)
        self.combo_price.bind("<<ComboboxSelected>>", self.combobox_clicked)
        self.combo_price.current(0)

        tk.Label(self, text='Search Car name', width=15, height=1, background="#E2D5F5",
                 relief="flat", font=("fantasy", 15), foreground="#524364") \
            .grid(row=1, column=0, pady=10)

        self.Entry_search = tk.Entry(self, width=20)
        self.Entry_search.grid(row=1, column=1, columnspan=4, sticky="EW")

        tk.Button(self, text='Search', width=20, height=1, font=("fantasy", 10),
                  relief="flat",background="#56426A", foreground="#FFFFFF", command=lambda: self.button_search()) \
            .grid(row=1, column=5, padx=(30, 0), pady=10)

        # SHOW ALL DATA
        self.treeview = ttk.Treeview()
        self.treeview.grid(row=2, columnspan=6, padx=(10, 0), sticky="NSEW")
        self.update_databox(self.search.get_defaut_data())
        self.treeview.bind("<Double-1>", self.on_double_click)
        self.treeview.configure(height=20)

        self.scrollbar = ttk.Scrollbar(orient="vertical", command=self.treeview.yview)
        self.scrollbar.grid(row=2, column=6, padx=(0, 10), sticky='ns')
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  font=("fantasy", 11), background="#91A486", foreground="#FFFFFF",  command=self.switch_main_menu) \
            .grid(row=3, columnspan=5, padx=10, pady=10)

        tk.Button(self, text='Reset', width=20, height=2,
                  relief="flat", font=("fantasy", 11), background="#C49346", foreground="#FFFFFF", command=self.reset) \
            .grid(row=3, column=5, padx=10, pady=10)

    def on_double_click(self, event):
        item = self.treeview.selection()[0]
        car_name = self.treeview.item(item, "values")[1]  # Assuming the car name is in the second column
        link = self.search.get_link_from_csv(car_name)
        webbrowser.open_new_tab(link)

    def reset(self):
        self.update_databox(self.search.get_defaut_data())
        self.combo_price.current(0)
        self.search.reset_mainframe()
        self.old_rate = 1

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
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        columns = list(data.columns)
        self.treeview['columns'] = columns
        self.treeview.column("#0", width=0, stretch=tk.NO)
        for col in columns:
            self.treeview.column(col, anchor=tk.W, width=120)
            self.treeview.heading(col, text=col, anchor=tk.W)
        for index, row in data.iterrows():
            self.treeview.insert("", tk.END, values=list(row))

    def compare_menu(self):
        self.geometry('1600x700')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.configure(background="#E2D5F5")
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
                  font=("fantasy", 11), background="#91A486", foreground="#FFFFFF",
                  command=self.switch_main_menu) \
            .grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Plot graph
    def car_clicked(self, event):
        if self.car1.get() and self.car2.get():
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
        self.geometry('1000x700')
        self.configure(background="#E2D5F5")
        """ The function for create statistic menu """

        tk.Label(self, text="Statistic of Data", font=("Helvetica", 20),
                 background="#bae8e8", foreground="black",
                 borderwidth=20, highlightthickness=2). \
            grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="EW")

        # Create Button to swift to main menu
        tk.Button(self, text="Go back to Main Menu",
                  relief="flat", width=20, height=2,
                  font=("fantasy", 11), background="#91A486", foreground="#FFFFFF",
                  command=self.switch_main_menu) \
            .grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")

        self.GraphPlot.plot_histogram("Price.DE.").get_tk_widget(). \
            grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

        self.GraphPlot.plot_correlation().get_tk_widget(). \
            grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

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