import requests as rq


class Connector(object):

    def __init__(self, url, api_key, api_user='', api_pass=''):
        self.output = 'json'
        self.base = ''

        if url != 'https://www.activecampaign.com':
            # not set reseller
            self.base = '/admin'
        if url[-1] == '/':
            # remove trailing slash
            url = url[:-1]

        if api_key:
            self.url = '{}{}/api.php?api_key={}'\
                       .format(url, self.base, api_key)
        else:
            self.url = '{}{}/api.php?api_user={}&api_pass={}'\
                       .format(url, self.base, api_user, api_pass)
        self.api_key = api_key

    def credentials_test(self):
        test_url = '{}&api_action=group_view&api_output={}&id=3'\
                       .format(self.url, self.output)
        return rq.get(test_url).status_code == 200


"""
if __name__ == '__main__':
    c = Connector(ACTIVECAMPAIGN_URL,  ACTIVECAMPAIGN_API_KEY)
    print c.credentials_test()
"""
