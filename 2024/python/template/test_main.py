import unittest
import main

class TestMain(unittest.TestCase):
    def test_load_data(self):
        self.assertEqual(main.load_data(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
