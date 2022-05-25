class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude}"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


bham_academy = Location(52.488647, -1.887249)

print(f"The Birminghma Academy is located at {bham_academy}")

# class Dog:
#     def __init__(self, age)
