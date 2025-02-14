import re

# Read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Email extraction
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# URL extraction
url_pattern = r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?"
urls = re.findall(url_pattern, text)

# Phone number extraction
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
phones = re.findall(phone_pattern, text)

# Currency extraction
currency_pattern = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
prices = re.findall(currency_pattern, text)

# Hashtag extraction
hashtag_pattern = r"#\w+"
hashtags = re.findall(hashtag_pattern, text)

# Print results
print(f"Emails: {emails}")
print(f"URLs: {urls}")
print(f"Phone Numbers: {phones}")
print(f"Prices: {prices}")
print(f"Hashtags: {hashtags}")