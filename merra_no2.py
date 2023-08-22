import xarray as xr
import pandas as pd
import numpy as np

time = ['2010','2011','2012','2013','2014','2015','2016']

for i in time:
    merra = xr.open_dataset('/data0/shr/bne/jc_data/nox/daily/raw/merra/daily' + i + 'no2.nc')
    merra_df = merra.to_dataframe()
    
    merra_df = merra_df.reset_index()
    merra_df.rename(columns={'NO2':'pred_merra'})
    
    merra_df.to_csv('/data0/shr/bne/jc_data/nox/daily/formatted/uncropped/merra/merra_no2_' + i + '_daily.csv')

