import subprocess
import sys

def installingRequiredPythonModules():
	#Checking for pandas
	try:
		import pandas as pd
		print("Found Pandas")
	except ImportError:
		print("Pandas module not found. Installing pandas...")
		try:
			subprocess.check_call('py -m pip install pandas')
			print("Pandas installed successfully.")
		except Exception as e:
			print(f"Error installing pandas: {e}")
			print("\aTerminating the program ...")
			sys.exit()
	
	#Checking for google-ai-generativelanguage
	try:
		import google.generativeai as genai
		print("Found google-ai-generativelanguage")
	except ImportError:
		print("google-ai-generativelanguage module not found. Installing pandas...")
		try:
			subprocess.check_call('py -m pip install google-ai-generativelanguage')
			print("google-ai-generativelanguage installed successfully.")
		except Exception as e:
			print(f"Error installing google-ai-generativelanguage: {e}")
			print("\aTerminating the program ...")
			sys.exit()
	
	print("Found all required modules")