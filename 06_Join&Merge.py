

##############################################################################
######################         JOIN & MERGE       ############################
##############################################################################

####creating 2 dataframes
import pandas as pd
data1 = {'id_person' : ['1', '2', '3', '4', '5'],
         'surname' : ['Ophelia', 'Lacie', 'Caridad', 'Loma','Davida'],
         'name' : ['Jerome', 'Deonna', 'Denita', 'Willene', 'Arlene']
        }
df_1 = pd.DataFrame(data1, columns = ['id_person', 'surname', 'name'])
print(df_1)

data2 = {'id_person' : ['6', '7', '8', '9', '10'],
         'surname' : ['Ophelia', 'Lacie', 'Caridad', 'Loma', 'Davida'],
         'name' : ['Jerome', 'Deonna', 'Denita', 'Willene', 'Arlene']
        }
df_2 = pd.DataFrame(data2, columns = ['id_person', 'surname', 'name'])
print(df_2)

### creating a 3rd dataset with a new column containing
### all individuals from dataset1 and dataset2
data3 = {'id_person' : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
         'Grade' : [9, 7, 6, 8, 9, 5, 3, 7, 8, 3]
        }
df_3 = pd.DataFrame(data3)
print(df_3)


### join 2 dataframes along row
### will add the rows from second dataframe to the first one
### will add rows
df_new = pd.concat([df_1, df_2])
print(df_new)

### join 2 dataframes along columns
df_new1 = pd.concat([df_1, df_2], axis = 1)
print(df_new1)
### will add the second dataset to the right of the first one

### join 2 datasets based on an id variable
df_new3 = pd.merge(df_new, df_3, on = 'id_person')
print(df_new3)

### merge funvtion. Code to be developed


