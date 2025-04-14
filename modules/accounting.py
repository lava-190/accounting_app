# app/modules/accounting.py
import ctypes
import os

# Determine the path to the compiled shared library
lib_path = os.path.join(os.path.dirname(__file__), '../../extensions/price_calculator.so')

# Load the shared C library using ctypes
calc_lib = ctypes.CDLL(lib_path)
calc_lib.calculate_total.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_size_t)
calc_lib.calculate_total.restype = ctypes.c_double

def calculate_total(prices):
    """
    Calculate the total sum of the provided price list using the C performance module.
    
    :param prices: List of float prices.
    :return: Total as float.
    """
    # Convert the list of prices to a ctypes array of doubles
    array_type = ctypes.c_double * len(prices)
    prices_array = array_type(*prices)
    total = calc_lib.calculate_total(prices_array, len(prices))
    return total
