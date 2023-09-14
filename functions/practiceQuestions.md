# Practice Questions

### 1. Why are functions advantageous to have in your programs?

- Because they can be called upon at anytime & will save you re-writing code over and over.

### 2. When does the code in a function execute: when the function is defined or when the function is called?

- When the function is called.

### 3. What statement creates a function?

- `def`

### 4. What is the difference between a function and a function call?

- the function is the `def` or defining of the function. function call is when you call upon the function like `spam()`

### 5. How many global scopes are there in a Python program? How many local scopes?

- One global Python scope per program execution. You can have as many local scopes as you define within functions.

### 6. What happens to variables in a local scope when the function call returns?

- They cease to exist or are forgotten.

### 7. What is a return value? Can a return value be part of an expression?

- `return` provides an output when it is called an executed. Yes it can be part of an expression!

### 8. If a function does not have a return statement, what is the return value of a call to that function?

- It defaults to return `None` - which is a special object in Python that represents an absence of value.

### 9. How can you force a variable in a function to refer to the global variable?

- Write `global spam` within your function to refer to the global variable of `spam`

### 10. What is the data type of `None`?

- `None` is a special built-in object within Python that represents absence of a value or a null value.

### 11. What does the `import areallyourpetsnamederic` statement do?

- imports the `areallyourpetsnamederic` module, if it exists in your python program.

### 12. If you had a function named `bacon()` in a module named `spam`, how would you call it after importing `spam`?

``` Python
import spam

spam.bacon()
```

### 13. How can you prevent a program from crashing when it gets an error?

- `try/except`

### 14. What goes in the `try` clause? What goes in the `except` clause?

- whatever function or code you want to try to execute goes within the `try` clause - the `except` clause should hold what will happen if an exception is met, as defined by the code
