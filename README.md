# filtertransmission

## Overview

Show transmission of an optical filter and determine FWHM and peak as well as central filter wavelength using DADOS spectrograph and Python Notebooks

Folder fotos contains screenshots during data aquisition and the very basic setup
Folder data contains the measured data
Folder src contains the scripts
Folder ref contains a reference spectrum
Folder products contains some PDF and PNG files for documentation purposes

Data is taken using the Baader DADOS Spectrograph with the 900l/mm grism
An ASI ZWO 071 MMC Pro camera is used for imaging

For the scripts except compute_dispersion_ml_900lmm.ipynb, Python 3.11 and the module astropy are used;
for the script ompute_dispersion_ml_900lmm.ipynb there is a tensorflow-based environment with GPU support
used; see project 'keras_based_lineidentification'.

With compute_dispersion_ml.ipynb a one-step notebook is available now which requires only the training data from keras_based_lineidentification (i.e., labels and model)

## Recipe

recipe for the filter transmission measurement (to be detailed)

* measure
  * the dispersion with a calibration lamp
  * the transmission without filter
  * the transmission with filter
  
* create the environment "tf-astropy" (see below)


* determine the dispersion partly manually with determine_disperson -
enter the necessary parameters (e.g., filenames) in the notebook

or

* compute dispersion with the compute_dispersion_ml notebook (using a pre-trained model) -- here you may adjust compute_dispersion_ml.toml 
for the necessary parameters

then

* determine the filter transmission using an example like process_filter_04nm.ipynb

## Create the environment

This subsection explains how to setup an environment with all necessary
modules and a tensorflow adaption for macos to use the internal GPU

The following worked for me for this project:

I use a directory ~/conda/py311 for the miniconda environment and 
a separate directory ~/conda/channel/apple for packages downloaded here

> cd ~\
> cd conda

Download the installation script for minicona for Apple silicon from https://repo.anaconda.com/miniconda/ into ~/conda/py311,
then continue as follows

> bash ./py311/Miniconda3-py311_25.3.1-1-MacOSX-arm64.sh -b -u -p ~/conda/py311 \
> source py311/bin/activate

Then, switch to the project directory
> cd ~/Workspaces \
> cd keras_based_line_identification \
> conda create -n tf python=3.11.11 \
> conda activate tf 

Download tensorflow-deps-2.10.0-0.tar.bz2 from https://anaconda.org/apple/tensorflow-deps/files

> conda install ~/conda/channel/apple/tensorflow-deps-2.10.0-0.tar.bz2 \
> pip install tensorflow-metal  \
> pip install tensorflow-macos \
> pip install pandas \
> pip install matplotlib \
> pip install scikit-learn \
> pip install scipy \
> pip install 'imageio==2.37.0' \
> pip install plotly \
> pip install opencv-python \
> pip install prettytable \
> conda install notebook \
> pip install ipykernel \
> pip install astropy