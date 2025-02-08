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
