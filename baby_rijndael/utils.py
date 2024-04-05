from .constants import SBOX_INVERSE, SBOX_LOOKUP, T_MATRIX


def s_operation(hex_stream: list[str]) -> list[str]:
    return [SBOX_LOOKUP[x] for x in hex_stream]


def sigma_operation(hex_stream: list[str]) -> list[str]:
    return [hex_stream[0], hex_stream[3], hex_stream[2], hex_stream[1]]


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
    mult_product = matrix_multiplication(T_MATRIX, matrix)
    result = matrix_modulo_two(mult_product)

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


def matrix_multiplication(
    matrix_a: list[list[int]], matrix_b: list[list[int]]
) -> list[list[int]]:
    # get the number of rows and columns in matrix_a
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    # get the number of rows and columns in matrix_b
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    # verify that the number of columns in matrix_a is equal to the number of rows in matrix_b
    assert (
        cols_a == rows_b
    ), "Number of columns in matrix_a must be equal to the number of rows in matrix_b"

    # initialize the resulting matrix
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # iterate through the rows of matrix_a
    for i in range(rows_a):
        # iterate through the columns of matrix_b
        for j in range(cols_b):
            # iterate through the columns of matrix_a
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def matrix_modulo_two(matrix_a: list[list[int]]) -> list[list[int]]:
    # get the number of rows and columns in matrix_a
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    # iterate through the rows of matrix_a
    for i in range(rows_a):
        # iterate through the columns of matrix_a
        for j in range(cols_a):
            matrix_a[i][j] = matrix_a[i][j] % 2

    return matrix_a
