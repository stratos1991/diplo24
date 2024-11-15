import numpy as np
import pandas as pd


# index should be DateTimeIndex
def missing_hourly_values(df: pd.DataFrame, start='2018-08-01 04:00:00',end='2022-09-15 09:00:00'):
    missingDatetimes = pd.date_range(start=start, end=end, freq='h').difference(df.index)
    missingDf = pd.DataFrame(index=missingDatetimes, data=np.ones(missingDatetimes.size))
    missingDfHours = missingDf.resample(rule='d').sum(min_count=1)
    missingDfHours.dropna(inplace=True)
    return missingDfHours
