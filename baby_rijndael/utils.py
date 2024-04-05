from .constants import SBOX_INVERSE, SBOX_LOOKUP


def s_operation(hex_stream: list[str]) -> list[str]:
    return [SBOX_LOOKUP[x] for x in hex_stream]


def sigma_operation(hex_stream: list[str]) -> list[str]:
    return [hex_stream[0], hex_stream[2], hex_stream[3], hex_stream[1]]


def inverse_s_operation(hex_stream: list[str]) -> list[str]:
    return [SBOX_INVERSE[x] for x in hex_stream]


def get_hex_stream(data: str) -> list[str]:
    # strip 0x from the beginning of the string
    if data.startswith("0x"):
        data = data[2:]

    # verify that the string is a valid hexadecimal string
    assert all(
        x in "0123456789abcdef" for x in data
    ), "Value must be a valid hexadecimal string"

    # convert to list of strings
    str_list = [str(x) for x in data]

    # convert str list to to_binary
    binary_list = [to_binary(x) for x in str_list]

    # convert binary list to hex list
    return [to_hex(x) for x in binary_list]


def print_matrix(hex_stream: list[str]) -> None:
    print(hex_stream[0], hex_stream[2])
    print(hex_stream[1], hex_stream[3])


def to_binary(hex_string: str) -> str:
    return bin(int(hex_string, 16))[2:].zfill(4)


def to_hex(binary_string: str) -> str:
    # convert binary string to integer, then to hexadecimal
    return hex(int(binary_string, 2))[2:]


def xor(matrix_a: list[str], matrix_b: list[str]) -> list[str]:
    binary_xor_arr = [
        (bin(int(a, 16) ^ int(b, 16))[2:].zfill(4)) for a, b in zip(matrix_a, matrix_b)
    ]

    # return as hexadecimal
    return [to_hex(x) for x in binary_xor_arr]


def t_multiplication(hex_stream: list[str]):
    # convert hex_stream to binary
    binary_stream = [to_binary(x) for x in hex_stream]

    # convert binary stream into a 8x2 bit matrix of 0s and 1s
    matrix = [[int(x) for x in binary] for binary in binary_stream]

    print(matrix)

    return hex_stream
