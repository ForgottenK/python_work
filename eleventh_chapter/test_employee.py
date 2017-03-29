import unittest
from employee import Employee

class testEmployee(unittest.TestCase):

	def setUp(self):
		self.emp = Employee('frank', 'king', 200000)

	def test_give_default_raise(self):
		self.emp.give_raise()
		self.assertEqual(self.emp.salary, 205000)

	def test_give_custom_raise(self):
		self.emp.give_raise(10000)
		self.assertEqual(self.emp.salary, 210000)

unittest.main()