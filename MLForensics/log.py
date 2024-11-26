import logging


def getLogger():
    format_str = '%(asctime)s:%(message)s'
    file_name  = 'MLForensics.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger('logger')
    return loggerObj
