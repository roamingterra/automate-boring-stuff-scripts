import pyperclip, re

# Get the text from the clipboard
text = pyperclip.paste()

# Find all phone numbers and email addresses in the text
phone_number_pattern = re.compile(r'''( # North American phone number patterns
(?:\+?\d+[\s]?)? # Country code + seperator(optional)
(?:\d\d\d) # Area code
(?:\s|\.|\-) # Separator 1
(?:\d\d\d) # First set of digits
(?:\s|\.|\-) # Separator 2
(?:\d\d\d\d) # Second set of digits
)''', re.VERBOSE)

mo_phone_numbers = phone_number_pattern.findall(text) # List of phone numubers

email_pattern = re.compile(r'''( # General email pattern
(?:[^@\s]*) # Mailbox name / username
(?:\@)
(?:[^@\s]*) # Sub domain. organization name or provider name.
(?:\.com|org|gov|ca) # Top level domain (domain category)
)''', re.VERBOSE)

mo_emails = email_pattern.findall(text) # List of emails

# Neatly format the matched strings into a single string to paste

if(len(mo_phone_numbers) == 0 and len(mo_emails) == 0): # Display message if no matches were found in the text
    print("No phone numbers or emails were found.")
else:  # Continue with formatting string if there is a match  
    phone_numbers_and_emails_string = ""
    phone_numbers_and_emails_string += "Phone numbers: " + ", ".join(mo_phone_numbers) # Add matched phone numbers to string
    phone_numbers_and_emails_string += ".\n\n" # Add ending period and two new lines
    phone_numbers_and_emails_string += "Emails: " + ", ".join(mo_emails) # Add matched emails to string
    phone_numbers_and_emails_string += "." # Add final period

    print(phone_numbers_and_emails_string)

    # Copy findings into the clipboard
    pyperclip.copy(phone_numbers_and_emails_string)
    print("\n\nPasted to clipboard.\n\n")


