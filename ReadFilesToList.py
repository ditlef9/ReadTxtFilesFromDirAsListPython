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


class ReadFilesToList:

    # Initialize class -------------------------------- #
    def __init__(self):
        filters_list = [] # Generate list

        # Find all filters in "filters" directory
        for filename in os.listdir("filters"):
            with open(os.path.join("filters", filename), 'r') as f: # open in readonly mode
                #print(filename)
                filters_list.append(filename)

        # Read filters
        filters_include_list = []
        for filename in filters_list:
            print(filename)

            # Read filter
            f = open('filters/' + filename)  # Open file on read mode
            data_list = f.read().splitlines()  # List with stripped line-breaks
            f.close()  # Close file

            # Remove first line
            del data_list[0]

            # Loop trough list and remove

            # Append to existing filters list
            filters_include_list.append(data_list)


        # Print all keywords
        filters_include_length = len(filters_include_list)

        print("Lenght=", filters_include_length);
        #print("Filters=", filters_include)
        for filter in filters_include_list:
          print(filter)



    # Call class from other class --------------------- #
    def __call__(self):
        return self.filters_list
