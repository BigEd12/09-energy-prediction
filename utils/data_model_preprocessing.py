import numpy as np
import pandas as pd

def add_wind_speed(df):
    """
    Input: DataFrame
    
    -Calculate and add wind speed in radians
    
    Output: DataFrame
    """
    return np.sqrt((df['U'] / 20) ** 2 + (df['V'] / 10) ** 2)

def wind_radians_degrees(df):
    """
    Input: DataFrame
    
    -Calculate and add wind speed in degrees
    
    Output: DataFrame
    """
    radians = np.arctan2(df['U'], df['V'])
    degrees = (np.degrees(radians) + 360) % 360
    return degrees

def direction_sector(df):
    """
    Input: DataFrame
    
    - Classify rows by wind direction
    - Add wind direction column
    
    Output: DataFrame
    """    
    if df['Direction (degrees)'] >= 315 or df['Direction (degrees)'] < 45:
        return 'North'
    elif df['Direction (degrees)'] >= 45 and df['Direction (degrees)'] < 135:
        return 'East'
    elif df['Direction (degrees)'] >= 135 and df['Direction (degrees)'] < 225:
        return 'South'
    else:
        return 'West'
    
def preprocessing(df):
    """
    Input: DataFrame
    
    - Run all preprocessing
    
    Output: DataFrame -> Four DataFrames (per sector)
    """    
    df['Speed (m/ps)'] = df.apply(add_wind_speed, axis=1)
    df['Direction (degrees)'] = df.apply(wind_radians_degrees, axis=1)
    df['Direction (sector)'] = df.apply(direction_sector, axis=1)
    north_df = df[df['Direction (sector)'] == 'North']
    east_df = df[df['Direction (sector)'] == 'East']
    south_df = df[df['Direction (sector)'] == 'South']
    west_df = df[df['Direction (sector)'] == 'West']
    
    return north_df, east_df, south_df, west_df