import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from read_data import Data
import seaborn as sns


class GraphPlot:
    """
    This is a class to create widget of graph.

    Attributes:
        parent (str): root of graph.
        data (Data): Data to store information of EV_car
        dataframe (dataframe) : Dataframe of data.
    """

    def __init__(self, parent):
        """
        The constructor for GraphPlot class.
        """
        self.parent = parent
        self.data = Data()
        self.dataframe = self.data.get_data()

    def plot_histogram(self, selected_var):
        """The function for create histogram widget."""
        plt.close('all')
        fig_hist, ax_hist = plt.subplots()
        sns.histplot(self.dataframe[selected_var], ax=ax_hist)
        ax_hist.set_xlabel(selected_var)
        ax_hist.set_ylabel("Frequency")
        ax_hist.set_title("Histogram of " + selected_var)
        histogram_widget = FigureCanvasTkAgg(fig_hist, master=self.parent)
        return histogram_widget

    def plot_price(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['Price.DE.'].values[0]
        car2_price = car2_data['Price.DE.'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=5)
        ax.set_ylabel('Price (in DE)', fontsize=8)
        ax.set_title('Price')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_battery(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['Battery'].values[0]
        car2_price = car2_data['Battery'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        ax.set_ylabel('Battery', fontsize=8)
        ax.set_title('Battery')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_charge(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['Fast_charge'].values[0]
        car2_price = car2_data['Fast_charge'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        ax.set_ylabel('Fast_charge', fontsize=8)
        ax.set_title('Fast_charge')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_range(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['Range'].values[0]
        car2_price = car2_data['Range'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        ax.set_ylabel('Range (in Km)', fontsize=8)
        ax.set_title('Range')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_top_speed(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['Top_speed'].values[0]
        car2_price = car2_data['Top_speed'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        ax.set_ylabel('Top_speed (in kg/h)', fontsize=8)
        ax.set_title('Top_speed')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_acceleration(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['acceleration..0.100.'].values[0]
        car2_price = car2_data['acceleration..0.100.'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        ax.set_ylabel('acceleration (in kg/hr)', fontsize=8)
        ax.set_title('acceleration')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_efficiency(self, car1, car2):
        """Function to create a bar graph comparing prices of two car models."""
        plt.close('all')
        fig, ax = plt.subplots(figsize=(4, 2))
        car1_data = self.dataframe[self.dataframe['Car_name'] == car1]
        car2_data = self.dataframe[self.dataframe['Car_name'] == car2]
        car1_price = car1_data['Efficiency'].values[0]
        car2_price = car2_data['Efficiency'].values[0]
        ax.bar([car1, car2], [car1_price, car2_price], width=0.7)
        ax.tick_params(axis='x', labelsize=6)
        ax.tick_params(axis='y', labelsize=8)
        ax.set_ylabel('Efficiency', fontsize=8)
        ax.set_title('Efficiency')
        histogram_widget = FigureCanvasTkAgg(fig, master=self.parent)
        return histogram_widget

    def plot_correlation(self):
        """Function to create a plot_correlation of all car models."""
        plt.close('all')
        fig_corr, ax_corr = plt.subplots()
        sns.scatterplot(x='Price.DE.', y='Efficiency', data=self.dataframe,
                        ax=ax_corr)
        ax_corr.set_xlabel("Price")
        ax_corr.set_ylabel("Efficiency")
        ax_corr.set_title("Correlation between Price and Efficiency")
        correlation_widget = FigureCanvasTkAgg(fig_corr, master=self.parent)
        return correlation_widget
