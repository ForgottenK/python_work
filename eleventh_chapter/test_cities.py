import unittest
from city_functions import city_country
class CityTestCase(unittest.TestCase):
	"""测试city_functions"""

	def test_city_country(self):
		"""测试是否能够从city_country获取正确的返回值"""
		formatted_string = city_country('santiago', 'chile')
		self.assertEqual(formatted_string, 'Santiago, Chile')

	def test_city_country_population(self):
		"""测试是否能够从city_country获取带人口信息的返回值"""
		formatted_string = city_country('santiago', 'chile', 5000000)
		self.assertEqual(formatted_string, 'Santiago, Chile - population 5000000')

unittest.main()