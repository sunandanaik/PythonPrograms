#python_pandas_example
# importing the module 
import pandas as pd 

# creating a sample dataframe 
data = pd.DataFrame({'Brand' : ['Maruti', 'Hyundai', 'Tata', 
                                'Mahindra', 'Maruti', 'Hyundai', 
                                'Renault', 'Tata', 'Maruti'], 
                    'Year' : [2012, 2014, 2011, 2015, 2012, 
                            2016, 2014, 2018, 2019], 
                    'Kms Driven' : [50000, 30000, 60000, 
                                    25000, 10000, 46000, 
                                    31000, 15000, 12000], 
                    'City' : ['Gurgaon', 'Delhi', 'Mumbai', 
                            'Delhi', 'Mumbai', 'Delhi', 
                            'Mumbai','Chennai', 'Ghaziabad'], 
                    'Mileage' : [28, 27, 25, 26, 28, 
                                29, 24, 21, 24]}) 

# displaying the DataFrame 
print(data)
# selecting rows from 1 to 4 and columns from 2 to 4 
#print(data.iloc[1 : 5, 2 : 5]) #excluding last limit of row and col

# selecting cars with brand 'Maruti' and Mileage > 25 
#print(data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)])

# selecting range of rows from 2 to 5 
#print(data.loc[2 : 5])

#print(data.loc[0:3,("Brand","Year")])

#Pandas more functions
#print(data.min())

#print(data.max())

print(data.mean())

print(data.median())

#create user-defined function and apply to the data
def half(s):
    return s*0.5

print(data[['Kms Driven','Mileage']].apply(half))

#to do categorical count
print(data['City'].value_counts())

#To sort data with respect to any column
print(data.sort_values(by='Year'))