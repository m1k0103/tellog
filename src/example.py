from telegram_computer_log import Bot, tellog

bot = Bot()

@tellog(bot)
def my_func():
	print("hello world!")


if __name__ == "__main__":
	my_func()
