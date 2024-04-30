import h5py
import numpy as np

'''
Groups
Groups are the container mechanism by which HDF5 files are organized. From a Python perspective, they operate somewhat like dictionaries. In this case the “keys” are the names of group members, and the “values” are the members themselves (Group and Dataset) objects.

'''



f = h5py.File('myfile.hdf5','w')



'''
Group objects also contain most of the machinery which makes HDF5 useful. The File object does double duty as the HDF5 root group, and serves as your entry point into the file:
'''

import pandas as pd


df_yh = pd.read_csv('./2024-04-16_AAPL_1min_yf.csv',index_col='date', parse_dates=True)
df_av = pd.read_csv('./20240424063830_AAPL_1min_av.csv',index_col='date', parse_dates=True)
print(df_av)
print(df_yh)


print(f.name)
print(list(f.keys()))

# Creating groups
grp = f.create_group('AAPL')
print(grp.name)

subgrp = grp.create_group('2024.04')
print(subgrp.name)

subsubsrp = subgrp.create_group('OHLCV')
print(subsubsrp.name)




#arr = df.to_numpy(dtype="datetime64[ns]")
#print(arr)

#dset = f.create_dataset("/AAPL/2024.04/OHLCV/1min", data=arr)
