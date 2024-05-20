import google.generativeai as genai
from .. import terminateProgram

def sendAndReceivePrompts(conversation, instructions, promptToSend):
	try:
		prompt = instructions + "\n\n" + promptToSend
		# Sending the prompt to the model
		conversation.send_message(prompt)
		return conversation.last.text
	except Exception as e:
		terminateProgram.terminateProgram(e)
