'''
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Assign a variable for the file to load and the path.
file_to_load = "Resources/election_results.csv"
# Open the election results and read the file.
election_data = open(file_to_load, 'r')
# To do: perform analysis.

# Close the file.
election_data.close()


file_to_load = "Resources/election_results.csv"
with open(file_to_load) as election_data:
     # To do: perform analysis.
     print(election_data)


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

# The data we need to retrieve.

# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote.

import os

    # FIRST WAY:
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

    # SECOND WAY (make sure to catch "import os"):
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson, ")

    # Write three counties to the file.
    txt_file.write("Countries in the Election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    '''


#ALL TOGETHER:
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Remove the heather row from the CSV file with next()
    headers = next(file_reader)
 
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)
