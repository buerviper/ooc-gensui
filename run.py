from mastodon import Mastodon
from pathlib import Path
import os
import random
import yaml

# Create an instance of the Mastodon class
mastodon = Mastodon(
    access_token='hhRvxq3zFpNPwe5V1qCb2ILZXZiXgXz-r25UtiYE_xA',
    api_base_url='botsin.space'
)

# Choose a random photo out of the /images folder
photo = random.choice([x for x in os.listdir("images") if os.path.isfile(os.path.join("images", x))])

# Get name of photo without ending
name = Path("images/"+photo).stem

# Check if photo has a description
if os.path.exists("images/descriptions/"+name+".yml"):
    description_file = open("images/descriptions/"+name+".yml", "r")
    description = yaml.load(description_file, Loader=yaml.FullLoader)

# Post a new status update

def post_status_with_image(spoiler_warning, image_alt_text, post_text = "#suikoden", sensitivity = "False", language = "en"):
    os.chdir("images")
    media = mastodon.media_post(photo, "image/png", description = image_alt_text)
    mastodon.status_post(post_text, media_ids=[media['id']], spoiler_text = spoiler_warning, sensitive = sensitivity, language = language)

status = description["status"]
spoiler_warning = description["spoiler_warning"]
alt_text = description["description"]
language = description["language"]
sensitivity = description["sensitivity"]

post_status_with_image(spoiler_warning, alt_text, status, sensitivity, language)
