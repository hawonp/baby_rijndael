from cipher.utils import (
    is_hexadecimal,
    is_sixteen_bit_hex,
    round_key,
    sbox,
    sbox_inverse,
    sigma_hat,
    tbox,
    xor,
)


def test_is_sixteen_bit_hex():
    # extract all possible 16-bit hex strings
    sixteen_bit_hex_strings = [hex(i)[2:].zfill(4) for i in range(2**16)]
    print(len(sixteen_bit_hex_strings))
    # test all possible 16-bit hex strings
    for hex_string in sixteen_bit_hex_strings:
        assert is_sixteen_bit_hex(hex_string) is True

    # test some invalid 16-bit hex strings
    assert is_sixteen_bit_hex("0") is False
    assert is_sixteen_bit_hex("00") is False
    assert is_sixteen_bit_hex("000") is False


def test_is_hexadecimal():
    assert is_hexadecimal("0") is True
    assert is_hexadecimal("1") is True
    assert is_hexadecimal("2") is True
    assert is_hexadecimal("3") is True
    assert is_hexadecimal("4") is True
    assert is_hexadecimal("5") is True
    assert is_hexadecimal("8") is True
    assert is_hexadecimal("9") is True
    assert is_hexadecimal("a") is True
    assert is_hexadecimal("b") is True
    assert is_hexadecimal("c") is True
    assert is_hexadecimal("d") is True
    assert is_hexadecimal("e") is True
    assert is_hexadecimal("f") is True
    assert is_hexadecimal("g") is False


def test_xor():
    assert xor("0", "1") == "0001"
    assert xor("1", "2") == "0003"
    assert xor("2", "3") == "0001"
    assert xor("3", "4") == "0007"
    assert xor("4", "5") == "0001"
    assert xor("5", "6") == "0003"
    assert xor("6", "7") == "0001"
    assert xor("7", "8") == "000f"
    assert xor("8", "9") == "0001"
    assert xor("9", "a") == "0003"
    assert xor("a", "b") == "0001"
    assert xor("b", "c") == "0007"
    assert xor("c", "d") == "0001"
    assert xor("d", "e") == "0003"
    assert xor("e", "f") == "0001"
    assert xor("f", "0") == "000f"
    assert xor("0000", "0000") == "0000"
    assert xor("0000", "ffff") == "ffff"
    assert xor("ffff", "ffff") == "0000"
    assert xor("ffff", "0000") == "ffff"


def test_sbox():
    assert sbox("0") == "a"
    assert sbox("1") == "4"
    assert sbox("2") == "3"
    assert sbox("3") == "b"
    assert sbox("4") == "8"
    assert sbox("5") == "e"
    assert sbox("6") == "2"
    assert sbox("7") == "c"
    assert sbox("8") == "5"
    assert sbox("9") == "7"
    assert sbox("a") == "6"
    assert sbox("b") == "f"
    assert sbox("c") == "0"
    assert sbox("d") == "1"
    assert sbox("e") == "9"
    assert sbox("f") == "d"


def test_sbox_inverse():
    assert sbox_inverse("0") == "c"
    assert sbox_inverse("1") == "d"
    assert sbox_inverse("2") == "6"
    assert sbox_inverse("3") == "2"
    assert sbox_inverse("4") == "1"
    assert sbox_inverse("5") == "8"
    assert sbox_inverse("6") == "a"
    assert sbox_inverse("7") == "9"
    assert sbox_inverse("8") == "4"
    assert sbox_inverse("9") == "e"
    assert sbox_inverse("a") == "0"
    assert sbox_inverse("b") == "3"
    assert sbox_inverse("c") == "7"
    assert sbox_inverse("d") == "f"
    assert sbox_inverse("e") == "5"
    assert sbox_inverse("f") == "b"


def test_sigma_hat():
    assert sigma_hat("abcd") == "adcb"
    assert sigma_hat("8cd5") == "85dc"


def test_round_key():
    assert round_key("6b5d", 1) == "6538"
    assert round_key("6538", 2) == "1e26"
    assert round_key("1e26", 3) == "7d5b"
    assert round_key("7d5b", 4) == "0358"


def test_tbox():
    assert tbox("85dc") == "20f7"
    assert tbox("8d0e") == "0ea3"
    assert tbox("4e5a") == "d298"
