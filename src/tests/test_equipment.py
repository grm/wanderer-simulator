import unittest
from equipment import WandererRotatorLite

class TestWandererRotatorLite(unittest.TestCase):
    def setUp(self):
        self.rotator = WandererRotatorLite(port='/dev/ttyUSB0', baudrate=19200)

    def tearDown(self):
        self.rotator.close()

    def test_handshake(self):
        self.rotator.handshake()
        self.assertTrue(True)  # If no exception, test passes

    def test_set_home_position(self):
        self.rotator.set_home_position()
        self.assertEqual(self.rotator.position, 0)

    def test_move_rotator(self):
        self.rotator.move_rotator(45)
        self.assertEqual(self.rotator.position, 45)

    def test_set_rotator_backlash(self):
        self.rotator.set_rotator_backlash(1155)
        self.assertEqual(self.rotator.backlash, 1)

    def test_set_rotator_backlash_enabled(self):
        self.rotator.set_rotator_backlash_enabled(True)
        self.assertEqual(self.rotator.backlash, 1)

    def test_reverse_rotator(self):
        self.rotator.reverse_rotator(True)
        self.assertEqual(self.rotator.reverse_coefficient, -1)

    def test_abort_rotator(self):
        self.rotator.abort_rotator()
        self.assertTrue(self.rotator.halt_command)

    def test_timer_hit(self):
        self.rotator.timer_hit()
        self.assertTrue(True)  # If no exception, test passes

if __name__ == '__main__':
    unittest.main()