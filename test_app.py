from app import random_fruit


def test_random_fruit():
    assert "apple" or "orange" or "cherry" in random_fruit()
