from mastodon import Mastodon

# Create an instance of the Mastodon class
mastodon = Mastodon(
    access_token='hhRvxq3zFpNPwe5V1qCb2ILZXZiXgXz-r25UtiYE_xA',
    api_base_url='botsin.space'
)

# Post a new status update
mastodon.status_post('Testititest')
