# launchlinks.py - Launches all links from a webpage in separate tabs.
# This is done by copying the contents of a webpage to the clipboard,
# then running this script

import webbrowser, pyperclip, re

# Get contents from clipboard
contents = pyperclip.paste()

# Make use of regex to match all URLs and store them in a list
url_pattern = re.compile(r'''(
(https://)? # https:// -> optional
(www\.)? # www. -> optional
([^\s\n]+) # The rest of the url before the top-level domain -> not optional
(\.[a-z]+) # top-level domain -> not optional
([^\s\n]*) # The rest of the url after the top-level domain -> optional
)''', re.VERBOSE)

mo_urls = url_pattern.findall(contents)

# Open all URLs (make use of a loop)
for url in mo_urls:
    print('launching url ' + url[1] + url[2] + url[3] + url[4] + " ...")
    webbrowser.open(url[0])
    
