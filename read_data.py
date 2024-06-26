import pandas as pd


class Data:
    """
     This is a class to read data file.

     Attributes:
         path (str): Path of data file.
         dataframe (dataframe): Dataframe of data.
     """

    def __init__(self):
        """
        The constructor for Data class.
        """
        self.path = "final_data.csv"
        self.dataframe = pd.read_csv(self.path)
        self.link_data = self.dataframe[["Car_name", "Car_name_link"]]
        self.dataframe.drop(columns=['Unnamed: 0'], inplace=True)
        self.dataframe.drop(columns=['Car_name_link'], inplace=True)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", None)

    def get_data(self):
        """ The function for get dataframe """
        return self.dataframe

    def get_link(self):
        return self.link_data
