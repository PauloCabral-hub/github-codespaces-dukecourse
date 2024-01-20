import pandas as pd 
import random

# Let us create a dataframe with a very bib size
leng = 100000000
data = {'a': (random.randint(0,100) for _ in range(leng)),
        'b':(random.randint(0,100) for _ in range(leng))}

df = pd.DataFrame(data)
df.std() # see how much time it takes to calculate

# now let us invite dask
import dask.dataframe as dd

ddf = dd.from_pandas(df, npartitions=3)

# calculations are done on the run and need a special method
ddf.std().compute() # compare how much time it takes

# to evaluate the graph of organization
ddf.dask