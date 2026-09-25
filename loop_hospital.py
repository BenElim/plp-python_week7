"""Part C - Loop Hospital
Three sick loops, diagnosed and fixed.
"""

# --- Patient 1: should print 1 to 10, but stops early ---
# FIXED: range(1, 10) stops at 9 because the stop value is exclusive;
# changed it to range(1, 11) so the loop actually reaches 10.
print("Patient 1:")
for i in range(1, 11):
    print(i)

# --- Patient 2: should count down 3, 2, 1 - but never stops ---
# FIXED: n was never decreased inside the loop, so the condition n > 0
# stayed true forever; added n -= 1 so n counts down and the loop ends.
print("Patient 2:")
n = 3
while n > 0:
    print(n)
    n -= 1

# --- Patient 3: should add up 1+2+3+4+5 = 15, but prints the wrong total ---
# FIXED: total = 0 was inside the loop, so it reset to 0 on every
# iteration instead of accumulating; moved it outside the loop.
print("Patient 3:")
total = 0
for i in range(1, 6):
    total = total + i
print(total)