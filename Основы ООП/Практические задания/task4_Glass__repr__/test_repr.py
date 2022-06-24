import unittest

from main import Glass


class TestRepr(unittest.TestCase):
    def test_repr(self):
        cap_vol = 700
        oc_vol = 300
        glass = Glass(cap_vol, oc_vol)
        expected_value = "Glass(700, 300)"
        actual_value = repr(glass)
        self.assertEqual(expected_value, actual_value)
