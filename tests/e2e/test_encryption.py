import pytest

from baby_rijndael.cipher_block_chaining import cbc_encrypt
from baby_rijndael.rijndael import BabyRijndael


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
def test_ecb_encryption(
    baby_rijndael_dataset: BabyRijndael,
    block: str,
    key: str,
    expected: str,
) -> None:
    baby_rijndale = baby_rijndael_dataset
    assert baby_rijndale.encrypt(block) == expected


def test_cbc_encryption() -> None:
    assert cbc_encrypt("0x3516bd2b", "0x1111", "0x0000") == "e6d25de9"
    assert (
        cbc_encrypt("0x85ca0e6fe5ce620e134d", "0xd884", "0x5407")
        == "b8d7ad81ad5653fac5cb"
    )
    assert (
        cbc_encrypt("0x85ca0e6fe5ce620e134d", "0xb95f", "0x9a26")
        == "49250478e624a83cccaf"
    )
