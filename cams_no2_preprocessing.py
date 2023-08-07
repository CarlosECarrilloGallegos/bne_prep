import xarray as xr
import pandas as pd
import numpy as np

cams = xr.open_dataset('CAMS/cams_no2_2003_2022/cams_daymean.nc')

time = ['2003','2004','2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

for i in time:
    cams_slice = cams.sel(time=slice(i + '-01-01T10:00:00.000000000',i + '-12-31T10:00:00.000000000'))
    cams_df = cams_slice.to_dataframe()
    cams_df = cams_df.reset_index()
    cams_df = cams_df.drop('bnds',axis=1).drop('time_bnds',axis=1).rename(columns={'no2':'pred_cams'})
    
    cams_df['pred_cams'] = cams_df['pred_cams']*((0.029/0.046)*(1e9))
    
    cams_df.to_csv('/data0/shr/bne/jc_data/nox/daily/formatted/uncropped/CAMS/cams_no2_' + i + '_daily.csv')
    
    
