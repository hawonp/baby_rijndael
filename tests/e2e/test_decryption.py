import pytest

from cipher.block_cipher import BabyRijndael
from cipher.cipher_block_chaining import cbc_decrypt


@pytest.mark.parametrize(
    "ciphertext, key, initialisation_vector, expected",
    [
        ("0xe6d25de9", "0x1111", "0x0000", "3516bd2b"),
        ("0xb8d7ad81ad5653fac5cb", "0xd884", "0x5407", "85ca0e6fe5ce620e134d"),
        ("0x49250478e624a83cccaf", "0xb95f", "0x9a26", "5d67df0102130b5b9f45"),
    ],
)
def test_cbc_decrypt(
    block_cipher_dataset: BabyRijndael,
    ciphertext: str,
    key: str,
    initialisation_vector: str,
    expected: str,
) -> None:
    block_cipher = block_cipher_dataset

    assert (
        cbc_decrypt(
            ciphertext=ciphertext,
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
def test_block_cipher_decryption(
    block_cipher_dataset: BabyRijndael,
    block: str,
    key: str,
    expected: str,
) -> None:
    block_cipher = block_cipher_dataset
    assert block_cipher.decrypt(expected, key) == block


def test_invalid_block_cipher_decryption(
    block_cipher_dataset: BabyRijndael,
) -> None:
    block_cipher = block_cipher_dataset

    # invalid block, valid key

    with pytest.raises(ValueError):
        block_cipher.decrypt("000", "0000")

    # valid block, invalid key
    with pytest.raises(ValueError):
        block_cipher.decrypt("0000", "000")
