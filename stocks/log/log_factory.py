import logging

class LoggerFactory():

    def __init__(self):
        self.logger = logging.getLogger()

    def get_logger(self, name, level, handlers):
        # handlers=0->None, 1->screen, 2->file, 3->both
        self.logger = logging.getLogger(name)
        self.set_level(level)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        if level >= 1:
            sh = logging.StreamHandler()
            sh.setLevel(level)
            sh.setFormatter(formatter)
            self.logger.addHandler(sh)
        if level >= 2:
            fh = logging.FileHandler(f'data/logs/{name}.log')
            fh.setLevel(level)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        return self.logger

    def set_level(self, level):
        self.logger.setLevel(level)