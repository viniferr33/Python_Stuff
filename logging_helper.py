"""
##### Logging #####

    Logging is a means of tracking events that happen when some software runs. 
    The software’s developer adds logging calls to their code to indicate that certain events have occurred. 
    An event is described by a descriptive message which can optionally contain variable data

    *Config         ->
    *Levels         ->
    *Hierarchy      ->
    *Propagation    ->
    *LogHandlers    ->
    *StackTraces    ->

"""

import logging

### Config
###
# Configure the configuration of the logging data
logging.basicConfig(
    level=logging.DEBUG,                                            # Defines the lowest level of logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Defines the format of logs, default is '%(name)s:%(message)s'
    datefmt='%m/%d/%Y %H:%M:%S'                                     # Define the dateformat
)

### File Config
###
# Set a .conf file to set the logger's config
## !Check the logging.conf file!
logging.config.fileConfig('logging.conf')

# Logger from the config file. 
logger = logging.getLogger('simpleExample')

### Levels
###
# That sets the priority level of an event, by default, the system logs only warning and above events

logging.debug('This is a debug message')            # |
logging.info('This is an info message')             # |
logging.warning('This is a warning message')        # |
logging.error('This is an error message')           # |
logging.critical('This is a critical message')      # V

### Hierarchy
###
# To create a logging handler module

# logg_handler.py
# -----------------------------------
logger = logging.getLogger(__name__)
logger.info('Some Stuff')
# -----------------------------------

### Propagation
###
# All logs created at a low hierarchy logger will be passed to high ones, that could make the log confusing, to avoid the propagation you can turn it to false.

logger.propagate = False

### LogHandlers
### 
# Dispatches the logs to appropriate destination, such as stdout, email, http, ftp, files, etc

# Creating a LogHandler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Config a LogHandler
stream_handler.setLevel(logging.WARNING)
stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)

file_handler.setLevel(logging.CRITICAL)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

# Add LogHandler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

### StackTraces
###
# To add the stacktrace of an Exception to the log
try:
    a = [1, 2, 3]
    value = a[3]
except IndexError as e:
    logging.error(e)
    logging.error(e, exc_info=True)

# ERROR:root:list index out of range
# ERROR:root:list index out of range
# Traceback (most recent call last):
#   File "<ipython-input-6-df97a133cbe6>", line 5, in <module>
#     value = a[3]
# IndexError: list index out of range

# For uncaught exceptions
import traceback
try:
    a = [1, 2, 3]
    value = a[3]
except:
    logging.error("uncaught exception: %s", traceback.format_exc())

