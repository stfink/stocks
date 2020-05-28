import logging
from stocks.log.log_factory import LoggerFactory

class LogManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            instance = object.__new__(cls, *args, **kwargs)
            instance.__init__()
            cls._instance = instance
        return cls._instance

    @classmethod
    def get_instance(cls, *args, **kwargs):
        return cls.__new__(cls, *args, **kwargs)
    
    def __init__(self):
        if LogManager._instance:
            return
        self.logger_factory = self._create_logger_factory()

    def _create_logger_factory(self):
        return LoggerFactory()

    def get_logger(self, name, level=logging.DEBUG, handlers=3):
        return self.logger_factory.get_logger(name, level, handlers)