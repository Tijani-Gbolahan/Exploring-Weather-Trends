import pandas as pd
from matplotlib import pyplot as plt

#import the data
data = pd.read_csv("lagos data.csv")
print(data)

#calculate moving average
def MeanFunction(check, input):
    output = input.rolling(window = check, center=False, on = "year").mean().dropna()
    return output

average_span = 10
moving_avg = MeanFunction(average_span, data)

plt.figure(1, figsize = (10, 5))
plt.grid(True)
plt.plot(moving_avg['year'], moving_avg['mov_avg_city'], label='Lagos')
plt.legend(loc='upper left')
plt.xlabel("Year (C.E.)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Lagos ({} year moving average)".format(average_span))
plt.show()
plt.close()


plt.figure(2, figsize = (10, 5))
plt.grid(True)
plt.plot(moving_avg['year'], moving_avg['mov_avg_gbl'], label='Global', color='orange')
plt.legend(loc='upper left')
plt.xlabel("Year (C.E.)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Global values ({} year moving average)".format(average_span))
plt.show()
plt.close()


plt.figure(3, figsize = (10, 5))
plt.grid(True)
plt.plot(moving_avg['year'], moving_avg['mov_avg_city'], label='Lagos')
plt.plot(moving_avg['year'], moving_avg['mov_avg_gbl'], label='Global', color='orange')
plt.legend(loc='best')
plt.xlabel("Year (C.E.)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Lagos Vs  Global values ({} year moving average)".format(average_span))
plt.show()
plt.close()

