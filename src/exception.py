import sys
import os
from dataclasses import dataclass
from src.logger import logging
@dataclass
class user_exception :
    def show_exception (self) :
        exc_type,exc_obj,exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        return "Name of the exception is {} and the exception occur in the {} file and the exception occur at line number {} ".format(str(exc_type),fname,exc_tb.tb_lineno)


if __name__=='__main__' :
    print("We are checking that information of the exception are coming in the proper format")
    exception = user_exception()
    try :
        a=2/0
        print(a)
    except :
        logging.info(exception.show_exception())



