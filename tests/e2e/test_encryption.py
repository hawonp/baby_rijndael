import pytest

from cipher.block_cipher import BabyRijndael
from cipher.cipher_block_chaining import cbc_encrypt


@pytest.mark.parametrize(
    "plaintext, key, initialisation_vector, expected",
    [
        ("0x3516bd2b", "0x1111", "0x0000", "e6d25de9"),
        ("0x85ca0e6fe5ce620e134d", "0xd884", "0x5407", "b8d7ad81ad5653fac5cb"),
        # ("0x85ca0e6fe5ce620e134d", "0xb95f", "0x9a26", "49250478e624a83cccaf"),
    ],
)
def test_cbc_encrypt(
    block_cipher_dataset: BabyRijndael,
    plaintext: str,
    key: str,
    initialisation_vector: str,
    expected: str,
) -> None:
    block_cipher = block_cipher_dataset

    assert (
        cbc_encrypt(
            plaintext=plaintext,
            key=key,
            initialisation_vector=initialisation_vector,
            block_cipher=block_cipher,
        )
        == expected
    )


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
def test_block_cipher_encryption(
    block_cipher_dataset: BabyRijndael,
    block: str,
    key: str,
    expected: str,
) -> None:
    block_cipher = block_cipher_dataset
    assert block_cipher.encrypt(block, key) == expected
