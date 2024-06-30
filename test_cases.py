import unittest
from parking_lot import Parking_Lot, Car

class TestParkingLot(unittest.TestCase):

    def setUp(self):
        self.parking_lot = Parking_Lot(no_levels=3, no_lanes=2, no_slots=3)
        self.car1 = Car('ABC123', size=1)
        self.car2 = Car('XYZ789', size=2)
        self.car3 = Car('LMN456', size=1)
        self.car4 = Car('PQR321', size=3)
        self.car5 = Car('JKL654', size=2)

    def test_park_car(self):
        self.assertTrue(self.parking_lot.park_car(self.car1))
        self.assertTrue(self.parking_lot.park_car(self.car2))
        self.assertTrue(self.parking_lot.park_car(self.car3))
        self.assertTrue(self.parking_lot.park_car(self.car4))  
        self.assertTrue(self.parking_lot.park_car(self.car5))

    def test_remove_car(self):
        self.parking_lot.park_car(self.car1)
        self.parking_lot.park_car(self.car2)
        self.assertTrue(self.parking_lot.remove_car(self.car2))
        self.assertFalse(self.parking_lot.remove_car(self.car4))  # Should fail
        self.assertTrue(self.parking_lot.remove_car(self.car1))

    def test_park_car_after_removal(self):
        self.parking_lot.park_car(self.car1)
        self.parking_lot.park_car(self.car2)
        self.parking_lot.remove_car(self.car2)
        self.assertTrue(self.parking_lot.park_car(self.car4))  # Should succeed now
        self.assertTrue(self.parking_lot.park_car(self.car1))

if __name__ == '__main__':
    unittest.main()
