from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class List(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(List, self).__init__(url, api_key)

    def add(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'list_add',
            self.output
        )
        response = rq.post(rq_url, data=post_data)
        return response

    def delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_delete',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def delete_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_delete_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'list_edit',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def field_add(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'list_field_add',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def field_delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_field_delete',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def field_edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'list_field_edit',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def field_view(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_field_view',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def list_(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def paginator(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_paginator',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def view(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'list_view',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response


"""
    ## add
    #list1 = {
    #    'name': 'The List',
    #    'sender_name': 'John Smith',
    #    'sender_addr1': 'Bd. MK',
    #    'sender_city': 'Bucharest',
    #    'sender_zip': '123456',
    #    'sender_country': 'Romania'
    #}
    #print ac.api('list/add', list1)

    ## delete
    #print ac.api('list/delete?id=2')

    ## delete list
    #print ac.api('list/delete?id=1,2')

    ## edit
    #list1 = {
    #    'id': 11,
    #    'name': 'The List Edited',
    #    'sender_name': 'John Smith',
    #    'sender_addr1': 'Bd. MK',
    #    'sender_city': 'Bucharest',
    #    'sender_zip': '123456',
    #    'sender_country': 'Romania'
    #}
    #print ac.api('list/edit', list1)

    ## field_add
    #field = {
    #    'title': 'My Field',
    #    'type': 1,
    #    'req': 1,
    #    'show_in_list': 1,
    #    'perstag': '%PERS_11%',
    #    'p[11]': 11,
    #    'options[label]': 'value'
    #}
    #print ac.api('list/field_add', field)

    ## field delete
    #print ac.api('list/field_delete?id=7')

    ## field_edit
    #field = {
    #    'id': 7,
    #    'title': 'My Field Edited',
    #    'type': 1,
    #    'req': 0,
    #    'show_in_list': 1,
    #    'perstag': '%PERS_11%',
    #    'p[11]': 11,
    #    'options[label]': 'value'
    #}
    #print ac.api('list/field_edit', field)

    ## field view
    #print ac.api('list/field_view?ids=7')

    ## list
    #print ac.api('list/list?ids=11,1,10')

    ## paginator
    #print ac.api('list/paginator?sort=&offset=0&limit=20&filter=0&public=0')

    ## view
    #print ac.api('list/view?id=1')
"""
