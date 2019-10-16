import unittest


class ExampleTest(unittest.TestCase):

    def test_start_here(self):
        self.assertEqual( 1, 1)

if __name__ == '__main__':
    unittest.main()