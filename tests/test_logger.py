import unittest
from stocks.log.log_manager import LogManager

class TestCase(unittest.TestCase):
    def test_log(self):
        # Test acquiring the logger and using it to print to screen
        self.logger = LogManager.get_instance().get_logger('test_log')
        self.logger.debug("This is a debug")
        self.logger.info("This is a info")
        self.logger.debug(__name__)