import config
from lib.GeminiOperations import establishConnection
from lib.ExcelOperations import readingExcelReport
from lib.ExcelOperations import performContentReview
from lib.ExcelOperations import savingCorrectedData

def main():
	conversation = establishConnection.establishConnection(config.config['api_key'])
	df = readingExcelReport.readingExcelReport(config.config)
	corrected_df = performContentReview.performContentReview(df, config.config, conversation)
	savingCorrectedData.savingCorrectedData(corrected_df, config.config)

main()