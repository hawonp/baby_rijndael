import pytest

from cipher.block_cipher import BlockCipher

__all__ = [
    "key",
    "block_cipher_dataset",
]


@pytest.fixture
def key() -> str:
    return "6b5d"


@pytest.fixture
def block_cipher_dataset(key: str):
    return BlockCipher(key)
