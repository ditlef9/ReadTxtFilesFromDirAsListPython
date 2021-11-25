###
#
# File: ReadFilesToList.py
# Version 1.0.0
# Date 14:28 25.03.2021
# Copyright (c) 2021 Ditlef
# License: http://opensource.org/licenses/gpl-license.php GNU Public License
#
###
import os
import re


class ReadFilesToList:

    # Initialize class -------------------------------- #
    def __init__(self):
        self.current = 0
        self.high = 0

        self.filenames_list = [] # Generate list of all txt files to read
        self.filters_list = [] # Generate list of all keywords separated with |

        # Find all filters in "filters" directory
        for filename in os.listdir("filters"):
            with open(os.path.join("filters", filename), 'r') as f: # open in readonly mode
                #print(filename)
                self.filenames_list.append(filename)

        # Read filters
        for filename in self.filenames_list:
            #print(filename)

            # Read filter
            f = open('filters/' + filename)  # Open file on read mode
            data_list = f.read().splitlines()  # List with stripped line-breaks
            f.close()  # Close file

            # Remove first line
            del data_list[0]

            # Loop trough list and remove double tabs
            count = 0
            for line in data_list:
                data_list[count] = re.sub("[\t ]{2,}", "|", line) # Make separator |

                # Append to existing filters list
                self.filters_list.append(data_list[count])

                count += 1

        # Count number of items in data_list and use it as high
        self.high = len(self.filters_list)

    # Call class from other class --------------------- #
    def __iter__(self):
        return self

    # Next for a for loop over keywords --------------- #
    def __next__(self): # Python 2: def next(self)
        self.current += 1
        if self.current < self.high:
            return self.filters_list
        raise StopIteration

    # Call class from other class --------------------- #
    def __call__(self):
        return self.filters_list
