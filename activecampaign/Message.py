from .ActiveCampaign import (
    ActiveCampaign,
    fmt_params,
    fmt_noparams
)
import requests as rq


class Message(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        super(Message, self).__init__(url, api_key)

    def add(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'message_add',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def delete_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_delete_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_delete',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'message_edit',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def list_(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def template_add(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'message_template_add',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def template_delete_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_template_delete_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def template_delete(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_template_delete',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def template_edit(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'message_template_edit',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def template_export(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_template_export',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def template_import(self, params, post_data):
        rq_url = fmt_noparams(
            self.url,
            'message_template_import',
            self.output
        )
        response = rq.get(rq_url, data=post_data)
        return response

    def template_list(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_template_list',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def template_view(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_template_view',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response

    def view(self, params, post_data={}):
        rq_url = fmt_params(
            self.url,
            'message_view',
            self.output,
            params
        )
        response = rq.get(rq_url)
        return response


"""
if __name__ == '__main__':
    ac = ActiveCampaign(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)

    ## add
##    message = {
##        'format': 'mime',
##        'subject': 'Fetch at send: %s' % datetime.datetime.now(),
##        'fromemail': 'person@example.com',
##        'fromname': 'John Smith',
##        'reply2': 'reply2@example.com',
##        'priority': 3,
##        'charset': 'utf-8',
##        'encoding': 'quoted-printable',
##        'htmlconstructor': 'external',
##        'htmlfetch': 'http://example.com',
##        'htmlfetchwhen': 'send',
##        'textconstructor': 'external',
##        'textgetch': 'http://example.com',
##        'textfetchwhen': 'send',
##        'p[1]': 1
##    }
##    print ac.api('message/add', message)

    ## delete
##    print ac.api('message/delete?id=32')

    ## delete_list
##    print ac.api('message/delete_list?ids=30,31')

    ## edit
##    message = {
##        'id': 1,
##        'subject': 'Fetch at send: %s' % datetime.datetime.now(),
##        'fromemail': 'person@example.com',
##        'p[1]': 1
##    }
##    print ac.api('message/edit', message)

    ## list
##    print ac.api('message/list?ids=1,2')

    ## template_add
##    template = {
##        'name': 'My New Template',
##        'subject': 'New Subject',
##        'html': '<html><head><title>New Template</title></head><body><h1>
##        This template was added via the API<h1></body></html></html>',
##        'template_scope': 'all',
##        'tags[]': 'Holiday',
##        'p[1]': 1
##    }
##    print ac.api('message/template_add', template)

    ## template_delete
##    print ac.api('message/template_delete?id=35')

    ## template_delete_list
##    print ac.api('message/template_delete_list?ids=35,36,37')

    ## template_edit
##    template = {
##        'id': 54,
##        'name': 'My New Template',
##        'html': '<html><head><title>New Template</title></head><body><h1>
##        This template was added via the API<h1></body></html></html>',
##        'p[1]': 1
##    }
##    print ac.api('message/template_edit', template)

    ## template_export
##    print ac.api('message/template_export?ids[54]=54&type=xml')

    ## template_import
##    template = {
##        'names[0]': 'My Template Imported Test',
##        'template_scope2': 'all',
##        'urls[0]': 'http://example.com/template.xml'
##    }
##    print ac.api('message/template_import', template)

    ## template_import
##    template = {
##         'names[0]': 'My Template Imported Test',
##         'template_scope2': 'all',
##         'urls[0]': 'http://example.com/template.xml'
##     }
##    print ac.api('message/template_import', template)

    ## template_view
##    print ac.api('message/template_view?id=54')

    ## view
##    print ac.api('message/view?id=1')

    ## template_list
##    print ac.api('message/template_list?ids=76')

"""
