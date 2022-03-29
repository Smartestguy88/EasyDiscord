# All scripts by Smartguy88 (Discord Smartguy88#4909, github Smartestguy88)
# gg gl :)

## If you are looking for a template, you are looking in the right place!
## Note this program can only run one bot at a time in the current version

# Looking for the github? Here it is: https://github.com/Smartestguy88/EasyDiscord

# Standard functions (import):
import Smartguy88

import logging

LOGGING = logging.getLogger(__name__) # Global root logger, see documentation of logging.py

LOGGER = logging.getLogger(f"{__name__}.PrimaryLogger") # Primary logger, handles standard logs
PANICLOGGER = logging.getLogger(f"{__name__}.PANIC") # Logs to private DM of owner, panic handler
ADMINLOGGER = logging.getLogger(f"{__name__}.ADMIN") # Admin logger, handles admin-only logs
DEBUGLOGGER = logging.getLogger(f"{__name__}.DEBUG") # Logs to debug channels, specifically a server / DM
HARDWARELOGGER = logging.getLogger(f"{__name__}.HARDWARE") # Logs to harddrive, *hard coded*

class LOG:
  def __call__(msg, *msgs, **options):
    totalMessage = str(msg)

from uuid import uuid4

Smartguy88.ass()