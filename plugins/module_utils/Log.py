import logging

class customLogger:
	def __init__(self, name, log_file=None, log_level=logging.DEBUG):
		self.logger = logging.getLogger(name)
		self.logger.setLevel(log_level)
		self.formatter = logging.Formatter('%(asctime)s-%(levelname)s -> %(message)s')

		if log_file:
			file_handler = logging.FileHandler(log_file)
			file_handler.setLevel(logging.DEBUG)
			file_handler.setFormatter(self.formatter)
			self.logger.addHandler(file_handler)

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)
	
	def error(self, message):
		self.logger.error(message)