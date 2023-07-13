import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tireWear = [0.5, 0.5, 0.5, 0.9]
        tires = CarriganTire(tireWear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tireWear = [0.5, 0.5, 0.5, 0.8]
        tires = CarriganTire(tireWear)
        self.assertFalse(tires.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        tireWear = [0.8, 0.7, 0.8, 0.7]
        tires = OctoprimeTire(tireWear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tireWear = [0.8, 0.7, 0.7, 0.7]
        tires = OctoprimeTire(tireWear)
        self.assertFalse(tires.needs_service())
