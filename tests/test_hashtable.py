# import sys
# sys.path.append('/../')
import pytest
from pythonTDD.sources.hashtable import HashTable, BLANK

def test_should_always_pass():
    assert 2+2 == 4, "test_should_always_pass did not pass"

# def test_should_always_fail():
#     assert 2+2 == 22, "test_should_always_fail did fail"


def test_create_hashtable_without_capacity_fails():
    with pytest.raises(TypeError) as excinfo:  
        HashTable() 
    assert "HashTable.__init__() missing" in str(excinfo.value)

def test_hashtable_has_capacity_property():
    assert HashTable(capacity=100) is not None

def test_hashtable_creates_hashtable():
    assert type(HashTable(capacity=100)) is HashTable

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 100

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values

def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key1"] = None
    assert None in hash_table.values

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"