# bollean mask for selecting data in dataframe
import pandas as pd

df = pd.read_csv('/some/path/')
mask = [False for _ in range(len(df))]
mask[3:7] = [True]*4

df[mask] # this is going to return only the rows in which the boolean value is True

# a more used approach is that one
mask = (df.loc[:,'col1'] < df.loc[:,'col2']) & (df.loc[:,'col3'] > 3) # This will also generate a boolean mask

# you can alse create a new column
df.loc[:,'new_column'] = df.loc[:,'col1']/df.loc[:,'col2']

# manipulating dataframe
df.rename(columns={'original_name': 'new_name'}) # new data frame renaming a column name
df.rename(index={0:'a', 1:'b', 2:'c'}) # new data frame renaming the rows

# to change the original dataframe
df.rename(index={0:'a', 1:'b', 2:'c'}, inplace=True)

# to come back to the original
df.rename(inplace=True)

# droping
df.drop(columns='col1')
df.drop(index=0)

# to change a given column to a specific type
df.col1.astype(int) # new column

# you can and a new row to a existing dataframe by
# 1. creating a dictionary corresponding to the new row
new_row = {'':'','':''}
# 2. by applying
df.append(new_row)
# 3. reseting the index
df.reset_index()

# replacing specific values
df.replace('original_value','new_one') # in the whole data frame

# Math
df.col1+1 # will result in incrementation of values

# applying functions to a data frame
df.apply(sum,axis=2) # this is the default, across columns

# Obs.: in this example we use a dataframe with two columns, the first labeled 'even' and the second labeled 'odd'.
# Each row of the dataframe contains an integer

# let us define our own function
def hundred_more(col):
    if sum(col) > 100:
        return 'Greter than 100'
    return 'Not greater than 100'

def label_evenodd(row):
    if row['even'] % 3 == 0:
        return True
    if row['odd'] % 3 == 0:
        return True
    return False

# to apply it
df.apply(hundred_more)
df.apply(label_evenodd,axis=1)

# we can also define a function that returns an iterable
def ret_list(row):
    ret_val = [False, False]
    if row['even'] > 6:
        ret_val[0] = True
    if row['odd'] > 6:
        ret_val[1] = True
    return ret_val

def div_three(row):
    if row % 3 == 0:
        return 'divisible by three'
    return 'NOT divisible by three'

# to apply we can do this
df.apply(ret_list, axis=1) # return an object which is a list of lists
df.apply(ret_list, axis=1, result_type='expand') # the result will be formated as a dataframe of two columns
df.even.apply(div_three)