from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Organization(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Organization, self).__init__(url, api_key)

    def list_(self, params):
        rq_url = fmt_params(self.url, 'organization_list',
                            self.output, params)
        response = rq.get(rq_url)
        return response
