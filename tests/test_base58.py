import base58
import unittest

class Base58Tests(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(base58.b58encode("Hello World!"), b'2NEpo7TZRRrLZSi2U')

    def test_encode_int(self):
        self.assertEqual(base58.b58encode_int(10), b'B')
