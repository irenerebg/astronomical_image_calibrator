'''
___________________________

IMAGE CALIBRATION FUNCTION
___________________________

This module defines the function used to calibrate images

'''

def image_calibrator(dark, bias, flat, original):
    '''Computes the calibrated image by doing several 
    mathematical operations.
    
    Arguments:
    - dark (fits): Master Dark image
    - bias (fits): Master Bias image
    - flat (fits): Master Flat image
    - original (uint16): Astronomical image data
    
    Returns:
    - final_image (float64): Calibrated image data 
    
    '''
    # Extracting data from the fits file
    time_dark = dark[0].header['EXPTIME']
    dark = dark[0].data
    bias = bias[0].data
    flat = flat[0].data
    # Calibration formulas are applied
    dark_current = (dark - bias) / time_dark
    final_image = (original - bias - dark_current) / flat
    return final_image
