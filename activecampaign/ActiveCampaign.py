from importlib import import_module
from .Connector import Connector

# formatters for making life easier, don't you want it that way?
fmt_params = '{}&api_action={}&api_output={}&{}'.format
fmt_noparams = '{}&api_action={}&api_output={}'.format


def get_mod(cls, parent):
    source_module = import_module(".{}".format(cls), parent)
    class1 = getattr(source_module, cls)  # get Subscriber
    return class1


class ActiveCampaign(Connector):

    def __init__(self, url, api_key, api_user='', api_pass=''):
        self.url = url
        self.api_key = api_key
        self.URL = url
        self.APIKEY = api_key
        super(ActiveCampaign, self).__init__(url, api_key, api_user, api_pass)

    def api(self, path, post_data={}):
        # IE: "contact/view"
        components = path.split('/')
        component = components[0]

        if '?' in components[1]:
            # query params appended to method
            # IE: contact/edit?overwrite=0
            method_arr = components[1].split('?')
            method = method_arr[0]
            params = method_arr[1]
        else:
            # just a method provided
            # IE: "contact/view
            if components[1]:
                method = components[1]
                params = ''
            else:
                return 'Invalid method.'

        # adjustments
        if component == 'branding':
            # reserved word
            component = 'design'
        elif component == 'sync':
            component = 'contact'
            method = 'sync'
        elif component == 'singlesignon':
            component = 'auth'

        # "contact" becomes "Contact"
        class1 = '{}'.format(component.capitalize())
        class1 = get_mod(class1, 'activecampaign')
        class1 = class1(self.URL, self.APIKEY)  # Subscriber()

        if method == 'list':
            # reserved word
            method = 'list_'

        if method in dir(class1):
            if post_data:
                return getattr(class1, method)(params, post_data)
            else:
                return getattr(class1, method)(params)
        return None

    # extra methods I created for shorthand scripting
    # get
    def _get_contact_by_id(self, cid=None):
        """Get a contact by ID

        Arguments:
            cid:str     contact/subscriber ID
        """
        response = self.api('contact/view?id={}'.format(cid))
        return response

    def _get_contact_by_email(self, email=None):
        """Get a contact by email

        Arguments:
            email:str     contact/company Email
        """
        response = self.api('contact/view?email={}'.format(email))
        return response

    # delete
    def _delete_contact_by_id(self, cid=None):
        """Delete a contact/company

        Arguments:
            cid:str     contact/susbscriber ID
        """
        response = self.api('contact/delete?id={}'.format(cid))
        return response

    # create
    def _create_contact(self, data=None):
        """Create a contact/company

        Arguments:
            data:dict   proper definition of a contact dict
        """
        response = self.api('contact/ad', post_data=data)
        return response
    # end contact section

    # create
    def _add_tags_by_id(self, cid=None, tag=None):
        """ Add tags by id for company/contact

        Arguments:
            cid:str         contact/susbscriber ID
            tags:list(str)  list of tags as strings
        """
        response = self.api('contact/tag_add',
                            post_data={'id': cid, 'tags':tag})
        return response

    # delete
    def _delete_tags_by_id(self, cid=None, tag=None):
        """ Delete a tag by a contact/susbscriber ID

        Arguments:
            cid:str         contact/susbscriber ID
            tags:list(str)  list of tags as strings
        """
        response = self.api('contact/tag_remove',
                            post_data={'id': cid, 'tags':tag})
        return response

    def _add_note_by_id(self, cid=None, note=""):
        """ Add a Note for a contact/company

        Arguments:
            cid:str     contact/susbscriber ID
            note:str    a note
        """
        data = {"id": cid, "note": note}
        response = self.api('contact/note_add?id={}'.format(cid),
                            post_data=data)
        return response

    # delete
    def _delete_note_by_id(self, nid=None):
        """ Delete a note by a note ID

        Arguments:
            nid:str     note ID to delete
        """
        response = self.api('contact/note_delete?noteid={}'.format(nid))
        return response
    # end contact components (properties, tags...)

    # list contacts
    def _list_contacts(self):
        """List all contacts

        """
        response = self.api('contact/list?ids=all')
        return response

    # list organizations, not very usefull but still
    def _list_orgs(self):
        """List all organizations

        """
        response = self.api('organization/list')
        return response
