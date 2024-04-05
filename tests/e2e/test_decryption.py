import pytest

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
def test_ecb_decryption(
    baby_rijndael_dataset: BabyRijndael,
    block: str,
    key: str,
    expected: str,
) -> None:
    baby_rijndale = baby_rijndael_dataset
    assert baby_rijndale.decrypt(expected) == block
