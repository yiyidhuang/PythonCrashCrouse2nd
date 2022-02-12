import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_citiy_country_population(self):
        santiago_chile = city_country('santiago', 'chile', population=5_000_000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
