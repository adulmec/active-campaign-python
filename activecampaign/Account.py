from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Account(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Account, self).__init__(url, api_key)

    def add(self, params, post_data={}):
        rq_url = fmt_noparams(
            self.url,
            'account_add',
            self.output
        )
        response = rq.post(rq_url, data=post_data)
        return response

    def cancel(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'account_cancel',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def edit(self, params, post_data={}):
        rq_url = fmt_noparams(
            self.url,
            'account_edit',
            self.output
        )
        response = rq.post(rq_url, data=post_data)
        return response

    def list_(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'account_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def name_check(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'account_name_check',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def plans(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'account_plans',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def status(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'account_status',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def status_set(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'account_status_set',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def view(self, params, post_data={}):
        rq_url = fmt_noparams(
            self.url,
            'account_view',
            self.output
        )
        response = rq.get(rq_url)
        return response


"""
    ## view
    #print ac.api('account/view')
"""
