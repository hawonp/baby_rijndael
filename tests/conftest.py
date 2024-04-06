import pytest

from cipher.block_cipher import BabyRijndael

__all__ = [
    "block_cipher_dataset",
]


@pytest.fixture
def block_cipher_dataset():
    return BabyRijndael()
