import pandas as pd
from .. import terminateProgram


def readingExcelReport(config):
	try:
		print("Proceding to read the excel file ...")
		xls = pd.ExcelFile(config['file_path'])
		df = xls.parse(config['sheet_name'], (config['header_row_index']-1))
		print("Successfully extracted data from the excel file!")
		return df
	except Exception as e:
		print("Error encountered while reading the excel file\n")
		terminateProgram.terminateProgram(e)
