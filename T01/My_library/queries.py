from My_library import aux_functions

def load_database(path, db_type):
    data_types = {"Passengers": "passengers.csv", "Airports": "airports.csv",
                  "Flights": "flights.csv", "Travels": "flights-passengers.csv"}

    file = aux_functions.csvreader(path + data_types[db_type])
    return file

def filter_flights(flights, airports, attr, simbol, value):
    if attr == "date":
        for flight in flights:
            if aux_functions.date_comparer(flight[3], value, simbol):
                yield flight
    elif attr == "distance":
        airports_dict = {airport[0]: airport for airport in airports}
        for flight in flights:
            airport1 = flight[1]
            airport2 = flight[2]
            lat1 = float(airports_dict[airport1][2])
            long1 = float(airports_dict[airport1][3])
            lat2 = float(airports_dict[airport2][2])
            long2 = float(airports_dict[airport2][3])
            if aux_functions.haversine(lat1, long1, lat2, long2, simbol, value):
                yield flight

def filter_by_destiny(flights, icao):
    for flight in flights:
        if flight[2] == icao:
            yield flight

def filter_by_id(travels, ids):
    for travel in travels:
        if travel[0] in ids:
            yield travel

def filter_passengers(passengers, flights, travels, icao, start, end):
    flights_fd = filter_by_destiny(flights, icao)
    flights_fd = filter_flights(flights_fd, None, "date", "<", end)
    flights_fd = filter_flights(flights_fd, None, "date", ">", start)
    ids = [flight[0] for flight in flights_fd]
    travels = filter_by_id(travels, ids)
    passengers_ids = {travel[1] for travel in travels}
    for passenger in passengers:
        if passenger[0] in passengers_ids:
            yield passenger

def filter_passenger_by_age(passengers, age, lower = True):
    for passenger in passengers:
        if (int(passenger[3]) < age) == lower:
            yield passenger

def filter_airports_by_country(airports, iso):
    for airport in airports:
        if airport[4] == iso:
            yield airport

def filter_airports_by_distance(airports, icao, distance, lower = False):
    airports_dict = {airport[0]: airport for airport in airports}
    airport = airports_dict[icao]
    lat1 = float(airport[2])
    long1 = float(airport[3])
    if lower:
        simbol = "<"
    else:
        simbol = ">="
    for airport2 in airports_dict.values():
        lat2 = float(airport2[2])
        long2 = float(airport2[3])
        if aux_functions.haversine(lat1, long1, lat2, long2, simbol, distance):
            yield airport2

def favourite_airport(passengers, flights, travels):
    pass

def passenger_miles(passengers, airports, flights, travels):
    distances = {flight: distance for flight, distance in
                 aux_functions.flight_distances(airports, flights)}
    passengers_dict = {passenger[0]: 0 for passenger in passengers}
    for travel in travels:
        passengers_dict[travel[1]] += distances[travel[0]]
    return passengers_dict

def popular_airports(flights, airports, travels, topn, avg = False):
    pass

def airport_passengers(passengers, flights, travels, icao1, icao2, operation):
    pass

def furthest_distance(passengers, airports, flights, travels, icao, n):
    pass
