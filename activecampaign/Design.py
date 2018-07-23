from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Design(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Design, self).__init__(url, api_key)

    def edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'branding_edit',
            self.output
        )
        response = rq.post(rq_url, data=post_data)
        return response

    def view(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'branding_view',
            self.output
        )
        response = rq.get(rq_url)
        return response


"""
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
    
    ## edit
    branding = {
        'id' : 1,
        'branding_url' : 'http://www.example.com/logo.png',
        'copyright' : 'off',
        'demo' : 'on',
        'footer_html' : 'html',
        'footer_html_valueEditor' : '',
        'groupid' :  3,
        'header_html' : 'html',
        'header_html_valueEditor' : '',
        'site_name' : 'Adulmec.ro',
        'logo_source' : 'url'
        
    }
    #print ac.api('branding/edit', branding)
    
    ## view
    print ac.api('branding/view')
"""
