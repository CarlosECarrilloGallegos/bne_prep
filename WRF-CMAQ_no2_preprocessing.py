import xarray as xr
import pandas as pd
import numpy as np
import glob
import dask

time = ['2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018']


for i in time:
    filelist = sorted(glob.glob('/data0/shr/bne/jc_data/o3/daily/raw/WRF-CMAQ/ftp.acom.ucar.edu/user/lacey/regional_atlas_cmaq/dailyaverage/*' + i + '*NO2*.nc'))
    wrf_cmaq = xr.open_mfdataset(filelist, concat_dim = 'None', combine = 'nested')
    wrf_df = wrf_cmaq.to_dataframe()
    
    wrf_df = wrf_df.reset_index()
    wrf_df = wrf_df.drop('None',axis=1).drop('Time',axis=1).drop('south_north',axis=1).drop('west_east',axis=1).rename(columns={'NO2_daily_avg':'pred_WRF-CMAQ'})
    
    wrf_df.to_csv('/data0/shr/bne/jc_data/nox/daily/formatted/uncropped/WRF-CMAQ/WRF-CMAQ_no2_' + i + '_daily.csv')
