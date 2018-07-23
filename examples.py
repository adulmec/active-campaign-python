from activecampaign import ActiveCampaign

# url provided to you by ActiveCampaign
base_url = '<your url>'
# api key provided to you by ActiveCampaign
api_key = '<your api_key>'

ac = ActiveCampaign(base_url,  api_key)
print(ac.api('account/view'))
