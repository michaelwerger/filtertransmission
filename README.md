# filtertransmission
Estimate optical filter transmission and FWHM using DADOS spectrograph and Python Notebooks

Folder fotos contains screenshots during data aquisition and the very basic setup
Folder data contains the measured data
Folder src contains the scripts
Folder ref contains a reference spectrum
Folder products contains some PDF and PNG files for documentation purposes

Data is taken using the Baader DADOS Spectrograph with the 900l/mm grism
An ASI ZWO 071 MMC Pro camera is used for imaging

For the scripts except compute_dispersion_ml_900lmm.ipynb, Python 3.11 and the module astropy are used;
for the script ompute_dispersion_ml_900lmm.ipynb there is a tensorflow-based environment with GPU support
used; see project 'keras_based_lineidentification'

recipe for the filter transmission measurement (to be detailed)

* measure
  * the dispersion with a calibration lamp
  * the transmission without filter
  * the transmission with filter
  
* create the environment with python and astropy
* determine the dispersion partly manually with determine_disperson

or

* create the environment with tensorflow
* create the wavelength calibration images from the calibration lamp measurement with create_testimages.ipynb
* compute dispersion with the ml method (using a pre-trained model)

then

* use or create the environment with python and astropy
* determine the filter transmission using an example like process_filter_04nm.ipynb

