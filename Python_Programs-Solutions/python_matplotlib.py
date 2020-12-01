import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt

#LINE PLOT
# x=np.arange(1,11)
# y=x*3
# 
# plt.plot(x,y)
# plt.title("Line Plot")
# plt.xlabel("x-label")
# plt.ylabel("y-label")
# 
# #changing line Aesthetics
# plt.plot(x,y,color='g',linestyle=":",linewidth=5)

#Adding two lines in the same plot
# x=np.arange(1,11)
# y1=2*x
# y2=3*x
# 
# plt.plot(x,y1,color='g',linestyle=":",linewidth=5)
# plt.plot(x,y2,color='r',linestyle="-",linewidth=3)
# plt.title("Line Plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid(True)

#Adding sub plots in the same screen

# x=np.arange(1,11)
# y1=2*x
# y2=3*x
# 
# plt.subplot(1,2,1) #subplot(1row,2col,index of subplot)
# plt.plot(x,y1,color='r',linestyle=":",linewidth=2)
# 
# plt.subplot(1,2,2)
# plt.plot(x,y2,color='g',linestyle=":",linewidth=2)
#plt.show()

#BAR PLOT
# student={"Bob":87,"Matt":56,"Sam":27,"Julie":78}
# names=list(student.keys())
# values=list(student.values())
# plt.barh(names,values,color='g')
# #Adding title and labels
# plt.title("Bar Plot")
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.show()

#SCATTER PLOT
# x=[10,20,30,40,50,60,70,80,90]
# y=[8,1,7,2,0,3,7,3,2]
# plt.scatter(x,y,marker="*",c="r",s=100)
# plt.show()

#Adding two markers in the same plot
# x=[10,20,30,40,50,60,70,80,90]
# a=[8,1,7,2,0,3,7,3,2]
# b=[7,2,5,6,9,1,4,5,3]
# plt.scatter(x,a,marker="*",c="r",s=100)
# plt.scatter(x,b,marker=".",c="b",s=200)
# plt.show()

#Adding sub-plots
# x=[10,20,30,40,50,60,70,80,90]
# a=[8,1,7,2,0,3,7,3,2]
# b=[7,2,5,6,9,1,4,5,3]
# plt.subplot(2,1,1)
# plt.scatter(x,a,marker="*",c="g",s=100)
# 
# plt.subplot(2,1,2)
# plt.scatter(x,b,marker=".",c="r",s=200)
# plt.show()

#HISTOGRAM
# data=[1,3,3,3,3,9,9,5,4,4,8,8,8,6,7]
# #plt.hist(data)
# #or
# plt.hist(data,color='g',bins=4)
# 
# plt.show()

#Working with dataset
# creating a sample dataframe 
# data = pd.DataFrame({'Brand' : ['Maruti', 'Hyundai', 'Tata', 
#                                 'Mahindra', 'Maruti', 'Hyundai', 
#                                 'Renault', 'Tata', 'Maruti'], 
#                     'Year' : [2012, 2014, 2011, 2015, 2012, 
#                             2016, 2014, 2018, 2019], 
#                     'Kms Driven' : [50000, 30000, 60000, 
#                                     25000, 10000, 46000, 
#                                     31000, 15000, 12000], 
#                     'City' : ['Gurgaon', 'Delhi', 'Mumbai', 
#                             'Delhi', 'Mumbai', 'Delhi', 
#                             'Mumbai','Chennai', 'Ghaziabad'], 
#                     'Mileage' : [28, 27, 25, 26, 28, 
#                                 29, 24, 21, 24]}) 
# 
# # displaying the DataFrame 
# print(data)
# plt.hist(data['Kms Driven'],bins=30,color='r')
# plt.show()

#reading csv file data
# info=pd.read_csv('data.csv')
# print(info.head())
# plt.hist(info['Class'],bins=30,color='r')
# plt.show()

#BOX PLOT
# one=[1,2,3,4,5,6,7,8,9]
# two=[1,2,3,4,5,4,3,2,1]
# three=[6,7,8,9,8,7,6,5,4]
# 
# data=list([one,two,three])
# print(data)
# 
# #plt.boxplot(data)

# VIOLIN PLOT
# plt.violinplot(data,showmedians=True)
# plt.show()

#PIE CHART
# fruit=['Apple','Orange','Mango','Papaya']
# quantity=[67,34,100,29]
# 
# #plt.pie(quantity,labels=fruit)
# #changing Aesthetics
# plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['yellow','grey','blue','pink'])
# plt.show()

#DOUGHNUT CHART
fruit=['Apple','Orange','Mango','Papaya']
quantity=[67,34,100,29]
plt.pie(quantity,labels=fruit,radius=1)
plt.pie([100],colors=['w'],radius=0.5)
plt.show()