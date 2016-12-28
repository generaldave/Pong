########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Driver File                                                          #
#                                                                      #
# Created on 2016-12-27                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from Logger import *   # Logger Class - Error logging
from init   import *   # init Class - Initialize App

########################################################################
#                                                                      #
#                                DRIVER                                #
#                                                                      #
########################################################################

# Initialize app
def main():
    app = init(appDirectory)

# Store app directory
appDirectory = os.path.dirname(os.path.realpath(__file__))

# Initialize error logging
logger = Logger(appDirectory, 'w')

# Try to run app, otherwise log error
try:   
    main()
except:
    logger.createLog('')
