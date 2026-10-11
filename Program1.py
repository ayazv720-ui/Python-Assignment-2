import re

text = input("Enter text: ")

# Find email addresses
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|edu)', text)

# Extract complete email addresses
all_emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|edu)',
    text
)

# Remove duplicates using set
unique_emails = set(all_emails)

print("\nValid Emails:")
for email in sorted(unique_emails):
    print(email)

print("\nTotal Valid Emails:", len(unique_emails))