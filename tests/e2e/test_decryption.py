import pytest

from cipher.block_cipher import BlockCipher


@pytest.mark.parametrize(
    "block, key, expected",
    [
        ("2ca5", "6b5d", "6855"),
        ("0123", "cdef", "2389"),
        ("cdef", "0123", "dba3"),
        ("5555", "a8b4", "125e"),
        ("372e", "0000", "7256"),
        ("ffff", "ffff", "c75b"),
    ],
)
def test_block_cipher_decryption(
    block_cipher_dataset: BlockCipher,
    block: str,
    key: str,
    expected: str,
) -> None:
    block_cipher = block_cipher_dataset
    assert block_cipher.decrypt(expected) == block
