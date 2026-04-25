import pytest

from normalize import normalize


@pytest.mark.parametrize("raw, expected", [
    ("فواحد الدوار", "في واحد الدوار"),
    ("فالتراب", "في التراب"),
    ("فهاد الدوار", "في هاد الدوار"),
    ("فجناب الواد", "في جناب الواد"),
    ("فبلاصتو", "في بلاصتو"),
    ("فكل قنت", "في كل قنت"),
    ("فين كيمشي", "فين كيمشي"),  # feen (where) must not be expanded
])
def test_normalize(raw: str, expected: str) -> None:
    assert normalize(raw) == expected
