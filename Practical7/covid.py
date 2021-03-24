import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/maoxinjie/IBI1_2020-21/Practical7")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:11:2,:])
# show all columns, and every second row between (and including) 0 and 10
covid_data.loc[:, "location"]
# all the rows & location column
is_Afghanistan = covid_data['location']=='Afghanistan'
is_Afghanistan.head()
# if the location is Afghanistan, then it is True.
covid_data[covid_data['location']=='Afghanistan']
# all the rows with location is Afghanistan
print(covid_data[covid_data['location']=='Afghanistan'].loc[:, "total_cases"])
covid_data[covid_data['location']=='World'].iloc[:, [0,2]]
world_new_cases = covid_data[covid_data['location']=='World'].iloc[:, [0,2]]
print(world_new_cases.describe())
print(world_new_cases.mean())
print(world_new_cases.median())
# the mean is 8254.326087 and the median is 2023.5. They are very different
world_new_cases.boxplot()
plt.title('world new cases')
plt.show()
world_dates = world_new_cases.iloc[:, 0]
world_new_cases2 = world_new_cases.iloc[:, 1]
print(world_new_cases2)
plt.plot(world_dates, world_new_cases2, 'b+')
# when change the 'b+' into 'r+', the color of the plot become red. "+"means the dots will present as "+", while "o" means it will present as round circles. When change it into 'bo', the plot then consists of blue solid circles.
plt.title('new cases worldwide')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
# change the x axis. show the date every 4 days. The rotation = -90, which makes the dates vertical with the x axis and become clearer.
plt.show()
china_new_cases = covid_data[covid_data['location']=='China'].iloc[:, 2]
uk_new_cases = covid_data[covid_data['location']=='United Kingdom'].iloc[:, 2]
plt.plot(world_dates, china_new_cases, 'b', label = 'China')
plt.plot(world_dates, uk_new_cases, 'r', label = 'UK')
plt.title(' comparing new cases in China and the United Kingdom')
plt.xlabel('date')
plt.ylabel('new cases')
plt.legend(loc = 'best')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
# the plot that compares the new cases in China and the United Kingdom.
world_new_deaths = covid_data[covid_data['location']=='World'].iloc[:, 3]
plt.plot(world_dates, world_new_cases2, 'b', label = 'new cases worldwide')
plt.plot(world_dates, world_new_deaths, 'r', label = 'new deaths worldwide')
plt.title('new cases and new deaths worldwide')
plt.xlabel('date')
plt.ylabel('amount of people')
plt.legend(loc = 'best')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
# the plot that shows the new cases and new deaths worldwide.
date = covid_data[covid_data['date']== '2020-03-31']
countries = date[covid_data['total_cases']<=10]
print(countries.iloc[:, [1,4]])
# it shows the countries that have not yet been more than 10 total infections as of 31 March