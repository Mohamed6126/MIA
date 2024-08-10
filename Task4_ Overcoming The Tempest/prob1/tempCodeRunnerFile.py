df.plot(x='Formatted Date',y='Apparent Temperature (C)',kind='line')
plt.xlabel('Formatted Date')
plt.ylabel('Apparent Temperature (C)')
plt.title('Apparent Temperature Over Time')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.tight_layout()
#Creating scatter