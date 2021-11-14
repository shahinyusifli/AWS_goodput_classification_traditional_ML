import pandas as pd


class ExtractData:


    def __init__(self, data_name, sep_value, columns, data_type):
        self.data_name = data_name
        self.sep_value = sep_value
        self.columns = columns
        self.data_type = data_type
    
    def extract_data(self):
        try:
            if self.data_type == 'dat':
                data = pd.read_table(self.data_name, sep=self.sep_value, usecols=self.columns)
                return data
            elif self.data_type == 'csv' :
                data = pd.read_csv(self.data_name, sep=self.sep_value, usecols=self.columns)
                return data
        
        except:
            print('Problem in data EXTRACTION')