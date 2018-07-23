from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Form(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Form, self).__init__(url, api_key)

    def getforms(self, params, post_data={}):
        rq_url = fmt_noparams(
            self.url,
            'form_getforms',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def html(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'form_html',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response


"""
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## getforms
    #print ac.api('form/getforms')

    ## html
    #print ac.api('form/html?id=1142')
"""
