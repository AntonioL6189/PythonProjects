import matplotlib.pyplot as plt
import pandas as pd
from pytrends.request import TrendReq

trends = TrendReq()

trends.build_payload(kw_list=["Data Analystics"])
data = trends.interest_by_region()
data = data.sort_values(by="Data Analystics", ascending=False)
data = data.head(10)

data.reset_index().plot(x="geoName",
                        y="Data Analystics",
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
#plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Data Analystics'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15,12))
data['Data Analystics'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Data Analystics',
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()