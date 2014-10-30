from ..service import Service


class TravelService(Service):
    def __init__(self):
        self.setup(host="http://localhost:8000/api/v1", apikey=None)

    def trips(self, who):
        return self._query("GET", "trips", who)['results']
