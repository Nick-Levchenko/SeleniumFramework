import logging


class Logger:

    def getLogger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(f"logs.log", mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(handler)
        return logger
