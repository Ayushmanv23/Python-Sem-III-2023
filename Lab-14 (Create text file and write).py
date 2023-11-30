#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     30-11-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

with open("MyFile.txt", "w") as file:
    for i in range(3):
        line = input(f"Enter line {i + 1}: ")
        file.write(line + "\n")

print("Three lines have been written to MyFile.txt.")
