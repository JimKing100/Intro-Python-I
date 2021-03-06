# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


test = LatLon(38, -122)
print(test.lat, test.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return 'Location name {self.name}, \
latitude = {self.lat}, \
longitude = {self.lon}'.format(self=self)


test1 = Waypoint('Stop1', 37, -123)
print(test1.name, test1.lat, test1.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return 'Location name {self.name}, \
difficulty = {self.difficulty}, \
size = {self.size}, \
latitude = {self.lat}, \
longitude = {self.lon}'.format(self=self)


test2 = Geocache('Place1', 5, 100, 36, -123)
print(test2.name, test2.difficulty, test2.size, test2.lat, test2.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache('Newberry Views', 'diff 1.5', 'size 2', 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
