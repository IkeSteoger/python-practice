# Practice Questions

### 1. What is the Unix epoch?

- It measures time by the number of seconds that have elapsed since 00:00:00 UTC on 1 January 1970, no adjustments are made for leap seconds.

### 2. What function returns the number of seconds since the Unix epoch?

- `time.time()`

### 3. How can you pause your program for exactly 5 seconds?

- `time.sleep(5)`

### 4. What does the `round()` function return?

- It will round a a float to the precision you specify. Pass in the number you want to round, plus an optional second argument respresenting how many digits after the decimal point you want to round it to. If you omit the second argument, it rounds your number to the nearest WHOLE integer.

### 5. What is the difference between a `datetime` object and a `timedelta` object?

- `datetime` is a fixed point in time. `timedelta` is a duration, independent of any point of time.

### 6. Using the `datetime` module, what day of the week was January 7, 2019?

- Monday

### 7. Say you have a function named `spam()`. How can you call this function and run the code inside it in a separate thread?

- `threadObj = threading.Thread(target=spam)`

### 8. What should you do to avoid concurrency issues with multiple threads?

- Make sure the code running in one thread does not read/write the same variables as code in another thread.
