 # this is the canonical pandas alias
import pandas as pd

# creating a base dictionary for the dataframe
data = {
    'Name': [ 'Paulo' ],
    'Age': [ '34' ],
    'Profession': ['Biomedical']
    }

# creating the dataframe

df = pd.DataFrame(data)

# if we want to rename the columns of the dataframe
df.columns=['subject','years','working_activity']

# if we want to make a dataframe from a csv file
file_path = '/workspaces/github-codespaces-dukecourse/simple-env/testing_course_tools/universidades.csv'
df = pd.read_csv(file_path)

# inspecting dataframe
df.head() # by default, the argument is 5
df.tai() 
df.describe() # for statistics of your dataframe
df.mean() # just one of the statistics
df.std() # another

# to show multiple columns
df.columns(['col1', 'col2'])

# to show a column named col1
df.col1

# acessing the data from iloc method
df.iloc[0,0] # first row and first column respectively

# with loc methods you can use the name of the column
df.loc[0,['col1', 'col2']]