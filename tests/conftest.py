"""
    conftest.py
        Fixture are defined here
"""
import pytest
from pythonTDD.sources.hashtable import HashTable, BLANK

@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    sample_data["key1"] = None
    return sample_data