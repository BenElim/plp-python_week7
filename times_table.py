"""Part A - Times Table
Asks the user for a number and prints its times-table from 1 to 10.
"""

number = int(input("Enter a number: "))

# range(1, 11) so the loop includes 1 through 10 (range's stop value is exclusive)
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")