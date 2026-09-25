# PLP Python Week 6 — Loops

## Files

- `times_table.py` — Asks the user for a number and prints its times-table from 1 to 10 using a `for` loop and f-strings.
- `skip_counter.py` — Prints the even numbers from 0 to 20 using a stepped `range()`, then counts down from 10 to 0 using a negative step.
- `loop_hospital.py` — Three broken loops, each fixed with a `# FIXED:` comment explaining the bug (an off-by-one `range()`, a `while` loop missing its decrement, and an accumulator reset inside the loop).
- `screenshots/` — Screenshots of each program's output.

## Off-by-one errors

An off-by-one error happens when a loop runs one time too many or too few, usually because you miscounted where it should start or stop — for example, `range(1, 10)` looks like it should print up to 10 but actually stops at 9, since `range()`'s stop value is exclusive. Remembering that `range(start, stop)` never includes `stop` itself is the habit that avoids this: if you want a number included, write it as `stop = target + 1` (or, for a countdown, `stop = target - 1`).