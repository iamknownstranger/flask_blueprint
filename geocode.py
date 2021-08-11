import requests
import haversine as hs
from point import Point

class Geocode:
    def __init__(self, address, api_key):
        self.address = address
        self.api_key = api_key
        self.response = requests.get(
            f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={address}&lang=en_US&format=json')
        self.response_json = self.response.json()
        self.lower_corner = Point(self.response_json[
            'response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']['lowerCorner'])
        self.upper_corner = Point(self.response_json[
            'response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']['upperCorner'])
        self.point = Point(self.response_json['response']['GeoObjectCollection']
                           ['featureMember'][0]['GeoObject']['Point']['pos'])

    def __repr__(self):
        return f"Address(upper_corner{self.upper_corner}, lower_corner{self.lower_corner})"

    def get_point(self):
        return self.point

    def is_located_inside(self, other) -> bool:
        other_point = other.get_point()
        point_latitude = other_point.get_latitude()
        point_longitude = other_point.get_longitude()

        upper_corner_latitude = self.upper_corner.get_latitude()
        upper_corner_longitude = self.upper_corner.get_longitude()

        lower_corner_latitude = self.lower_corner.get_latitude()
        lower_corner_longitude = self.lower_corner.get_longitude()

        if point_latitude > lower_corner_latitude and point_latitude < upper_corner_latitude:
            if point_longitude > lower_corner_longitude and point_longitude < upper_corner_longitude:
                return True

        return False

    def get_distance(self, other):
        distance = hs.haversine(
            self.get_point().get_point_tuple(), other.get_point().get_point_tuple())
        return distance


if __name__ == '__main__':
    api_key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'
    origin_address = "New Delhi"
    destination_address = "Mumbai"
    another_address = "Parliament, New Delhi"

    origin_address_geocode = Geocode(origin_address, api_key)
    destination_address_geocode = Geocode(destination_address, api_key)
    another_address_geocode = Geocode(another_address, api_key)

    print("Tests for geocode objects")
    print("Repr:", origin_address_geocode)
    print("Point of origin address (get_point):", origin_address_geocode.get_point())
    print(f"Is {origin_address} located inside {destination_address} (is_located_inside): {origin_address_geocode.is_located_inside(destination_address_geocode)}")
    print(f"Is {origin_address} located inside {another_address} (is_located_inside): {origin_address_geocode.is_located_inside(another_address_geocode)}")
    print(f"Distance from {origin_address} to {destination_address} (get_distance): {origin_address_geocode.get_distance(destination_address_geocode):.2f} KM")
    print(f"Distance from {destination_address} to {origin_address} (get_distance): {destination_address_geocode.get_distance(origin_address_geocode):.2f} KM")
    print(f"Distance from {origin_address} to {another_address} (get_distance): {origin_address_geocode.get_distance(another_address_geocode):.2f} KM")
