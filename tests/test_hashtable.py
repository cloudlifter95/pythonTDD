# import sys
# sys.path.append('/../')
from pythonTDD.sources.hashtable import HashTable

def test_should_always_pass():
    assert 2+2 == 4, "test_should_always_pass did not pass"

# def test_should_always_fail():
#     assert 2+2 == 22, "test_should_always_fail did fail"


def test_create_hashtable():
    assert HashTable() is not None