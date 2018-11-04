#!/usr/bin/env python3

import urllib.request
email = "mymail"
password = 'mypassword'

# Set up authentication for gmail
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='mail.google.com',
                          uri='https://mail.google.com/',
                          user=email,
                          passwd=password)
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)

gmailurl = 'https://mail.google.com/gmail/feed/atom'
with urllib.request.urlopen(gmailurl) as page:
    contents = page.read().decode('utf-8')

ifrom = contents.index('<fullcount>') + 11
ito   = contents.index('</fullcount>')

fullcount = contents[ifrom:ito]

print('{} new emails'.format(fullcount))
