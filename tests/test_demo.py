import unittest
from src.demo_dagger_python import demo

class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEqual(demo.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
