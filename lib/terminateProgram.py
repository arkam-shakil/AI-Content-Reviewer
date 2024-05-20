import sys

def terminateProgram(error, exit="true"):
	print("An error occurred:", str(error))
	
	if exit == "true":
		terminate = input("Press 'Enter' to exit the program")
		sys.exit()
