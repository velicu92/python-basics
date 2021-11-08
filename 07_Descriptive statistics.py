
##############################################################################
######################    Descriptive statistics  ############################
##############################################################################

import os
print(os.getcwd())
from pandas import read_excel

## open data
mydata = read_excel('Employee data.xls', 'Employee data')
len(mydata)

## print summary statistics for all numeric variables
print(mydata.describe())

### print statistics for 1 variable

### method 1:
var1 = mydata.salary
print(var1.describe())

### method 2 (A better way):
print(mydata.salary.describe())

### printing combined messages (median salary):
print('The median salary is', mydata.salary.median())

### printing empirical mode
from scipy.stats import mode
print(mode(mydata.salary))

### print skewness value (asymetry)
from scipy.stats import skew
print('The skewness of the salary is', skew(mydata.salary))

### print kurtosis value
from scipy.stats import kurtosis
print('The kurtosis of the salary is', kurtosis(mydata.salary))

