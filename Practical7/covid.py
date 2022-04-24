import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#The code for importing the .csv file works
os.chdir("/Users/yaofeiran/Documents/GitHub/IBI1_2021-22/Practical7")
covid_data=pd.read_csv("full_data.csv")
# a represents the first and third columns from rows 10-20 (inclusive)
a=covid_data.iloc[10:21,[1,3]]
print(a)
# used a Boolean to show “total cases” for all rows corresponding to Afghanistan
b=covid_data.loc[covid_data['location']=='Afghanistan',"total_cases"]
print(b)

# used a Boolean to show 'date','new cases','new deaths' for all rows corresponding China
c=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]
c.to_csv('China.csv',index=False,encoding='gbk')#save above data,as China.csv

#read the information of new cases and deaths in China.csv
china_new_data=pd.read_csv("China.csv")
t4=china_new_data['new_cases']
t5=china_new_data['new_deaths']

#use numpy to calculate their Mean
m1=round(np.mean(t4),2)
m2=round(np.mean(t5),2)
print("Mean cases:",m1,"Mean deaths:",m2)

#whether they are similar?
if m1!=m2:
 print("they are different,which means people were cured. The proportion of new cases that kill the infected persion is",m2/m1)

#boxplot 
test=[t4,t5]#to have two boxplots,first combine them together
plt.boxplot(test,notch=False,vert=True,patch_artist=True)
plt.xticks([1,2],['cases','deaths'],rotation=0)
plt.title("China's new cases and deaths")
plt.show()

#plot cases over time.
t6=china_new_data['date']
plt.plot(t6,t4,'r+')
plt.show()

#plot cases and deaths
plt.plot(t6,t4,'r+')
plt.plot(t6,t5,'b+')
plt.legend(('new_cases','new_deaths'),loc='upper right')
#modulate x axis
plt.xticks(china_new_data.iloc[0:len(china_new_data):4,0],rotation=-90)
plt.show()


#question of place having less than 10 cases
G=covid_data.loc[covid_data['date'].str.contains("2020-03-31"),['location','total_cases']]
G.to_csv('a.csv',index=False,encoding='gbk')#save every places in a new file
a=pd.read_csv("a.csv")
b=a.loc[a['total_cases']<=10,"location"]
print("Places having cases no more than 10 are listed as follows:",b)



