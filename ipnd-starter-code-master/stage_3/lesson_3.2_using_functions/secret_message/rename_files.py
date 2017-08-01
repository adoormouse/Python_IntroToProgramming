# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
import os
def rename_files():
    file_list = os.listdir(r"./prank/")
    print(file_list)
    saved_path = os.getcwd()

    print(saved_path)

    os.chdir(r"./prank/")

    for file_name in file_list:
        print("Origional: " + file_name)
        trans_table = file_name.maketrans("0123456789", "          ", "0123456789")
        new_file_name = file_name.translate(trans_table)

        # if there is no change, skip file
        if file_name != new_file_name:
            print("Renamed to: " + new_file_name)
            os.rename(file_name, new_file_name)
        else:
            print("Skipping, nothing to translate")

rename_files()