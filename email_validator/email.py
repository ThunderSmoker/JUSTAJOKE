from email_validator import validate_email, EmailNotValidError

email = input("Enter A email:")

try:
    email = validate_email(email).email
except EmailNotValidError as e:
    print(str(e))
    exit(0)
print("Valid!!")