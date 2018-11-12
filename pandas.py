
#Session 8: Assignment 1
#1) How-to-count-distance-to-the-previous-zero
#For each value, count the difference of the distance from the previous zero (or the start
#of the Series, whichever is closer) and if there are no previous zeros,print the position
# Consider a DataFrame df where there is an integer column {'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}
# The values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.
#import pandas as pd
#df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

#!/usr/bin/env python
# coding: utf-8
# In[1]:
mylist = [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
i = 0
y = []

for x in l:
    if x != 0:
        i = i + 1
    else:
        i = 0
    y.append(i)
y


Out[1]:[1, 2, 0, 1, 2, 3, 4, 0, 1, 2]
  


#2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a
#Series of random numbers.

# In[2]:

import numpy as np
mydti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(mydti)), index=mydti)
s

Out[2]:
2015-01-01    0.285151
2015-01-02    0.362307
2015-01-05    0.685471
2015-01-06    0.737332
2015-01-07    0.458355
2015-01-08    0.141911
2015-01-09    0.455301
2015-01-12    0.526278
2015-01-13    0.653731
2015-01-14    0.691939
2015-01-15    0.480330
2015-01-16    0.817594
2015-01-19    0.667449
2015-01-20    0.192651
2015-01-21    0.272776
2015-01-22    0.852543
2015-01-23    0.567112
2015-01-26    0.113078
2015-01-27    0.105644
2015-01-28    0.744900
2015-01-29    0.417822
2015-01-30    0.622133
2015-02-02    0.081471
2015-02-03    0.463224
2015-02-04    0.654864
2015-02-05    0.975416
2015-02-06    0.606594
2015-02-09    0.958875
2015-02-10    0.101988
2015-02-11    0.535301
                ...   
2015-11-20    0.329431
2015-11-23    0.798501
2015-11-24    0.833220
2015-11-25    0.484855
2015-11-26    0.074337
2015-11-27    0.605465
2015-11-30    0.143751
2015-12-01    0.168188
2015-12-02    0.885129
2015-12-03    0.378361
2015-12-04    0.153456
2015-12-07    0.575323
2015-12-08    0.422731
2015-12-09    0.544545
2015-12-10    0.388016
2015-12-11    0.866112
2015-12-14    0.545066
2015-12-15    0.424560
2015-12-16    0.876964
2015-12-17    0.519806
2015-12-18    0.274908
2015-12-21    0.404071
2015-12-22    0.824601
2015-12-23    0.457531
2015-12-24    0.188073
2015-12-25    0.832751
2015-12-28    0.628803
2015-12-29    0.696590
2015-12-30    0.701032
2015-12-31    0.760858
Freq: B, Length: 261, dtype: float64
      

#3) Find the sum of the values in s for every Wednesday

# In[3]:
s[s.index.weekday == 2].sum()

Out[3]:28.56350536137436
  
#4) Average For each calendar month
# In[4]:

avg_M=s.resample('M').mean()
avg_M

Out[4]:
2015-01-31    0.493264
2015-02-28    0.495887
2015-03-31    0.442868
2015-04-30    0.521585
2015-05-31    0.537034
2015-06-30    0.521567
2015-07-31    0.568609
2015-08-31    0.507287
2015-09-30    0.453464
2015-10-31    0.499880
2015-11-30    0.493434
2015-12-31    0.544238
Freq: M, dtype: float64
    
#5) For each group of four consecutive calendar months in s, find the date on which the
#highest value occurred.

# In[5]:

s.groupby(pd.Grouper(freq='4M')).idxmax()

Out[5]:
2015-01-31   2015-01-22
2015-05-31   2015-05-15
2015-09-30   2015-06-01
2016-01-31   2015-10-07
dtype: datetime64[ns]
