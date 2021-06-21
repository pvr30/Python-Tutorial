# The Logs will Appear in log.txt file.


import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger()

logger.info('This Is Info Log')
logger.debug('This is Debug Log')
logger.critical('This is Critical Log')
logger.error('An Error Occurred')
logger.warning('This Is Warning Log')

