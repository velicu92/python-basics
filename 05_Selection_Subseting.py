
##############################################################################
######################   SELECTIONS / SUBSETING   ############################
##############################################################################

### read the data.
from pandas import read_excel, concat
employee = read_excel('Employee data.xls', 'Employee data')
print(employee)

### first option
subset1 = employee.loc[employee['gender'] == 'm']
print(subset1)
subset2 = subset1.loc[subset1['salary'] >= 30000]
print(subset2)
### check the number of rows
len(subset2.index)

### Second option, using operator '&'
subset_m =  employee[(employee.gender == 'm') & (employee.salary >= 30000)]
print(subset_m)
len(subset_m)

subset_f = employee[(employee.gender == 'f') & (employee.salary >= 30000)]
len(subset_f.index)


#### concatenation of 2 datasets.

dataset = concat([subset_m, subset_f], ignore_index = True)
len(dataset)

print(dataset)

dataset.to_excel('dataset.xls')
