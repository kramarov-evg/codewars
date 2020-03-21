import unittest
import directions_reduction as dr


class Tests(unittest.TestCase):

    def test_basic_deletion(self):
        self.assertEqual(dr.dirReduc(["WEST", "EAST", "NORTH"]), ["NORTH"])

    def test_nested_deletion(self):
        self.assertEqual(dr.dirReduc(["SOUTH", "WEST", "EAST", "NORTH", "WEST"]), ["WEST"])

    def test_empty_result(self):
        self.assertEqual(dr.dirReduc(["SOUTH", "NORTH"]), [])

    def test_empty_input(self):
        self.assertEqual(dr.dirReduc([]), [])

    def test_unreduceable(self):
        self.assertEqual(dr.dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
