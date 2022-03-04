#Hello to my simple pytest project#
#Important note is test file need to start with test, in other way it will be error with found and write the test file
import pytest
import requests

def test_func_fast():
    pass


@pytest.mark.slow
def test_func_slow():
    pass

def test_request():
    req1 = 201
    assert req1 == 201