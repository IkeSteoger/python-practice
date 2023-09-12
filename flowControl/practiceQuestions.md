# Practice Questions

### 1. What are the two values of the Boolean data type? How do you write them?

- `True` & `False`. Must use capital T or F.

### 2. What are the three Boolean operators?

- `and`, `or`, and `not`

### 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

- `True == True` returns True
- `True == False` returns False
- `False == True` return False
- `False == False` returns True

- `True and True` returns True
- `True and False` returns False
- `False and True` returns False
- `False and False` returns False

- `True or True` returns True
- `True or False` returns True
- `False or True` returns True
- `False or False` returns False

- `not True` returns False
- `not False` returns True

### 4. What do the following expressions evaluate to?

``` Python
(5 > 4) and (3 == 5)
// False
not (5 > 4)
// True
(5 > 4) or (3 == 5)
// False
not ((5 > 4) or (3 == 5))
// True
(True and True) and (True == False)
// False
(not False) or (not True)
// True
```

### 5. What are the six comparison operators?

- `==` is Equal To
- `!=` is Not Equal To
- `<` is Less Than
- `>` is Greater Than
- `<=` is Less Than or Equal To
- `>=` is Greater Than or Equal To

### 6. What is the difference between the equal to operator and the assignment operator?

`==` equal operator checks if the two are equal. `=` assignment operator assigns the value to the variable

### 7. Explain what a condition is and where you would use one.

Conditions are Logical conditions from mathematics. You would use one most commonly in "if" statements.

### 8. Identify the three blocks in this code:

``` Python
spam = 0
```

- This block assigns spam to 0

``` Python
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
```

- This block checks if spam is equal to 10. if so, print eggs! or if its greater than 5, if so print bacon! any other number, print ham.

``` Python
print('spam')
```

- print spam.

### 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

``` Python
if spam == 1:
    print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')
```

### 10. What keys can you press if your program is stuck in an infinite loop?

- Ctrl + C

### 11. What is the difference between break and continue?

- `break` alters the flow of the loop by terminating once a specific condition is met
- `continue` skips the remaining code inside the loop for the current iteration only.

### 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

- The are all the same, because `range()` takes in three arguments, start value, stop value, and the step up value. The start value defaults to 0 and the step value defaults to 1.

### 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

``` Python
i = 1
for i in range(1, 11):
    print(str(i))
    i = i + 1
```

``` Python
i = 1
while i < 11:
    print(str(i))
    i = i + 1
```

### 14. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing spam?

``` Python
import spam

spam.bacon()
```
