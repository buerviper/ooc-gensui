from mastodon import Mastodon
import os, random


# Create an instance of the Mastodon class
mastodon = Mastodon(
    access_token='hhRvxq3zFpNPwe5V1qCb2ILZXZiXgXz-r25UtiYE_xA',
    api_base_url='botsin.space'
)

# Post a new status update
image = random.choice([x for x in os.listdir("images") if os.path.isfile(os.path.join("images", x))])

Mastodon.media_post(image, mime_type=None, description=None, focus=None, file_name=None, thumbnail=None, thumbnail_mime_type=None, synchronous=False)[source]
