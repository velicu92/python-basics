## Import modules.

import pandas as pd 

##creating a dataframe

data = {'first_name' : ['Bruce', 'Clark'],
        'last_name' : ['Wayne', 'Kent'],
        'YearOfBirth' : [1939, 1938],
        'Nr_exams' : [5, 4]
        }
print(data)

##transform to dataframe with .DataFrame command
df = pd.DataFrame(data, index = [1,2])
print(df)

## Operations with DataFrames:

print(df['first_name']) ### View 1 column
print(df[['first_name','Nr_exams']])  ## View 2 columns
data2 = df[['first_name','Nr_exams']] ## subsetting a dataframe
print(data2)

print(df[:1]) ### View first row (can be more than 1 row to view)
print(df[df['Nr_exams'] > 4]) ### View all rows with Ne_exams > 4
print(df.loc[1])  ## View 1 row. Should specify the index
print(df.loc[2,'YearOfBirth'])  ### View values of df using row and column

### saving dataframes.

df.to_csv('df.csv')
data2.to_csv('data2.csv')
df.to_excel('df.xlsx')

df.loc[3] = ['Barry','Allen', 1940, 2]  ## adding a row
print(df)
subset1 = df.drop([3])  ## deleting a row by index
print(subset1)
subset1 = subset1.drop('Nr_exams', axis = 1)  ### deleting a column. 
                        ##  axis = 1 proves that we are reffering to a column
print(subset1)

subset2 = df.drop(df.columns[[1,3]], axis = 1, inplace = False)
print(df)
print(subset2)  ### drops columns 1 and 3. (remember, first row = 0)

subset3 = df[df.last_name != 'Kent']  ## drops the line where las_name != 'Kent'
print(subset3)

subset4 = df[df.first_name == 'Kent']  ## keep the rows with first_name = 'Kent'
print(subset4)

sub_index = df.drop(df.index[1])
print(sub_index)

### NOTE: indexes in python start from 0


##############################################################################
####################    Search in Data Frame    ##############################
##############################################################################

import pandas as pd
data = {'score': [3,3,3,3]}
df = pd.DataFrame(data)
print(df)


### First IF
if (df.score == 3).any():
    print('Does any cells equal 3? Yes!')
else:
    print('Does any cells equal 3? No!')

### Second IF
if (df.score == 3).all():
    print('Are all cells equal 3? Yes!')
else:
    print('Are all cells equal 3? No!')
    
    