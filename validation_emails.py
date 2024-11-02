import re
import email.utils

n = int(input())
pattern = r"^([a-zA-Z][a-zA-Z0-9\_\-\.]+)\@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
for _ in range(n):
    name, email_address = email.utils.parseaddr(input())
    if re.search(pattern, email_address):
        print(email.utils.formataddr((name, email_address)))