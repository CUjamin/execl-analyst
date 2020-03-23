from unittest import TestCase
from excel.ExcelObject import ExcelObject
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


class TestExcelObject(TestCase):
    def test_print(self):
        print(PROJECT_ROOT)
        filename = PROJECT_ROOT + '/工作簿1.xlsx'
        file = open(filename, 'rb')
        excelObject = ExcelObject(file)
        excelObject.print()
