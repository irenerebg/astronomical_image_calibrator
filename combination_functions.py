'''
____________________________

IMAGE COMBINATION FUNCTIONS
____________________________

This module defines the functions used to combinate images

'''

import numpy as np
from astropy.stats import mad_std  # absolute median deviation

def average(bits):
    '''Computes the mean from a matrix of values
    
    Arguments:
    - bits (array, unit16): an array with all the images to combine
    
    Returns:
    - average (float64): combined values by mean
    '''
    return np.average(bits, axis=0)

def median(bits):
    '''Computes the median from a matrix of values
    
    Arguments:
    - bits (array, unit16): an array with all the images to combine
    
    Returns:
    - median (float64): combined values by median
    '''
    return np.median(bits, axis=0)

def median_absolute_deviation(bits):
    '''Computes the MAD from a matrix of values
    
    Arguments:
    - bits (array, unit18): an array with all the images to combine
    
    Returns:
    - average (f8): combined values by MAD
    '''
    mad_sigma = mad_std(bits, axis=0)
    median = np.median(bits, axis=0)            # images are combined by the median
    
    excluidos = (bits - median) / mad_sigma > 1 # those values >1 away are excluded
    
    bits = bits.astype(float)

    valores_originales = bits[excluidos]        # original values are saved
    bits[excluidos] = np.nan                    # we use nan to omit those values when we use the mean

    clip_combine = np.nanmean(bits, axis=0)     # we apply the mean without the nan values
    bits[excluidos] = valores_originales        # nan values are turned in to the original values
    return clip_combine
