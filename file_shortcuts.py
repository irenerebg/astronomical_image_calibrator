'''
_____________________

FITS FILES SHORTCUTS
_____________________

This module defines functions to simplify opening and generating fits files

'''

from astropy.io import fits
import numpy as np

def file_opener(path):
    '''Opens a fits file
    
    Arguments:
    - path (string): file opening path
    
    Returns:
    - fits (fits): fits file opened
    '''
    return fits.open(path)

def save_header(path, n):
    '''Returns the header of a fits file
    
    Arguments:
    - path (string): file opening path
    - n (int): number of images
    
    Returns:
    - fits (header): header of a fits file
    '''
    filename = path + f"{n:03d}.fits"
    file = file_opener(filename)
    return file[0].header

def file_array_generator(path,n):
    '''
    Generates an array of matrices, each matrix is the data matrix of the values
    of the image pixels
    
    Arguments:
    - path (string): file opening path
    - n (int): number of images

    Returns:
    - file_array (array, int16 matrices): array of images
    - time_exp (float64): exposition time of the image
    '''
    file_list = []
    
    for i in range(1, n + 1):
        # Opening all the images
        filename = path + f"{i:03d}.fits"
        file = fits.open(filename)
        file_list.append(file[0].data)
        # Exposition time is saved in a extra variable
        if i == 1:
            time_exp = file[0].header['EXPTIME']

    file_array = np.array(file_list)
    return file_array, time_exp

def hdu_master_generator(image, time_exp, image_name, method):
    '''
    Generates an array of matrices, each matrix is the data matrix of the values
    of the image pixels
    
    Arguments:
    - image (matrix, float64): image pixels data
    - time_exp (float64): exposure time
    - image_name (string): "Bias", "Dark" or "Flat"
    - method (string): "AAVSO" or "MAD"

    Returns:
    - fits file with data values and exposure time saved
    '''
    # Create the HDU object
    hdu = fits.PrimaryHDU(image)
    hdu.header['EXPTIME'] = time_exp
    # Write the FITS file
    hdu.writeto(f'./master_files/{method}/Master_{image_name}.fits', overwrite=True)
        
def hdu_image_generator(image, header, image_name, method, i):
    '''
    Generates an array of matrices, each matrix is the data matrix of the values
    of the image pixels
    
    Arguments:
    - image (matrix, float64): image pixels data
    - time_exp (float64): exposure time
    - image_name (string): "Bias", "Dark" or "Flat"
    - method (string): "AAVSO" or "MAD"

    Returns:
    - fits file with data values and exposure time saved
    '''
    # Create the HDU object
    hdu = fits.PrimaryHDU(data=image, header=header)
    # Write the FITS file
    hdu.writeto(f'./calibrated_files/{method}/{image_name}/Calibrated_{image_name}_{i:03d}.fits', overwrite=True)