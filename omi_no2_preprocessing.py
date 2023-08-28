import xarray as xr
import pandas as pd
import numpy as np
import glob

time = ['2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

for i in time:
    filelist = glob.glob('/data0/shr/bne/jc_data/nox/daily/raw/AURA_fin/Daily/' +i+ '/*.h5')
    omi_v4 = xr.open_mfdataset(filelist, concat_dim = 'None', combine = 'nested')
    omi_v4_df = omi_v4.to_dataframe()
    omi_v4_df_conus = omi_v4_df.query('Latitude >24.5 and Latitude <49.5 and Longitude > -124.75 and Longitude < -66.75')
    omi_v4_df_conus = omi_v4_df_conus.reset_index()
    omi_v4_df_conus = omi_v4_df_conus.drop('GMI_SurfNO2',axis=1).drop('GMI_SurfNO2_2pm',axis=1).drop('phony_dim_0',axis=1).drop('phony_dim_1',axis=1).drop('OMI_SurfNO2_2pm',axis=1).rename(columns={'OMI_SurfNO2':'pred_OMIv4', 'None':'Day'})
    
    #Replace fill values with NANs
    omi_v4_df_conus = omi_v4_df_conus.mask(omi_v4_df_conus < -200)
    
    omi_v4_df_conus.to_csv('/data0/shr/bne/jc_data/nox/daily/formatted/CONUS/OMI_v4/OMI_no2_' + i + '_daily.csv')
