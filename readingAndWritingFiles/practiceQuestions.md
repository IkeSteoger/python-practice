# Practice Questions

### 1. What is a relative path relative to?

- The current (working) directory

### 2. What does an absolute path start with?

- `/`

### 3. What does `Path('C:/Users') / 'Al'` evaluate to on Windows?

- path object representing the file/directory of `C:/Users/Al`

### 4. What does `'C:/Users' / 'Al'` evaluate to on Windows?

- `C:/Users/Al`

### 5. What do the `os.getcwd()` and `os.chdir()` functions do?

- `getcwd()` gets current working directory, `chdir()` changes current working directory.

### 6. What are the `.` and `..` folders?

- `.` is current directory, `..` is parent directory

### 7. In `C:\bacon\eggs\spam.txt`, which part is the dir name, and which part is the base name?

- dir = eggs, base name = spam.txt

### 8. What are the three “mode” arguments that can be passed to the open() function?

- `r` read mode, `w` write mode, `a` append mode

### 9. What happens if an existing file is opened in write mode?

- Its contents are discarded and the file is treated as a new empty file!

### 10. What is the difference between the `read()` and `readlines()` methods?

- `read()` will read the whole file at once and print out the first characters that take up as many bytes as you specify, where `readlines()` will read and print out only the first characters that take up the bytes you specify

### 11. What data structure does a shelf value resemble?

- a dictionary
