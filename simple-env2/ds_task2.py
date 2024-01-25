# Loading different files in python

# b:rail 1
# Loading a SQL file
import os
file_list = os.listdir(".")
for item in file_list:
    if item.find(".sql") > 0:
        item = os.path.join(os.path.abspath("."),item)
        break
# 2:rail 1

# b:rail 2a
# let us take the example of a sql file
sql_file = open(item) # with this method you will have to close latter
# sql_content = sql_file.read() # you will get a single string
sql_content = sql_file.readlines()
sql_file.close() # when done
# e:rail 2a

# b:rail 2b
# A better option is to 
with open("path") as sql_file:
    sql_content = sql_file.readlines() # no need to close, it is done under the hood
# e:rail b2