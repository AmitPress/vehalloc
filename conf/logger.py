import logging
from logging.handlers import TimedRotatingFileHandler

# the logs must be rotated everyday
handler = TimedRotatingFileHandler('logs/dailyactivities.log', when='midnight', interval=1, backupCount=5)

# get a default logger and set the handler
logger = logging.getLogger("default")
# define formatter
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
handler.setFormatter(formatter) # setting the formatter

logger.addHandler(handler) # adding the handler
logger.setLevel(logging.INFO) # setting the lowest capture l;evel
