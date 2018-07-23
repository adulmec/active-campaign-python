from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Group(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Group, self).__init__(url, api_key)

    def add(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'group_add',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def delete_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'group_delete_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'group_delete',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'group_edit',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def list_(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'group_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def view(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'group_view',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response


"""
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
    # group = {
    #    'title': 'second-test-group',
    #    'descript' : 'This group is created from API',
    #    'lists[1]' : 1,
    #    'pg_form_edit' : 1,
    #    'pg_contact_add' : 1,
    #    'pg_contact_delete' : 0
    # }
    # print ac.api('group/add', group)

    ## delete_list
    #print ac.api('group/delete_list?ids=4,5')

    ## delete
    #print ac.api('group/delete?id=6')

    ## edit
    # group = {
    #    'title': 'second-group',
    #    'id' : 7
    # }
    # print ac.api('group/edit', group)

    ## list
    #print ac.api('group/list?ids=1,7')

    ## view
    #print ac.api('group/view?id=7')
"""
