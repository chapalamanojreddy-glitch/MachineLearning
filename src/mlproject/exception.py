import sys
import os

try:
    from .logger import logging
except Exception:
    # allow running this module directly for quick debugging: ensure 'src' is on sys.path
    pkg_root = os.path.dirname(__file__)            # .../src/mlproject
    src_root = os.path.dirname(pkg_root)            # .../src
    if src_root not in sys.path:
        sys.path.insert(0, src_root)
    from mlproject.logger import logging


def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = ("Error occured in python script name [{0}] line number [{1}] error message [{2}]"
        .format(file_name, exc_tb.tb_lineno, str(error))
    )
    return error_message




class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail)

    def __str__(self):
        return self.error_message
   

    pass




