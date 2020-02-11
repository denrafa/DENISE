from unittest import TestCase

from demo import Demo
class TestCalculator(TestCase):
    def test_add(self):
        self.demo = Demo()
        self.assertEqual(self.demo.add(3, 4), 7)

    def test_multiply(self):
       self.fail()

