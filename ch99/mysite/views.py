import logging

logger = logging.getLogger('mylogger')

def my_view(request, arg1, arg):
    if bad_mojo:
        logger.error('Something went wrong!')