# ASTRONOMICAL IMAGE CALIBRATOR

Este proyecto calibra de forma automática imágenes astronómicas generadas por cámaras CCD

## Estructura del programa

- calibrated_files: carpeta donde se almacenan los archivos .fits calibrados
    - AAVSO: carpeta donde se almacenan los archivos .fits calibrados por el método de la AAVSO
    - MAD: carpeta donde se almacenan los archivos .fits calibrados por el método de desviación absoluta de la mediana

- calibrated_files: carpeta donde se almacenan los archivos .png calibrados
    - AAVSO: carpeta donde se almacenan los archivos .png calibrados por el método de la AAVSO
    - MAD: carpeta donde se almacenan los archivos .png calibrados por el método de desviación absoluta de la mediana

- data: carpeta donde se almacenan los archivos originales
    - Bias: tomas Bias para generación de Master Bias
    - Darks: tomas Dark para generación de Master Dark y Master Flat
        - Darks: tomas Dark para generación de Master Dark
        - Flat_Darks: tomas Dark para restar a la Master Flat
    - Flats: tomas Flat para generación de Master Flat
    - Lights: tomas de las imágenes astronómicas a calibrar, cada carpeta contiene las tomas del objeto de su mismo nombre

- master_files
    - AAVSO: carpeta donde se almacenan los archivos .fits master por el método de la AAVSO
    - MAD: carpeta donde se almacenan los archivos .fits master por el método de desviación absoluta de la mediana

- *[calibrator.py](calibrator.py)*: módulo con la función de calibración

- *[combination_functions.py](combination_functions.py)*: módulo con las funciones de media, mediana y MAD

- *[file_shortcuts.py](file_shortcuts.py)*: módulo con atajos para apertura y creación de archivos .fits

- *[image_calibrator.ipynb](image_calibrator.ipynb)*: notebook ejecutable que genera las imágenes calibradas en .fits y .png

- *[master_files_generator.ipynb](master_files_generator.ipynb)*: notebook ejecutable que genera los archivos Master en .fits