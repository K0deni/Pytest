#Hello to my simple pytest project#
#Important note is test file need to start with test, in other way it will be error with found and write the test file
import pytest

#Using 'quiet' report mode 
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

# content of test_class_demo.py
class TestClassDemoInstance:
    def test_one(self):
        assert 0 

    def test_two(self):
        assert 0