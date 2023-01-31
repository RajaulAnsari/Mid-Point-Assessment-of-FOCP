# Fundamental of Computer Programming

## Assignment: Task 4

### Task

A certain organisation has a policy concerning user passwords. To
be acceptable, a password must contain at least one letter, at
least one digit, and at least one standard punctuation character.
A senior developer has crafted the high quality code below, and the code
has been ruthlessly tested, so is known to be correct. Use it in a program
that prompts a user to enter a possible password and then displays whether or not
the password is acceptable

- Hints:
```py
def password_checker(password):
  from string import ascii_letters as letters, digits, punctuation
  has_letter = has_digit = has_punc = False
  for character in password:
    if character in letters:
      has_letter = True
    elif character in digits:
      has_digit = True
    elif character in punctuation:
      has_punc = True
return has_letter and has_digit and has_punc
```
