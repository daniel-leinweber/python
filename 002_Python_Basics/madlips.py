#!/usr/bin/env python3

# For a mad lips we need to concatenate strings
# Python provides multiple ways to do this.
#
# First: Using the + sign
# Second: Using the .format string function
# Third: Using a format string like f"{variable1} some text"

print("\nMad lips game")
print("#############")

# Ask user for input
adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
color1 = input("Color: ")
adjective3 = input("Adjective: ")
adjective4 = input("Adjective: ")
color2 = input("Color: ")
noun = input("Noun: ")

# Concatenate mad lips
madlips = f"\nSanta Claus is a {adjective1} man who wears a {adjective2} \
{color1} suit with a {adjective3} belt and a {adjective4} {color2} hat. \
Every Christmas, he rides a {noun} full of presents.\n"

# Display mad lips to user
print(madlips)
