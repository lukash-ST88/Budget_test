from django.test import TestCase
import pytest


class TestClass(TestCase):
    def test_hello_world(self):
        self.assertEqual("hello", "hello")


@pytest.mark.slow
def test_hello_world():
    print('something')
    assert "hello" == "hello"


@pytest.mark.skip
def test_vowels():
    result = set('aeiou')
    expected = set('aeiou')
    print("this test has run")
    assert result == expected




