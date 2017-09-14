import math

class StreamWidthRegression:
    """description of class"""

    def __init__(self):
        #Coefficients for regression for each region and bed type
        #                                 Intcpt,     Area,       Precip,      Slope,      Elev
        self.north_appalachians_fine   = [ 0.1195,     0.3702,     -2.6518,    -0.1895,    0.0000  ]
        self.north_appalachians_course = [ 0.1195,     0.3702,     0.0000,     -0.1895,    0.0000  ]

        self.south_appalachians_fine   = [ 0.3058,     0.3935,     0.0000,     0.0000,     0.0000  ]
        self.south_appalachians_course = [ 0.6053,     0.3935,     0.0000,     0.0852,     0.0000  ]

        self.coastal_plains_fine       = [ 0.4332,     0.2604,     0.0000,     0.0000,     0.0000  ]
        self.coastal_plains_course     = [ 0.8927,     0.2604,     0.0000,     0.0000,     0.00557 ]

        self.upper_midwest_fine        = [ 0.2356,     0.4110,     2.5732,     0.0876,     0.00137 ]
        self.upper_midwest_course      = [ 0.2356,     0.4110,     0.0000,     0.0000,     0.0000  ]

        self.temperate_plains_fine     = [ 0.3957,     0.3498,     1.1730,     0.0000,     0.0000  ]
        self.temperate_plains_course   = [ 0.8318,     0.1516,     0.5172,     0.0000,     0.0000  ]

        self.northern_plains_fine      = [ 0.4041,     0.2788,     0.0000,     0.0000,    -0.00034 ]
        self.northern_plains_course    = [ 0.2607,     0.2788,     0.0000,     0.0000,     0.0000  ]

        self.southern_plains_fine      = [ 0.7568,     0.1666,     0.0000,     0.1296,     0.0000  ]
        self.southern_plains_course    = [ 0.2851,     0.4920,     0.0000,     0.1296,    -0.00024 ]

        self.western_mountains_fine    = [ 0.1825,     0.3986,     0.6167,     0.0000,     0.0000  ]
        self.western_mountains_course  = [ 0.2524,     0.3986,     0.6167,     0.0000,     0.000033]

        self.xeric_fine                = [ 0.1168,     0.3223,     0.0000,     0.0000,     0.0000  ]
        self.xeric_course              = [ 0.3383,     0.3223,     0.3048,     0.0000,     0.0000  ]

        self.regions = {}
        self.regions[16] = [self.north_appalachians_fine, self.north_appalachians_course]
        self.regions[21] = [self.south_appalachians_fine, self.south_appalachians_course]
        self.regions[9]  = [self.coastal_plains_fine, self.coastal_plains_course]
        self.regions[25] = [self.upper_midwest_fine, self.upper_midwest_course]
        self.regions[24] = [self.temperate_plains_fine, self.temperate_plains_course]
        self.regions[17] = [self.northern_plains_fine, self.northern_plains_course]
        self.regions[22] = [self.southern_plains_fine, self.southern_plains_course]
        self.regions[26] = [self.western_mountains_fine, self.western_mountains_course]
        self.regions[27] = [self.xeric_fine, self.xeric_course]

    def calculate_stream_width(self, eco_region_id, area, precipitation, slope, elevation):
        regress_vars = [1.0, math.log(area), math.log(precipitation), math.log(slope), elevation]
        lst_regressions = self.regions[eco_region_id]

        stream_width_fine   = 0.0
        stream_width_course = 0.0
        for idx, item in enumerate(lst_regressions):
            stream_width_fine   += regress_vars[idx] * item[0][idx]
            stream_width_course += regress_vars[idx] * item[1][idx]

        dbl_bankfull_width_fine   = math.pow(10, stream_width_fine)
        dbl_mean_width_fine = dbl_bankfull_width_fine * 0.75

        dbl_bankfull_width_course = math.pow(10, stream_width_course)
        dbl_mean_width_course = dbl_bankfull_width_course * 0.75

        dbl_mean_width = (dbl_mean_width_fine + dbl_mean_width_course) / 2.0

        return dbl_mean_width
