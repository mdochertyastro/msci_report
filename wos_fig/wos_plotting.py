# Data Setup

ml={2005:10813,2006:10082,2007:12492,2008:15204,2009:18199,2010:14813,
    2011:15664,2012:17528,2013:20997,2014:24921,2015:30733,2016:35689,
    2017:47101,2018:62509,2019:78678}

grav={2005:1614,2006:1872,2007:1916,2008:2039,2009:2144,2010:2512,
    2011:2783,2012:2773,2013:3322,2014:3723,2015:4038,2016:5377,
    2017:6511,2018:8961,2019:8849}

import matplotlib.pyplot as plt

years=ml.keys()
ml_vals=ml.values()
grav_vals=grav.values()

plt.figure(figsize=(4,3))
plt.plot(years,ml_vals)
plt.show()

