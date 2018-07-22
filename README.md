## Installation

You can install **active-campaign-python** from pypi

`pip install active-campaign-python`

## Example Usage

<pre>
from activecampaign import ActiveCampaign

# url provided to you by ActiveCampaign
base_url = '<your url>'
# api key provided to you by ActiveCampaign
api_key = '<your api_key>'

ac = ActiveCampaign(base_url,  api_key)
print(ac.api('account/view'))
</pre>

Each of the endpoint subclasses have comments at the bottom

## Prerequisites

1. A valid ActiveCampaign **hosted** account (trial or paid).

## That is all for now
