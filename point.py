class Point:
    def __init__(self, position):
        self.__string_latitude, self.__string_longitude = position.split()
        self.__latitude = float(self.__string_latitude)
        self.__longitude = float(self.__string_longitude)

    def __repr__(self):
        return f"Point({self.__latitude}, {self.__longitude})"

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude
    
    def get_point_tuple(self):
        return (self.__latitude, self.__longitude)

if __name__ == '__main__':
    position = '37.623429 55.766557'
    point = Point(position)
    print("Test point object for Ring road, moscow")
    print("repr:", point)
    print("get_latitude:", point.get_latitude())
    print("get_longitude:", point.get_longitude())
    print("get_point_tuple", point.get_point_tuple())

