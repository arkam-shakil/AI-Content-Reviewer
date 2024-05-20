import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.utils import get_column_letter
from .. import terminateProgram

def savingCorrectedData(df, config):
	# Writing the DataFrame to a new Excel file and preserving formatting
	try:
		print("Proceeding to write the DataFrame to a new Excel file ...")
		df.to_excel(config['output_file'], sheet_name=config['sheet_name'], index=False)
		print("Successfully wrote the DataFrame to the new Excel file!")
	except Exception as e:
		print("Error encountered while writing the DataFrame to the new Excel file\n")
		terminateProgram.terminateProgram(e)
