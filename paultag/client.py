import os

from paultag.service import Service


class PaulTagAPI(Service):
    def __init__(self, host=None, apikey=None):
        self.setup(host=host, apikey=apikey)

    def _get_object(self, entity_id, **kwargs):
        """
        Get an Object in the Open Civic Data API by it's ID, which
        is a valid API path from the root of the app. This method
        is the means through which all other detail methods hit the
        API.
        """
        return self._query("GET", entity_id, **kwargs)

    def _get_list(self, *args, **kwargs):
        """
        Get the list response from the Open Civic Data API by its
        API rest path. This method is the means through with all
        other list endpoints hit the API.
        """
        page = kwargs.get("page", 1)
        nkwargs = kwargs.copy()
        nkwargs['page'] = (page + 1)
        next_ = lambda: self._get_list(*args, **nkwargs)

        return self._query("GET", *args, **kwargs)

    # List methods.

    def _get_apikey(self):
        key = super(PaulTagAPI, self)._get_apikey()
        return key
