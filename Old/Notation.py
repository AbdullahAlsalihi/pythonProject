
import re

def example(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

example(1,2,3, name="Abdul", age=30)

def find_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = re.findall(email_pattern, text)
    return email

text = "Contact us at support@example.com and sales@example.org."
email = find_emails(text)
print(email)

