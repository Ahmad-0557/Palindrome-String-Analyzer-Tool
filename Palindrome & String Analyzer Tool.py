userinput = input("Enter a string: ")
print(len(userinput), userinput.upper(), userinput.lower())
if userinput[::-1] == userinput:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")