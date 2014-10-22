from ..service import Service


class TravelService(Service):
    def __init__(self):
        self.setup(host="http://localhost:8000", apikey=None)

    def trips(self, who):
        return self._query("GET", "trips", who)['active_trips']

    def trip(self, trip_id):
        return self._query("GET", "trip", trip_id)
