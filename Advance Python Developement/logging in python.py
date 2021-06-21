"""
      ***Logging***:
Logging is a means of tracking events that happen when some software runs.
Logging is important for software developing, debugging and running.
If you don’t have any logging record and your program crashes,
there are very little chances that you detect the cause of the problem.
And if you detect the cause, it will consume a lot of time

"""





"""
In its simplest term, the `logging` module is used to print things out
(to the console or to a file).

The `logging` module should be used to communicate with the developer
(e.g. information about what’s happening; when an error happens; a critical problem; etc…).

To communicate with the user, continue using `print()` and `input()`.

To use logging, we just have to import the `logging` module and get a new logger:

"""

"""

There are various logging levels (below in ascending order of criticality),
for you to use depending on the circumstance:

DEBUG
INFO
WARNING
ERROR
CRITICAL

So if you’re logging for help while developing or debugging,
use the `DEBUG` level (`logger.debug('message')`).

If your program’s about to crash because a critical exception happened; 
use `logger.critical()`.
"""


"""
import logging
logger = logging.getLogger('test_logger')
logger.info("Everything is Fine")
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


logger.debug('Serious Issue')
logger.info("Everything is Fine")

logger.setLevel(logging.CRITICAL)
logger.critical('Internet Is Down')

"""

import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger()

logger.info('This Is Info Log')
logger.debug('This is Debug Log')
logger.critical('This is Critical Log')
logger.error('An Error Occurred')
logger.warning('This Is Warning Log')
