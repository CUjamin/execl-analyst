import pandas as pd


class ExcelObject:
    def __init__(self, file):
        self.excel = pd.ExcelFile(file)
        self.sheet_names = self.excel.sheet_names
        self.sheet_total = len(self.excel.sheet_names)
        self.sheets = []
        for sheet_name in self.sheet_names:
            sheet = pd.read_excel(file, sheet_name)
            self.sheets.append(sheet)

    def print(self):
        print('sheet_names:', self.sheet_names)
        print('sheet_len:', self.sheet_total)
        for sheet in self.sheets:
            print(sheet)
