from paultag.travel.service import TravelService


def print_trip(trip):
    print("""Trip ID: {id}
From:    {start}
Until:   {end}

{reason}
    """.format(**trip))


travel = TravelService()
for trip in travel.trips("tag"):
    print_trip(trip)
