import os
import sys
import dill
import pandas as pd
import numpy as np

from src.mlproject.exception import CustomException

def save_object(obj, file_path):
    """Saves a Python object to the specified file path using pickle."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        import pickle
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)