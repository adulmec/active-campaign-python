from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Campaign(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Campaign, self).__init__(url, api_key)

    def create(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'campaign_create',
            self.output
        )
        response = rq.post(rq_url, data=post_data)
        return response

    def delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_delete',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def delete_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_delete_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def list_(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def paginator(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_paginator',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_bounce_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_bounce_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_bounce_totals(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_bounce_totals',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_forward_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_forward_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_forward_totals(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_forward_totals',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_link_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_link_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_link_totals(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_link_totals',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_open_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_open_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_open_totals(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_open_totals',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_totals(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_totals',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_unopen_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_unopen_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_unsubscription_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_unsubscription_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def report_unsubscription_totals(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_report_unsubscription_totals',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def send(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_send',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def status(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'campaign_status',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response


"""
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## create
    sdate = datetime.datetime.now() + datetime.timedelta(hours=0, minutes=2)
    campaign = {
        'type': 'single',
        'name': 'testActiveCampaign: {}'.formatdatetime.datetime.now(),
        'sdate': time.strftime('%Y-%m-%d %H:%M:%S', sdate.timetuple()),
        'status': 1,
        'public': 1,
        'tracklinks': 'all',
        'trackreads': 1,
        'htmlunsub': 1,
        'p[1]': 1,
        'm[35]': 100
    }
    from time import time
    time2 = time()
    print ac.api('campaign/create', campaign)
    print 'diff2 = %.5f seconds' %(time() - time2)

    ## delete
##    print ac.api('campaign/delete?id=12')

    ## delete_list
##    print ac.api('campaign/delete_list?ids=1,2')

    ## list
##    print ac.api('campaign/list?ids=3,4')

    ## paginator
##    print ac.api('campaign/paginator?sort=&offset=0&limit=20&'
                   'filter=0&public=0')

    ## report_bounce_list
##    print ac.api('campaign/report_bounce_list?campaignid=3')

    ## report_bounce_totals
##    print ac.api('campaign/report_bounce_totals?campaignid=13&messageid=2')

    ## report_forward_list
##    print ac.api('campaign/report_forward_list?campaignid=13&messageid=2')

    ## report_forward_totals
##    print ac.api('campaign/report_forward_totals?campaignid=13&messageid=2')

    ## report_link_list
##    print ac.api('campaign/report_link_list?campaignid=13&messageid=2')

    ## report_link_totals
##    print ac.api('campaign/report_link_totals?campaignid=13&messageid=2')

    ## report_open_list
##    print ac.api('campaign/report_open_list?campaignid=13&messageid=2')

    ## report_open_totals
##    print ac.api('campaign/report_open_totals?campaignid=13&messageid=2')

    ## report_totals
##    print ac.api('campaign/report_totals?campaignid=13&messageid=2')

    ## report_unopen_list
##    print ac.api('campaign/report_unopen_list?campaignid=13&messageid=2')

    ## report_unsubscription_list
##    print ac.api('campaign/report_unsubscription_list?campaignid=13')

    ## report_unsubscription_totals
##    print ac.api('campaign/report_unsubscription_totals?campaignid=13&'
                   'messageid=2')

    ## report_send
##    print ac.api('campaign/send?campaignid=13&messageid=2&type=mime&'
                   'action=send&email=person@example.com')

    ## report_status
##    print ac.api('campaign/status?id=13&status=5')
"""
