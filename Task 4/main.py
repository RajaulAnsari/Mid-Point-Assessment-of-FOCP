def password_checker(password):
    from string import ascii_letters as letters, digits, punctuation 
    has_letter = has_digit = has_punc = False
    length=len(character)
    for i in range(length):
        if character[i] in letters:
            has_letter = True
        elif character[i] in digits:
            has_digit = True
        elif character[i] in punctuation:
            has_punc = True
    if has_letter and has_digit and has_punc:
        print("Acceptable")
    else:
        print("Not acceptable")

if __name__=='__main__':
    character=input("Enter a possible password: ")
    password_checker(character)