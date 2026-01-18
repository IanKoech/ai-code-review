# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re

def count_valid_emails(emails):
    if not isinstance(emails, list):
        return 0

    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    count = 0
    for email in emails:
        if isinstance(email, str):
            if re.match(email_regex, email.strip()):
                count += 1
                
    return count