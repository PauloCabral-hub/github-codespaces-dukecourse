# How to get the name of the directories in a given path
import os

directories = os.listdir('/some/dir')

# To retrieve a index of a given object in the list
directories.index('name_of_the_object')

# Let us work with dictionaries now
contacts = {'name':'paulo','last_name':'passos'}
contacts.get('missing_key','missing_message') # remember that this method has the advantage of not returning a error for non-existant keyvalues

# To loop through a dictionary 
dict = {'a': 'a@gmail.com', 'b': 'b@gmail.com'}

for item in dict:
    print(item) # print keys

for item in dict.values():
    print(item) # print values

for subj, email in dict.items():
    print(subj, email) # for both

