#from visa_approval.logger import logging

#from visa_approval.exception import visaException
#import sys


#logging.info('This is our custom log.')

#try:
    #a=2/0
#except Exception as e:
    #raise visaException(e,sys)

#import os

#mongo_db_url = os.getenv('MONGODB_URL')
#print(mongo_db_url)

from visa_approval.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()