import unittest
from ..point import Point

class TestPoint(unittest.TestCase):

    def test_get_latitude(self):
        position = '37.62 55.76'
        point = Point(position)
        latitude = point.get_latitude()
        self.assertEqual(latitude, 37.62)

    def test_get_longitude(self):
        position = '37.62 55.76'
        point = Point(position)
        longitude = point.get_longitude()
        self.assertEqual(longitude, 55.76)

    def test_get_point_tuple(self):
        position = '37.62 55.76'
        point = Point(position)
        point_tuple = point.get_point_tuple()
        self.assertEqual(point_tuple, (37.62, 55.76))

if __name__ == '__main__':
    unittest.main()
