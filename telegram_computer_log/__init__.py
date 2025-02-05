import yaml
import os
from telegram_computer_log.main import main

def start():
	#check if config exists, and asks for bot key.
	if "config.yml" not in os.listdir():
		f = open("config.yml", "w+")
		f.write(f"""BOT_TOKEN: {input("This is your first setup. Please enter the bot token of the bot: ")}\nCHAT_ID: {input("This is your first setup. Please enter the chat id: ")}\n""")
		f.close()
	else:
		print("config.yml detected. Skipping first setup...")
	
	# running the main function
	main()
