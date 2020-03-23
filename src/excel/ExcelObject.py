import pandas as pd


class ExcelObject:
    def __init__(self, file):
        self.excel = pd.ExcelFile(file)
        self.sheet_names = self.excel.sheet_names
        self.sheet_total = len(self.excel.sheet_names)

    def print(self):
        print('sheet_names:', self.sheet_names)
        print('sheet_len:',self.sheet_total)
