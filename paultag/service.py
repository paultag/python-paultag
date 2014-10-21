import requests


class Service(object):
    """
    Helper methods for a given API Implementation.
    """

    def setup(self, apikey=None, host=None):
        """
        Configure the Service object's bits.

        The reason this isn't in a constructor is that we can
        continue to reload/change config during runtime without
        trying to manually invoke the superclass constructor.
        As such, we're explicitly exposing a setup method to
        configure the API Key and API Host.
        """
        self.apikey = apikey if apikey else self._get_apikey()
        self.host = host

        if host is None:
            raise ValueError("Bad Host!")

    def get_url(self, host, *args):
        """
        Construct the URL to query.
        """
        return "{}/{}/".format(
            host,
            "/".join(args)
        )

    def _query(self, method, *args, **kwargs):
        """
        Query the API given a path (*args), with params (**kwargs).
        """
        params = kwargs
        kwargs['apikey'] = self.apikey

        if 'fields' in kwargs:
            kwargs['fields'] = ",".join(kwargs.pop('fields'))

        response = requests.request(
            method,
            self.get_url(
                self.host,
                *args
        ), params=params)
        if response.ok:
            return response.json()
        raise ValueError(response.json())

    def _get_apikey(self):
        """
        """
        pass
