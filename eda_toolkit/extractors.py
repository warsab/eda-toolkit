
import numpy as np

def extract_nr(value):
    numeric_value = ''.join(filter(str.isdigit, str(value)))
    return int(numeric_value) if numeric_value else np.nan
