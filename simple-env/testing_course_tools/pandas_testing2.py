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