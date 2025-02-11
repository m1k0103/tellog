import requests
import os
import yaml
import time


class Bot:
	def __get_token_and_chat(self):
		# this will only run the first timethe script is ran.
		# this just creates the tellog_config.yml file. the rest of the script is ran as usual
		if "tellog_config.yml" not in os.listdir():
			f = open("tellog_config.yml", "w+")
			f.write(f"""BOT_TOKEN: {input("Please enter the bot's token: \nCHAT_ID: {input("Enter chat id: ")}")}""")
			f.close()
		
		# now it reads both the bot_token and the chat_id from config
		with open("tellog_config.yml") as f:
			try:
				contents = yaml.safe_load(f)
				return contents["BOT_TOKEN"], contents["CHAT_ID"]


	def __init__(self):
		data = __get_token_and_chat()
		self.__token = data[0]
		self.__channel_id = data[1]


	def log(self, message):
		url = f"https://api.telegram.org/bot{self.__TOKEN}/sendMessage?chat_id={self.__CHAT_ID}&text={message}"
		
		response = requests.get(url)
		
		if response.ok:
			print("Successful message sent.")
			return True
		else:
			print("Not successful.")
			return False


def tellog(func,bot):
	def wrapper():
		start_time = time.time()
		func()
		bot.log(f"{nameof(func)} executed successfully in {time.time()-start_time}")
	return wrapper
