import time
import logging
import sys

logger = logging.getLogger("TESTS FOR THE BEST GAMEDEV COMPANY:)")
logger.setLevel(logging.DEBUG)
empty = logging.StreamHandler("")
ch = logging.StreamHandler(sys.stderr)
f_handler = logging.FileHandler("myoutput.txt")
ch.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
f_handler.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(f_handler)

def _measuring(func):
    def measure(self):
        try:
            start_time = time.time()
            func(self)
            time_end = time.time()
            # print("")
            logger.info(f"\nYour test {func.__name__} took {time_end - start_time} seconds")
        except Exception as e:
            logger.info(f"\nYour test {func.__name__}"
                        f"failed with exception: {e}")
    return measure


