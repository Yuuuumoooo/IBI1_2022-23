#import the libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the working directory
os.chdir("/Users/qiuliyan/Desktop/IBI/IBI1_2022-23/Practical7")

#import the full_data.csv
covid_data = pd.read_csv("full_data.csv")

#show the second column from every 100th row from the first 1000 rows(in- clusive)
selected_data_1 = covid_data.iloc[0:1001:100,1]
print(selected_data_1)
##11 rows in total

#get the data of the total_cases in Afghanistan
my_raw=covid_data["location"]=="Afghanistan"
selected_data_2 = covid_data.loc[my_raw,"total_cases"]
print(selected_data_2)

#calculate the mean of new cases and new deaths on 2020.03.31
my_raw=covid_data["date"]=="2020-03-31"
new_data=covid_data.loc[my_raw,["location","new_cases","new_deaths"]]
print(np.average(new_data["new_cases"]))
print(np.average(new_data["new_deaths"]))

#plot boxplot
plt.boxplot(new_data["new_cases"])
plt.title("boxplot of new cases")
plt.show()
plt.boxplot(new_data["new_deaths"])
plt.title("boxplot of new deaths")
plt.show()

#plot new cases worldwide over time
world_dates=covid_data.drop_duplicates(subset="date",keep="first",inplace=False)
world_dates=world_dates.loc[:,"date"]

world=covid_data["location"]=="World"
world_new_cases=covid_data.loc[world,"new_cases"]

plt.plot(world_dates, world_new_cases,"b+")
plt.title("worldwide new cases over time")
plt.xlabel("date")
plt.ylabel("number")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=60)
plt.show()

#plot both new cases and new deaths worldwide over time
world_new_deaths=covid_data.loc[world,"new_deaths"]
plt.plot(world_dates, world_new_cases,"bo",label="new cases")
plt.plot(world_dates, world_new_deaths,"ro",label="new deaths")
plt.xlabel("date")
plt.ylabel("number")
plt.title("worldwide new cases and deaths over time")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=60)
plt.legend()
plt.show()

#How have new cases and total cases developed over time in the UK?
UK=covid_data["location"]=="United Kingdom"
UK_cases=covid_data.loc[UK,["new_cases","total_cases"]]
plt.plot(world_dates,UK_cases["new_cases"],"b*",label="new cases")
plt.plot(world_dates,UK_cases["total_cases"],"r*",label="total cases")
plt.xlabel("date")
plt.ylabel("number")
plt.legend()
plt.title("new and total cases in UK over time")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=60)
plt.show()
