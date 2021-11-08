
### Data import without Pandas can be difficult
### You would need to use Excel before that, to format the tables.
### Only numbers can be imported. Dates should be transformed to specific formats


##############################################################################
### Import data using Pandas
##############################################################################

import pandas as pd
import os
print(os.getcwd()) 

### you should import each function from pandas
### importing csv file

from pandas import read_csv
data1 = read_csv('lunch.csv')
print(data1)

### importing Excel file. can do both xls and xlsx

from pandas import read_excel
data2 = read_excel('lunch.xlsx', 'Sheet1')
print(data2)

##############################################################################
### Some basic operations
##############################################################################

print(data2.year)  ## print one variable
the_variable = data2.total_served
print(the_variable)
d = sum(data2.total_served)
print(d)
print('The sum of Sales for this lunch dataset is', d)

mimimum = min(the_variable)
maximum = max(the_variable)
print('The mimimum total served value is', mimimum, 'and the maximum is', maximum)

diff = the_variable - data2.avg_free
print(diff)

diff2 = data2.total_served - data2.avg_free
print(diff2)

### creating a new calculated column. just for testing (no economical sense)

data2['diff3'] = data2['total_served'] - data2['avg_free']
print(data2)

### creating an adjusted price (with the discount from perc_free_red)

data2['total_price'] = (data2['total_served']) - ((data2['perc_free_red'] / 
     100) * data2['total_served'])

print(data2)

### another way to add a column. Be carefull with the index. it would be a better 
### idea to make these calculations inside the dataframe.

data3 = data2
data3['sum'] = diff
print(data3[['year','diff3','sum']])
print(data3)

### Please note: use 1 bracket '[' to specify 1 column and 2 brackets '[[' for
### multiple columns. The number of brackets it's not equal to number of fields


##############################################################################
##################         Data export        ################################
##############################################################################

data3.to_excel('04_import&export.xlsx')

