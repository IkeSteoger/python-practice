# Practice Questions

### 1. What are escape characters?

- They let you use characters that are otherwise impossible to put into a string.

> - `\'` prints as Single quote
> - `\"` prints as Double quote
> - `\t` prints as Tab
> - `\n` prints as Line Break
> - `\\` prints as Blackslash

### 2. What do the \n and \t escape characters represent?

- `\n` is Line break. `\t` is Tab.

### 3. How can you put a \ backslash character in a string?

- using `\\`

### 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

- Because you are using double quotes around the string so the single quote doesn't cause issues.

### 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

- You could use the triple single or double quotes to do multiline strings.

### 6. What do the following expressions evaluate to?

> - 'Hello, world!'[1]
> - 'Hello, world!'[0:5]
> - 'Hello, world!'[:5]
> - 'Hello, world!'[3:]

- 'e'
- 'Hello'
- 'Hello'
- 'lo, world!'

### 7.  What do the following expressions evaluate to?

> - 'Hello'.upper()
> - 'Hello'.upper().isupper()
> - 'Hello'.upper().lower()

- 'HELLO'
- True
- 'hello'

### 8. What do the following expressions evaluate to?

> - 'Remember, remember, the fifth of November.'.split()
> - '-'.join('There can be only one.'.split())

- ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
- 'There-can-be-only-one.'

### 9. What string methods can you use to right-justify, left-justify, and center a string?

- `rjust()` for right, `ljust()` for left, `center()` for center

### 10. How can you trim whitespace characters from the beginning or end of a string?

- you can use `strip()`, `rstrip()`, `lstrip()` methods