import pickle

class CCDParameters():
    #xsize = 4656
    #ysize = 3520
    xsize = 4944
    ysize = 3284

    @staticmethod
    def __init__(xsize=4656, ysize=3520):
        CCDParameters.xsize = xsize
        CCDParameters.ysize = ysize


class FigureSize():
    THIN     = [24, 3]
    NARROW   = [24, 8]
    MEDIUM   = [24, 15]
    LARGE    = [24, 24]

class Parameters(object):

    slit_rows = []
    slit_positions = []
    lower_pixel = 0
    upper_pixel = 0
    detection_level =0.0
    detection_windowsize = 19
    detection_order = 4
    detection_distance = 8
    flip = False
    dark = None # either float or 2d array
    processed = True # if true, instrument calibration is determined already
    vmin, vmax = 0, 100
    wavelength_solution_file = 'wavelength_solution.dat'
    show_colorbar = False

    @staticmethod
    def dump(f='parameters.pickle'):

        with open(f, 'wb') as parameters_f:
            pickle.dump(Parameters, parameters_f)

    @staticmethod
    def load(f='parameters.pickle'):
        with open(f, 'rb') as parameters_f:
            r = pickle.load(parameters_f)
        return r

     