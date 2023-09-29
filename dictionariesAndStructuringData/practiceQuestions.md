# Practice Questions

### 1. What does the code for an empty dictionary look like?

- `{}`

### 2. What does a dictionary value with a key 'foo' and a value 42 look like?

- `{'foo': '42'}`

### 3. What is the main difference between a dictionary and a list?

- Unlike lists, dictionaries are unordered. The first item in a list would be at index `[0]` but there is no first item in dictionaries. Thus you assign a key that has a value.

### 4. What happens if you try to access `spam['foo']` if spam is `{'bar': 100}`?

- You would get a `KeyError` error because the `'foo'` key doesn not exist.

### 5. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat'` in `spam` and `'cat'` in `spam.keys()`?

- There is no difference, both look for the term `'cat'` as a key in the dictionary.

### 6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat'` in `spam` and `'cat'` in `spam.values()`?

- checking for `'cat'` in spam would return all matching keys & values of `'cat'` whereas `spam.values()` would only check for `'cat'` within the values and not the keys.

### 7. What is a shortcut for the following code?

> ``` Python
> if 'color' not in spam:
>     spam['color'] = 'black'
> ```

``` Python
spam.setdefault('color', 'black')
```

### 8. What module and function can be used to “pretty print” dictionary values?

- `import pprint` is the module. `pprint.pprint()` is a function to pretty print dictionary values.
