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
pd.read_csv(file_path)