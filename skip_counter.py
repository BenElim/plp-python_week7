"""Part B - Skip Counter
Prints even numbers from 0 to 20, then counts down from 10 to 0.
"""

print("Even numbers:")
# stop is 21 (exclusive) so that 20 itself is included
for i in range(0, 21, 2):
    print(i)

print("Countdown:")
# negative step counts down; stop is -1 (exclusive) so that 0 itself is included
for i in range(10, -1, -1):
    print(i)