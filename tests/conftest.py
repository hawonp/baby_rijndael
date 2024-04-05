import pytest

from baby_rijndael.rijndael import BabyRijndael

__all__ = [
    "key",
    "iv",
    "baby_rijndael_dataset",
]


@pytest.fixture
def key() -> str:
    return "6b5d"


@pytest.fixture
def iv() -> str | None:
    return None


@pytest.fixture
def baby_rijndael_dataset(
    key: str,
    iv: str | None,
):
    return BabyRijndael(
        key=key,
        iv=iv,
    )
