from paultag.travel.service import TravelService

travel = TravelService()
for trip in travel.trips("tag"):
    print(trip)
