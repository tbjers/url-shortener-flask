import base58

def test_encode():
    assert base58.b58encode("Hello World!") == b'2NEpo7TZRRrLZSi2U'

def test_encode_int():
    assert base58.b58encode_int(10) == b'B'
