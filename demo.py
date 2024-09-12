from visa_approval.logger import logging

from visa_approval.exception import visaException
import sys


logging.info('This is our custom log.')

try:
    a=2/0
except Exception as e:
    raise visaException(e,sys)