s=input("Enter a string:")
left_string=s[1:]+s[0]
right_string=s[len(s)-1]+s[0:len(s)-1]
print(left_string)
print(right_string)