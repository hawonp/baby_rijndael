import numpy as np

from .constants import SBOX_INVERSE, SBOX_LOOKUP, T_INVERSE, T_MATRIX


#######################
# AUXILIARY FUNCTIONS #
#######################
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


def to_binary(hex_string: str) -> str:
    return bin(int(hex_string, 16))[2:].zfill(4)


def to_hex(binary_string: str) -> str:
    # convert binary string to integer, then to hexadecimal
    return hex(int(binary_string, 2))[2:]


def print_matrix(hex_stream: list[str]) -> None:
    print(hex_stream[0], hex_stream[2])
    print(hex_stream[1], hex_stream[3])


########################
# ENCRYPTION FUNCTIONS #
########################
def calc_s(hex_stream: list[str]) -> list[str]:
    return [SBOX_LOOKUP[x] for x in hex_stream]


def calc_sigma_hat(hex_stream: list[str]) -> list[str]:
    return [hex_stream[0], hex_stream[3], hex_stream[2], hex_stream[1]]


def calc_t(hex_stream: list[str]) -> list[str]:
    # convert hex_stream to binary
    binary_stream = [to_binary(x) for x in hex_stream]

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
    result = np.array(T_MATRIX) @ np.array(matrix) % 2

    # reconstruct hex stream from column major order matrix
    output = [
        to_hex(
            str(result[0][0])
            + str(result[1][0])
            + str(result[2][0])
            + str(result[3][0])
        ),
        to_hex(
            str(result[4][0])
            + str(result[5][0])
            + str(result[6][0])
            + str(result[7][0])
        ),
        to_hex(
            str(result[0][1])
            + str(result[1][1])
            + str(result[2][1])
            + str(result[3][1])
        ),
        to_hex(
            str(result[4][1])
            + str(result[5][1])
            + str(result[6][1])
            + str(result[7][1])
        ),
    ]

    return output


def calc_xor(matrix_a: list[str], matrix_b: list[str]) -> list[str]:
    binary_xor_arr = [
        (bin(int(str(a), 16) ^ int(str(b), 16))[2:].zfill(4))
        for a, b in zip(matrix_a, matrix_b)
    ]

    # return as hexadecimal
    return [to_hex(x) for x in binary_xor_arr]


#######################
# DECRYPTION FUNCTIONS #
########################
def calc_inverse_s(hex_stream: list[str]) -> list[str]:
    return [SBOX_INVERSE[x] for x in hex_stream]


def calc_inverse_t(hex_stream: list[str]) -> list[str]:
    # convert hex_stream to binary
    binary_stream = [to_binary(x) for x in hex_stream]

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
    result = np.array(T_INVERSE) @ np.array(matrix) % 2
    # mult_product = matrix_multiplication(T_MATRIX, matrix)
    # result = matrix_modulo_two(mult_product)

    # reconstruct hex stream from column major order matrix
    output = [
        to_hex(
            str(result[0][0])
            + str(result[1][0])
            + str(result[2][0])
            + str(result[3][0])
        ),
        to_hex(
            str(result[4][0])
            + str(result[5][0])
            + str(result[6][0])
            + str(result[7][0])
        ),
        to_hex(
            str(result[0][1])
            + str(result[1][1])
            + str(result[2][1])
            + str(result[3][1])
        ),
        to_hex(
            str(result[4][1])
            + str(result[5][1])
            + str(result[6][1])
            + str(result[7][1])
        ),
    ]

    return output


#######################
# ROUND KEY FUNCTIONS #
#######################
def get_y(i: int):
    return [str(2 ** (i - 1)), str(0)]


def calc_round_key(key: list[str], round: int):
    w0 = [key[0], key[1]]
    w1 = [key[2], key[3]]

    reverse_w1 = [key[3], key[2]]

    s_w1 = calc_s(reverse_w1)

    xor_w0 = calc_xor(w0, s_w1)

    w2 = calc_xor(xor_w0, get_y(round))

    w3 = calc_xor(w1, w2)

    return w2 + w3
