import pytest

from app.app.utils import font_size


font_test_data = [
    ("Leia", 32),
    ("Han", 32),
    ("Obi-Wan", 24),
    ("The Mandalorian", 18),
]


@pytest.mark.parametrize("chars, size", font_test_data)
def test_font_size(chars, size):
    resulting_size = font_size(chars)
    assert resulting_size == size
