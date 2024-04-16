import numpy as np

from .constants import SBOX_INVERSE, SBOX_LOOKUP, T_INVERSE, T_MATRIX

__all__ = [
    "print_matrix",
    "is_hexadecimal",
    "xor",
    "sbox",
    "sbox_inverse",
    "sigma_hat",
    "tbox",
    "tbox_inverse",
    "round_key",
    "add_padding",
    "remove_padding",
    "xor_bytes",
]


#######################
# AUXILIARY FUNCTIONS #
#######################
def print_matrix(x: str):
    print(x[0], x[2])
    print(x[1], x[3])


def is_hexadecimal(data: str) -> bool:
    # strip 0x from the beginning of the string
    if data.startswith("0x"):
        data = data[2:]

    # verify that the string is a valid hexadecimal string
    if not all(x in "0123456789abcdef" for x in data):
        return False

    return True


def add_padding(data: bytes):
    # pad with 0xff if there is an odd number of bytes
    if len(data) % 2 != 0:
        data += b"\xff"
    return data


def remove_padding(data: bytes):
    # remove padding if the last byte is 0xff and even number of bytes
    if data[-1] == 0xFF and len(data) % 2 == 0:
        data = data[:-1]
    return data


########################
# ENCRYPTION FUNCTIONS #
########################
def xor(x: str, y: str) -> str:
    result = int(x, 16) ^ int(y, 16)
    return hex(result)[2:].zfill(4)


def xor_bytes(x: bytes, y: bytes) -> bytes:
    result = int.from_bytes(x, "big") ^ int.from_bytes(y, "big")
    return result.to_bytes(len(x), "big")


def sbox(x: str) -> str:
    if "0x" in x:
        x = x[2:]

    return "".join([SBOX_LOOKUP[x] for x in x])


def sbox_inverse(x: str) -> str:
    if "0x" in x:
        x = x[2:]
    return "".join([SBOX_INVERSE[x] for x in x])


def sigma_hat(x: str) -> str:
    x = x.zfill(4)
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    return a + d + c + b


def _t_aux(block: str, t_matrix: list[list[int]]) -> str:
    # strip 0x from the beginning of the string
    if "0x" in block:
        block = block[2:]

    # convert to matrix form
    # convert to binary
    binary_stream = [bin(int(x, 16))[2:].zfill(4) for x in block]

    # create a 8x2 matrix storing the binary values in column major order
    matrix = [[0 for _ in range(2)] for _ in range(8)]

    matrix[0][0] = int(binary_stream[0][0])
    matrix[1][0] = int(binary_stream[0][1])
    matrix[2][0] = int(binary_stream[0][2])
    matrix[3][0] = int(binary_stream[0][3])
    matrix[4][0] = int(binary_stream[1][0])
    matrix[5][0] = int(binary_stream[1][1])
    matrix[6][0] = int(binary_stream[1][2])
    matrix[7][0] = int(binary_stream[1][3])
    matrix[0][1] = int(binary_stream[2][0])
    matrix[1][1] = int(binary_stream[2][1])
    matrix[2][1] = int(binary_stream[2][2])
    matrix[3][1] = int(binary_stream[2][3])
    matrix[4][1] = int(binary_stream[3][0])
    matrix[5][1] = int(binary_stream[3][1])
    matrix[6][1] = int(binary_stream[3][2])
    matrix[7][1] = int(binary_stream[3][3])

    # multiply matrix by T_MATRIX
    result = np.array(t_matrix) @ np.array(matrix) % 2

    # reconstruct hex stream from column major order matrix
    a = str(result[0][0]) + str(result[1][0]) + str(result[2][0]) + str(result[3][0])
    b = str(result[4][0]) + str(result[5][0]) + str(result[6][0]) + str(result[7][0])
    c = str(result[0][1]) + str(result[1][1]) + str(result[2][1]) + str(result[3][1])
    d = str(result[4][1]) + str(result[5][1]) + str(result[6][1]) + str(result[7][1])

    return hex(int(a + b + c + d, 2))[2:].zfill(4)


def tbox(x: str) -> str:
    return _t_aux(x, T_MATRIX)


def tbox_inverse(x: str) -> str:
    return _t_aux(x, T_INVERSE)


#######################
# ROUND KEY FUNCTIONS #
#######################
def _get_y(i: int):
    return str(2 ** (i - 1)) + str(0)


def round_key(key: str, round: int):
    w0 = key[0] + key[1]
    w1 = key[2] + key[3]
    reverse_w1 = w1[1] + w1[0]
    s_w1 = sbox(reverse_w1)
    xor_w0 = xor(w0, s_w1)[2:]
    w2 = xor(xor_w0, _get_y(round))[2:]
    w3 = xor(w1, w2)[2:]
    return (w2 + w3).zfill(4)
