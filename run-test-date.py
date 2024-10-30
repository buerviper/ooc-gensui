from mastodon import Mastodon
from pathlib import Path
import os
import datetime

# Access Mastodon instance
mastodon = Mastodon(
    access_token=os.environ['MASTODON_ACCESS_TOKEN'],
    api_base_url='botsin.space'
)

date = datetime.datetime.now()

if int(date.strftime("%d")) == 30 and int(date.strftime("%m")) == 10:
    post = "morgen ist halloween"
else:
    post = "heute ist nicht weihnachten"

print(date.strftime("%d")) 
print(date.strftime("%m"))

# Write a "Hello World!" post
image = mastodon.status_post(post) # this is the only required argument. you can either give the filename directly or use the "media_file" argument.
