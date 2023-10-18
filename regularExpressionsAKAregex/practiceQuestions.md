# Practice Questions

### 1. What is the function that creates `Regex` objects?

- `re`

### 2. Why are raw strings often used when creating `Regex` objects?

- So that backslashes do not have to be escaped.

### 3. What does the `search()` method return?

- It returns the index (position) of the first match. It is case sensitive

### 4. How do you get the actual strings that match the pattern from a `Match` object?

- Pass the string you want to search into the Regex object's search method. `re.search('test')`

### 5. In the regex created from `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, what does group `0` cover? Group `1`? Group `2`?

- Group 0 is an entire match, Group 1 covers the first set of parens, and group 2 coverts the second set of parens.

### 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

- You can use the escape character the `\`

### 7. The `findall()` method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

- Its based on the presence of capturing groups in the regex. If the regex contains one or more capturing groups, it returns a list of tuples.

### 8. What does the `|` character signify in regular expressions?

- It denotes alteration aka "OR"

### 9. What two things does the `?` character signify in regular expressions?

- It serves as a quantifier or a lookahead/lookbehind

### 10. What is the difference between the `+` and `*` characters in regular expressions?

- `+` means one or more of that element. `*` means zero or more of that element.

### 11. What is the difference between `{3}` and `{3,5}` in regular expressions?

- `{3}` means exactly three times. `{3,5}` means between 3 and 5 times.

### 12. What do the `\d`, `\w`, and `\s` shorthand character classes signify in regular expressions?

- `\d` is a digit. `\w` is a word character. `\s` is whitespace.

### 13. What do the `\D`, `\W`, and `\S` shorthand character classes signify in regular expressions?

- These are the negated versions of the lowercase. So `\D` means everything that ISN'T a digit.

### 14. What is the difference between `.*` and `.*?`?

- `.*` is a greedy quantifier that will match the longest possible sequence of characters that satisfy the regex. the `.*?` is a non-greedy/lazy version that matches the shortest possible sequence of characters that satisfy the regex.

### 15. What is the character class syntax to match all numbers and lowercase letters?

- `[0-9a-z]`

### 16. How do you make a regular expression case-insensitive?

- using `re.I` or `re.IGNORECASE` inside of the `re.search()` method

### 17. What does the `.` character normally match? What does it match if `re.DOTALL` is passed as the second argument to `re.compile()`?

- the `.` normally matches any character except a newline character. the `re.DOTALL` the dot matches any character, including new line. this makes the dot match any character in the input string, making it more inclusive.

### 18. If `numRegex = re.compile(r'\d+')`, what will `numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` return?

- X drummers, X pipers, five rings, X hens

### 19. What does passing `re.VERBOSE` as the second argument to `re.compile()` allow you to do?

- It'll ignore whitespace and newline characters, and also allows you to add comments.

### 20. How would you write a regex that matches a number with commas for every three digits? It must match the following

> - '42'
> - '1,234'
> - '6,368,745'

### but NOT the following

> - '12,34,567'
> - '1234'

- `^\d{1,3}(,\d{3})*$`

### 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

> - 'Haruto Watanabe'
> - 'Alice Watanabe'
> - 'RoboCop Watanabe'

### but NOT the following

> - 'haruto Watanabe' (where the first name is not capitalized)
> - 'Mr. Watanabe' (where the preceding word has a nonletter character)
> - 'Watanabe' (which has no first name)
> - 'Haruto watanabe' (where Watanabe is not capitalized)

- `^[A-Z][a-zA-Z]*\sWatanabe$`

### 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

> - 'Alice eats apples.'
> - 'Bob pets cats.'
> - 'Carol throws baseballs.'
> - 'Alice throws Apples.'
> - 'BOB EATS CATS.'

### but NOT the following

> - 'RoboCop eats apples.'
> - 'ALICE THROWS FOOTBALLS.'
> - 'Carol eats 7 cats.'

- `^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$`
