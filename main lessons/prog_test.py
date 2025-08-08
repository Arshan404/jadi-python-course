import unittest

from prog import countc

class TestCountc(unittest.TestCase):
    def test_simple(self):
        s = "jadi"
        c = "a"
        self.assertEqual(countc(s,c) , 1)

    def test_nothing(self):
        s = ""
        c = "a"
        self.assertEqual(countc(s,c) , 0)

    def test_longer(self):
        s = "jadi jadi jadi jadi jadi"
        c = "a"
        self.assertEqual(countc(s,c) , 5)

    def test_non_existence(self):
        s = "jadi"
        c = "x"
        self.assertEqual(countc(s,c) , 0)

    def test_all(self):
        s = "xxxxxxx"
        c = "x"
        self.assertEqual(countc(s,c) , 7)

if __name__ =='__main__':
    unittest.main()
