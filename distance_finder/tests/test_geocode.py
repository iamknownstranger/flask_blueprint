import unittest
from ..geocode import Geocode


class TestGeocode(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGeocode, self).__init__(*args, **kwargs)
     
        self.__api_key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'
        self.origin_address = "New Delhi"
        self.destination_address = "Mumbai"
        self.another_address = "Parliament, New Delhi"

        self.origin_geocode = Geocode(self.origin_address, self.__api_key)
        self.destination_geocode = Geocode(
            self.destination_address, self.__api_key)
        self.another_geocode = Geocode(self.another_address, self.__api_key)

    def test_is_valid_address(self):
        is_valid_address = self.origin_geocode.is_valid_address
        self.assertEqual(True, is_valid_address)

    def test_is_located_inside_flase(self):
        is_located_inside = self.origin_geocode.is_located_inside(
            self.destination_geocode)
        self.assertEqual(is_located_inside, False)

    def test_is_located_inside_true(self):
        is_located_inside = self.origin_geocode.is_located_inside(self.another_geocode)
        self.assertEqual(is_located_inside, True)

    def test_get_distance(self):
        distance = self.origin_geocode.get_distance(self.destination_geocode)

        self.assertEqual(distance, 558.4986033306964)
    


if __name__ == '__main__':
    unittest.main()
