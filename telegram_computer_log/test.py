from main import Logger


logger = Logger("events.log")
assert logger.debug("test") == True
