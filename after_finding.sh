#!/bin/bash

# Start by creating a list of files
touch /tmp/somefile{0..10}.txt

# Then you can perform the search
find /tmp -name somefile* -type f -print

# Now to remove the files
find /tmp -name somefile* -type f -print | xargs /bin/rm -f

# Some things to know:
# mdfind (MacOS) enables you to look for files created in a data range (with less work).
# Use xargs with the option that makes it human readable.
