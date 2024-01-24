# The task here is to populate a dictionary with system information using some methods you need to get used to
import os

working_path = '/workspaces/github-codespaces-dukecourse/simple-env2'
path_items = os.listdir(working_path)
path_content = {'files':[], 'dirs':[]}

full_path_items = [os.path.join(working_path, item) for item in path_items]

for path in full_path_items:
    if os.path.isdir(path):
        path_content['dirs'].append(path)
    if os.path.isfile(path):
        path_content['files'].append(path)