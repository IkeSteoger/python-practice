# Practice Questions

### 1. What is `[]`?

- an empty list

### 2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)

- `insert()` method inserts the specified value at the specified position. In this case, you would use `spam.insert(2, 'hello')` We use position 2 because the first position is considered 0, so the third position is 2.

## For the following three questions, let’s say `spam` contains the list `['a', 'b', 'c', 'd']`

### 3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?

- `'d'`

### 4. What does `spam[-1]` evaluate to?

- `'d'`

### 5. What does `spam[:2]` evaluate to?

- `['a', 'b']`

## For the following three questions, let’s say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`

### 6. What does `bacon.index('cat')` evaluate to?

- `1` (seeks the first occurance of `'cat'`)

### 7. What does `bacon.append(99)` make the list value in bacon look like?

- It appends `99` to the end of the list, making it `[3.14, 'cat', 11, 'cat', True, 99]`

### 8. What does `bacon.remove('cat')` make the list value in bacon look like?

- It removes the first occurance of `'cat'`, making it `[3.14, 11, 'cat', True, 99]`

### 9. What are the operators for list concatenation and list replication?

- `+` to concat two lists and `*` to replicate the list `x` number of times

### 10. What is the difference between the `append()` and `insert()` list methods?

- `insert()` asks for a specified position to insert the specified value. `append()` will just add the specified value to the end of the list.

### 11. What are two ways to remove values from a list?

- `clear()` will remove all items from list. `pop()` removes an item by index and get its value. `remove()` removes an item by value. `del` removes items by index or slice.

### 12. Name a few ways that list values are similar to string values.

- Both lists and strings have indexes & slices, and can be used in `for` loops, can be concatenated or replicated, and be used with the `in` and `not in` operators.

### 13. What is the difference between `lists` and `tuples`?

- Tuples are immutable objects and lists are mutable.

### 14. How do you type the tuple value that has just the integer value `42` in it?

- `(42,)` - trailing comma is mandatory

### 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

- you can call the `tuple()` function or the `list()` function 

### 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

- They contain references to the list values.

### 17. What is the difference between `copy.copy()` and `copy.deepcopy()`?

- `copy.copy()` doesn't create a copy of the nested objects, instead it just copies the references to the nested objects. While `copy.deepcopy()` copies all the nested objects recursively.
