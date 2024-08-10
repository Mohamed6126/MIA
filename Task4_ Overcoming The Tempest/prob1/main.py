import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sn
df = pd.read_csv('Weather Dataset.csv')
#handling missing,duplicate and incorrect data
df.drop_duplicates(inplace=True)
df.sort_values(by=['Formatted Date'],ascending=True,inplace=True)
key = -2000
df = df[~df.isin([key]).any(axis=1)]
#creating plot
plt.figure(figsize=(12, 6))
df.plot(x='Formatted Date',y='Apparent Temperature (C)',kind='line')
plt.xlabel('Formatted Date')
plt.ylabel('Apparent Temperature (C)')
plt.title('Apparent Temperature Over Time')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#Creating scatter
plt.figure(figsize=(12, 6))
plt.scatter(x=df['Humidity'],y=df['Apparent Temperature (C)'])
plt.xlabel('Humidity')
plt.ylabel('Apparent Temperature (C)')
#creating histogram
plt.figure(figsize=(12, 6))
plt.hist(df['Apparent Temperature (C)'],bins=10)
#Creating heatmap
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], format='%Y-%m-%d %H:%M:%S.%f %z', errors='coerce',utc=True)
df['Month']=df['Formatted Date'].dt.month
print(df['Month'])
numeric_df = df.select_dtypes(include=[np.number])
cormat=numeric_df.corr()
sn.heatmap(cormat, annot=True, cmap='RdYlGn', linewidths=0.5, fmt='.2f')
plt.title('Heatmap of Correlation Matrix')
plt.show()