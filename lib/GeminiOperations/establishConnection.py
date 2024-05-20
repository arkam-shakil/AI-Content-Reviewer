import google.generativeai as genai
from .. import terminateProgram

"""
	Purpose: Establishes a connection to the GenerativeAI API using the provided API key.
	Args:
		-APIKey (str): The API key for accessing the GenerativeAI API.
"""
def establishConnection(APIKey):
	print("Stablishing connection ...")
	# Configuring the API key
	genai.configure(api_key=APIKey)
	
	# Setting up the model generation configuration
	generation_config = {
		"temperature": 1,
		"top_p": 0.95,
		"top_k": 0,
		"max_output_tokens": 2048,
	}
	
	# Defining safety settings to filter harmful content
	safety_settings = [
		{
			"category": "HARM_CATEGORY_HARASSMENT",
			"threshold": "BLOCK_MEDIUM_AND_ABOVE"
		},
		{
			"category": "HARM_CATEGORY_HATE_SPEECH",
			"threshold": "BLOCK_MEDIUM_AND_ABOVE"
		},
		{
			"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
			"threshold": "BLOCK_MEDIUM_AND_ABOVE"
		},
		{
			"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
			"threshold": "BLOCK_MEDIUM_AND_ABOVE"
		},
	]
	
	# Initializing the generative model
	model = genai.GenerativeModel(
		model_name="gemini-1.5-pro-latest",
		generation_config=generation_config,
		safety_settings=safety_settings
	)
	
	# Checking if the connection is successfully stablished
	try:
		conversation = model.start_chat(history=[])
		conversation.send_message("Hello")
		
		if (len(conversation.last.text) > 1):
			print("Connection has been stablished successfully!")
			return conversation
	except Exception as e:
		terminateProgram.terminateProgram(e)
