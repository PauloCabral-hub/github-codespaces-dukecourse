# Let us learn to work with json files
import json
import os

# We can translate a dictionary to .json given the similarities
telefone_list = {"Paulo": "(98)9501-0000", "Samara":"(98)9501-0001"}

# translating to jason
json_output = json.dumps(telefone_list)

# the other way around
loaded_output = json.loads(json_output)

# loading from an actual file
curr_path = os.path.abspath(".")
file_list = os.listdir(".")
for f in file_list:
    if f.find('.json') > 0:
        break

with open(os.path.join(curr_path,f)) as jfile:
    loaded_output = json.load(jfile) # attention is not loads.


# Now let us practice saving data to a file
data = {}
with open("another_jfile.json","w") as f:
    json.dump(data, f) # attention is not dumps