import os

def trav_fsys():
    for root, directories, files in os.walk(os.path.abspath(".")): # so it is important to verify that the root is the single string returnedlasd
        #print(f"This is the files: {root}") # ignore this for a while
        #print(f"This is the directories: {root}")
        for _file in files:
            absolute_path = os.path.join(root, _file)
            print(f"file path: {absolute_path}")

if __name__ == "__main__":
    trav_fsys()