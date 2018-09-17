import csv
from math import radians, cos, sin, asin, sqrt
from datetime import datetime

def csvreader(path):
    with open(path, "r", encoding='utf-8' ) as file:
        reader = csv.reader(file, skipinitialspace=True)
        next(reader)
        for row in reader:
            yield row

def for_each(function, iterable):
    for elem in iterable:
        function(elem)

def n_of_queries(query):
    if len(query) > 1:
        if isinstance(query[1], list):
            return (1 + n_of_queries(query[1]))
    return 1


def distance(lat1, lon1, lat2, lon2):
    r = 3440

    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    distance = r * c
    return distance

def flight_distances(airports, flights):
    airports_dict = {airport[0]: airport for airport in airports}
    for flight in flights:
        airport1 = flight[1]
        airport2 = flight[2]
        lat1 = float(airports_dict[airport1][2])
        long1 = float(airports_dict[airport1][3])
        lat2 = float(airports_dict[airport2][2])
        long2 = float(airports_dict[airport2][3])
        yield flight[0], distance(lat1, long1, lat2, long2)

def haversine(lat1, lon1, lat2, lon2, simbol, value):
    d = distance(lat1, lon1, lat2, lon2)
    if simbol == "<":
        return d < value
    elif simbol == ">":
        return d > value
    elif simbol == "==":
        return d == value
    elif simbol == "!=":
        return d != value
    elif simbol == "<=":
        return d <= value
    else:
        return False

def my_parser(consulta):
    pass




def date_comparer(date1, date2, simbol):

    a = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    b = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    if simbol == "<":
        return a < b
    elif simbol == ">":
        return a > b
    elif simbol == "==":
        return a == b
    elif simbol == "!=":
        return a != b
    else:
        return False
