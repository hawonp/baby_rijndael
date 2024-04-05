from .enums import EncryptionDirection, EncryptionMode
from .utils import (
    get_hex_stream,
    print_matrix,
    s_operation,
    sigma_operation,
    t_multiplication,
    xor,
)


class BabyRijndael:

    def __init__(
        self,
        mode: EncryptionMode,
        direction: EncryptionDirection,
        filename: str,
        key: str,
        iv: str | None,
    ) -> None:
        self.mode = mode
        self.direction = direction
        self.filename = filename
        self.key = get_hex_stream(key)
        self.iv = get_hex_stream(iv) if iv else None

    def run(self, block: str) -> str:
        if self.direction == EncryptionDirection.ENCRYPT:
            output = self._encrypt(block)
        else:
            output = self._decrypt(block)

        return output

    def one_round(
        self,
        input: str,
        apply_s: bool,
        apply_sigma: bool,
        apply_t: bool,
        key: list[str],
    ) -> list[str]:
        hex_stream: list[str] = get_hex_stream(input)

        if apply_s:
            hex_stream = s_operation(hex_stream)
        if apply_sigma:
            hex_stream = sigma_operation(hex_stream)
        if apply_t:
            hex_stream = t_multiplication(hex_stream)

        return xor(hex_stream, key)

    def _encrypt(self, input: str) -> str:
        # preliminary
        round_zero = self.one_round(input, False, False, False, self.key)
        print_matrix(round_zero)

        # round 1
        # key_one = self.

        # round 2

        # round 3

        # round 4

        # xor_key = xor(hex_stream, self.key)
        # print("After Key XOR:")
        # print_matrix(xor_key)

        # # round 2
        # print("\nRound 2:")
        # s_op = s_operation(xor_key)
        # print("After S-Box Operation:")
        # print_matrix(s_op)

        # sigma_op = sigma_operation(s_op)
        # print("After Sigma Operation:")
        # print_matrix(sigma_op)

        # t_mult = t_multiplication(sigma_op)
        # print("After T-Multiplication:")
        # print_matrix(t_mult)

        # round_key1 = round_key(self.key, 1)
        # print("Round Key 1:")
        # print_matrix(round_key1)

        # # round 3
        # print("\nRound 3:")

        # print("round key 2")
        # round_key2 = round_key(round_key1, 2)
        # print_matrix(round_key2)

        return input

    def _decrypt(self, input: str) -> str:
        return input
