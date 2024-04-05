import pytest

from baby_rijndael.rijndael import BabyRijndael

__all__ = [
    "key",
    "baby_rijndael_dataset",
]


@pytest.fixture
def key() -> str:
    return "6b5d"


@pytest.fixture
def baby_rijndael_dataset(
    key: str,
):
    return BabyRijndael(
        key=key,
    )
