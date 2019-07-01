# -*- coding: utf-8 -*-

from netCDF4 import Dataset
from pyloco import GroupTask


class WeatherMultimap(GroupTask):
    """read multiple netcdf data files and generate weather map images in parallel

'weathermultimap' task reads multiple netcdf data files and generates weather map
images in parallel

Example(s)
----------

>>> pyloco weathermultimap -o oecd.json
"""

    _name_ = "weathermultimap"
    _version_ = "0.1.0"

    def __init__(self, parent):

        self.add_data_argument("data", action="append", required=True,
                help="netcdf data file")
#
#        self.add_option_argument("-d", "--dataset", metavar="dataset",
#                default=default_dataset, help="Dataset code (default='%s')"
#                % default_dataset) 
#
#        self.add_option_argument("-f", "--filter", metavar="filter",
#                default=default_filter, help="Query filter(default='%s')"
#                % default_filter)
#
#        self.add_option_argument("-a", "--agency", metavar="agency",
#                default=default_agency, help="Agency code. (default='%s')"
#                % default_agency) 
#
#        self.add_option_argument("-p", "--params", metavar="params",
#                help="Additional parameters") 
#
#        self.add_option_argument("-o", "--outfile", metavar="outfile",
#                help="Save OECD data in a file") 
#
#        self.register_forward("data", help="OECD stats in JSON format ")

    def perform(self, targs):

        for path in targs.data:
            #rootgrp = Dataset(path, "r", format="NETCDF4")
            rootgrp = Dataset(path, "r")
            print (rootgrp.data_model)
            print ("GROUPS: ", rootgrp.groups)
            print ("DIMENSIONS : ", rootgrp.dimensions.keys())
            print ("VARIABLES :", rootgrp.variables.keys())
            #x2a_Sf_lfrac
            import pdb; pdb.set_trace()
            rootgrp.variables['x2a_Sf_lfrac'].get_dims()
            rootgrp.variables['x2a_Sf_lfrac'].shape

            rootgrp.close()

#        self.add_forward(data=data)
#['data_model', 'dimensions', 'disk_format', 'enumtypes', 'file_format', 'filepath', 'getncattr', 'groups', 'ncattrs', 'parent', 'path', 'variables', 'vltypes']
