# All scripts by Smartguy88 (Discord Smartguy88#4909, github Smartestguy88)
# gg gl :)
# This file is NOT TO BE EDITED!

## *** IF YOU ARE LOOKING FOR A FILE TO EDIT THIS IS NOT IT  ***
## *** THIS IS AN INTERNAL FILE AND IS IMPLEMENTATION DETAIL ***

## If you are looking for a template, though, you are looking in the right place!
## Note this program can only run one bot at a time in the current version

# Looking for the github? Here it is: https://github.com/Smartestguy88/EasyDiscord
# Looking for installation guide? Here it is: "pip install EasyDiscord" into a python-enabled terminal

from typing import final

# Standard functions (import) from my own package:
import Smartguy88

import logging


@final
class LOG:
  """
  This class is used to log messages to the console and to the log file.
  How each logging level is dealt with from this class depends on a few factors, which are internally defined from this function
  This class' functions are implementation detail ONLY, and should not be used by the user nor changed :)
  """
  # Module root logger, see documentation of logging.py at https://docs.python.org/3/library/logging.html
  _logger: logging.Logger = logging.getLogger(__name__)
  def _logger_get(self): return self._logger
  def _logger_set(self): raise 

  logger = property(_logger_get, _logger_set, _logger_del)

from uuid import uuid4



