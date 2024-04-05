# from .block import Block
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

    def _encrypt(self, input: str) -> str:
        print("Initial Key:")
        print_matrix(self.key)

        # convert input to hex stream
        hex_stream: list[str] = get_hex_stream(input)

        print("Initial Block:")
        print_matrix(hex_stream)

        # round 1
        print("\nRound 1:")
        xor_key = xor(hex_stream, self.key)
        print("After Key XOR:")
        print_matrix(xor_key)

        # round 2
        print("\nRound 2:")
        s_op = s_operation(xor_key)
        print("After S-Box Operation:")
        print_matrix(s_op)

        sigma_op = sigma_operation(s_op)
        print("After Sigma Operation:")
        print_matrix(sigma_op)

        t_mult = t_multiplication(sigma_op)
        print("After T-Multiplication:")
        print_matrix(t_mult)

        return input

    def _decrypt(self, input: str) -> str:
        return input
