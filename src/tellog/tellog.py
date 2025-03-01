import requests
import os
import yaml
import time


class Bot:
	def __init__(self):
		self.__data = self.__get_token_and_chat()
		self.__token = self.__data[0]
		self.__chat_id = self.__data[1]


	def __get_token_and_chat(self):
		# this will only run the first timethe script is ran.
		# this just creates the tellog_config.yml file. the rest of the script is ran as usual
		if "tellog_config.yml" not in os.listdir():
			f = open("tellog_config.yml", "w+")
			f.write(f"""BOT_TOKEN: {input("Please enter the bot's token: ")}\nCHAT_ID: {input("Enter chat id: ")}\n""")
			f.close()		
		# now it reads both the bot_token and the chat_id from config
		with open("tellog_config.yml") as f:
			try:
				contents = yaml.safe_load(f)
				return contents["BOT_TOKEN"], contents["CHAT_ID"]
			except yaml.YAMLError as e:
				print(e)


	def log(self, message):
		url = f"https://api.telegram.org/bot{self.__token}/sendMessage?chat_id={self.__chat_id}&text={message}"
		
		response = requests.get(url)
		
		if response.ok:
			print("Successful message sent.")
			return True
		else:
			print("Not successful.")
			return False


def tellog(bot):
	def inner(func):
		start_time = time.time()

		def wrapper():
			func()
			bot.log(f"{func.__name__} executed successfully in {time.time()-start_time}")
			
		return wrapper

	return inner
