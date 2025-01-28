import yaml


def read_token():
	with open("config.yml") as f:
		try:
			contents = yaml.safe_load(f)
			return contents[BOT_TOKEN]
		except yaml.YAMLError as e:
			print(e)


def log_keys():
	pass


def send_message():
	token = read_token()
	pass

def detect_process(name):
	pass


def main():
	# on start of the script (aka on pc startup)
	send_message("PC has been turned on and logged in successfully.")
	pass
