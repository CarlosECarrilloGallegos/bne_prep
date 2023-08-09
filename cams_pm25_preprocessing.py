import xarray as xr
import pandas as pd
import numpy as np

#path for code: /data0/shr/bne/jc_data/pm25

cams = xr.open_dataset('hourly/raw/CAMS/cams_pm25_daymean_2003_2022.nc')

time = ['2003','2004','2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

for i in time:
    cams_slice = cams.sel(time=slice(i + '-01-01T10:00:00.000000000',i + '-12-31T10:00:00.000000000'))
    cams_df = cams_slice.to_dataframe()
    cams_df = cams_df.reset_index()
    cams_df = cams_df.drop('bnds',axis=1).drop('time_bnds',axis=1).rename(columns={'pm2p5':'pred_cams'})
    
    cams_df['pred_cams'] = cams_df['pred_cams']*(1e9)
    
    cams_df.to_csv('/data0/shr/bne/jc_data/pm25/daily/formatted/uncropped/CAMS/cams_pm25_' + i + '_daily.csv')
    
