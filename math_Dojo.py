import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for num in nums:
            self.result += num
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for num in nums:
            self.result -= num
        return self

class tests(unittest.TestCase):
    def test_add_one(self):
        md = MathDojo()
        md.add(1)
        self.assertEqual(md.result, 1)
    def test_add_multiple(self):
        md = MathDojo()
        md.add(1, 4)
        self.assertEqual(md.result, 5)
    def test_subtract_one(self):
        md = MathDojo()
        md.subtract(1)
        self.assertEqual(md.result, -1)
    def test_subtract_multiple(self):
        md = MathDojo()
        md.subtract(1, 5)
        self.assertEqual(md.result, -6)
    def test_chaining(self):
        md = MathDojo()
        md.add(10).subtract(5)
        self.assertEqual(md.result, 5)

    def setUp(self):
        print("running setup")
    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()

