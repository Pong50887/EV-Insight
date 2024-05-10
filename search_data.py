from read_data import Data


class Search:
    """
    This is a class for searching Data EV car

    Attributes:
        data (Data): Data to store information of EV car.
        dataframe (dataframe) : Dataframe of data.
    """

    def __init__(self):
        """
        The constructor for Search class.
        """
        self.data = Data()
        self.link_data = self.data.get_link()
        self.dataframe = self.data.get_data()
        self.mainframe = self.dataframe.copy()

    def search_data(self, entry_search):
        results = self.mainframe[
            self.mainframe['Car_name'].str.lower().str.contains(entry_search)]
        if results.empty:
            return "No matching results"
        else:
            return results

    def get_default_data(self):
        return self.dataframe

    def get_price(self, rate, old_rate):
        self.mainframe['Price.DE.'] /= old_rate
        self.mainframe['Price.DE.'] *= rate
        self.mainframe['Price.DE.'] = round(self.mainframe['Price.DE.'], 1)
        return self.mainframe

    def search_most_efficient(self):
        sort = self.mainframe.sort_values(by='Efficiency', ascending=False)
        return sort

    def search_longest_range(self):
        sort = self.mainframe.sort_values(by='Range', ascending=False)
        return sort

    def search_cheapest(self):
        sort = self.mainframe.sort_values(by='Price.DE.')
        return sort

    def search_fast_charge(self):
        sort = self.mainframe.sort_values(by='Fast_charge', ascending=False)
        return sort

    def get_car_name_list(self):
        car_names = self.dataframe['Car_name'].tolist()
        return car_names

    def reset_mainframe(self):
        self.mainframe = self.dataframe.copy()

    def get_link_from_csv(self, car_name):
        car_data = self.link_data[self.link_data['Car_name'] == car_name]
        return car_data.iloc[0]['Car_name_link']
