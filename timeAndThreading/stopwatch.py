#! python3
# stopwatch.py - Simple stopwatch program!

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl+C to quit.')
input() # Press ENTER to begin.
print('Started.')
startTime = time.time() # Get the first lap's start time.
lastTime = startTime
lapNum = 1

# Start tracking the lap times.

try:
    while true:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # Reset the last lap time.
except KeyboardInterrupt:
    # Handle the Ctrl+C exception to keep its error from displaying.
    print('\nDone.')