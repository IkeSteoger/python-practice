# Practice Questions

### 1. Write an `assert` statement that triggers an `AssertionError` if the variable spam is an integer less than `10`

- `assert(spam >= 10, 'The spam variable is less than 10')`

### 2. Write an `assert` statement that triggers an `AssertionError` if the variables `eggs` and `bacon` contain strings that are the same as each other, even if their cases are different (that is, `'hello'` and `'hello'` are considered the same, and `goodbye'`and `'GOODbye'` are also considered the same)

- `assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!'`

### 3. Write an `assert` statement that always triggers an `AssertionError`

- `assert False, 'This assertion always triggers.'`

### 4. What are the two lines that your program must have in order to be able to call `logging.debug()`?

- `import logging` and `logging.basicConfig(level=logging.DEBUG)`

### 5. What are the two lines that your program must have in order to have `logging.debug()` send a logging message to a file named `programLog.txt`?

- `import logging` and `logging.basicConfig(filename='programLog.txt', level=logging.DEBUG)`

### 6. What are the five logging levels?

- Debug, Info, Warning, Error, Critical

### 7. What line of code can you add to disable all logging messages in your program?

- `logging.disable(logging.CRITICAL)`

### 8. Why is using logging messages better than using `print()`to display the same message?

- You can disable logging messages in several ways and logging messages provide a timestamp.

### 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

- Step Over allows the application to execute the next action, if the action involves a call to an operation, it will not step into its implementation, instead it will step over.
- Step Into allows the application execute the next action, but if the action involves a call to an operation, it will step into the implementation.
- Step Out allows the application to execute until the currently executed implentation is returned.

### 10. After you click Continue, when will the debugger stop?

- At the next breakpoint.

### 11. What is a breakpoint?

- Its a point in which the debugger is instructed to stop at a particular location in the program, returning control of the debugger to the user.

### 12. How do you set a breakpoint on a line of code in Mu?

- `import pdb` and `set_trace()`
