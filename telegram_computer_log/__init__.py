import yaml
import os

def start():
	#check if config exists
	if "config.yml" not in os.listdir():
		f = open("config.yml", "w+"):
		f.write(f"""BOT_TOKEN: {input("This is your first setup. Please enter the bot token of the bot: ")}""")
		f.close()
	
	
	
