import pandas as pd
import time
from ..GeminiOperations import sendAndReceivePrompts
from .. import terminateProgram



def performContentReview(df, config, conversation):
	#Checking if all columns are present, if not removing it from the array
	for column in config['columns_to_check']:
		try:
			tempDF = df[column]
		except:
			print(f"Can not find a column with the name {column}")
			config['columns_to_check'].remove(column)
	
	# Looping through each column and performing content review
	for column in config['columns_to_check']:
		print(f"Processing {column} column ...")
		originalStatements = []
		correspondingCorrectedStatements = []
		
		for index, cell in enumerate(df[column]):
			if type(cell) != str:
				continue
			if cell in originalStatements:
				result = correspondingCorrectedStatements[originalStatements.index(cell)]
			else:
				result = sendAndReceivePrompts.sendAndReceivePrompts(conversation, (config['instructions'] + column), str(cell))
				result = result.replace("*", "")
				originalStatements.append(cell)
				correspondingCorrectedStatements.append(result)
				time.sleep(30)
			
			if result.strip() != "OK":
				df.at[index, column] = result
			
			#Printing the corrected sentances
			if config['show_corrections'] == "true":
				print("Actual sentance: ", cell)
				print("Corrected sentance: ", result)
		print(f"Completed processing {column} column!")
	return df
