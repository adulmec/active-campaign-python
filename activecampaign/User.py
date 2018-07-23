from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class User(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(User, self).__init__(url, api_key)

    def add(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'user_add',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def delete_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'user_delete_list',
            self.output,
            params
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'user_delete',
            self.output,
            params
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'user_edit',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def list_(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'user_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def me(self, params, post_data={}):
        rq_url = fmt_noparams(
            self.url,
            'user_me',
            self.output
        )
        response = rq.get(rq_url)
        return response

    def view(self, params, post_data={}):
        if params.startswith('email='):
            action = 'user_view_email'
        elif params.startswith('username='):
            action = 'user_view_username'
        elif params.startswith('id='):
            action = 'user_view'
        rq_url = fmt_params(
            self.url,
            action,
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response


"""
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
##    user = {
##        'username': 'johnsmith',
##        'first_name': 'John',
##        'last_name': 'Smith',
##        'password': 'mypwd',
##        'password_r': 'mypwd',
##        'email': 'person@example.com',
##        'group[3]' : 3
##    }
##    print ac.api('user/add', user)

    ## delete_list
##    print ac.api('user/delete_list?ids=3,4')

    ## delete
##    print ac.api('user/delete?id=5')

    ## edit
##    user = {
##        'username': 'johnsmith',
##        'first_name': 'John',
##        'last_name': 'Smyth',
##        'password': 'mynwqpwd',
##        'password_r': 'mynewpwd',
##        'email': 'person@example.com',
##        'group[3]' : 3,
##        'id' : 6
##    }
##    print ac.api('user/edit', user)

    ## list
##    print ac.api('user/list?ids=1,6')

    ## me
##    print ac.api('user/me')

    ## view email
##    print ac.api('user/view?email=person@example.com')

    ## view username
##    print ac.api('user/view?username=johnsmith')

    ## view id
##    print ac.api('user/view?id=1')

"""
