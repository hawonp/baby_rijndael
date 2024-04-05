from .utils import (
    calc_inverse_s,
    calc_inverse_t,
    calc_round_key,
    calc_s,
    calc_sigma_hat,
    calc_t,
    calc_xor,
    get_hex_stream,
)

__all__ = ["BabyRijndael"]


class BabyRijndael:
    def __init__(
        self,
        key: str,
    ) -> None:
        self.key = get_hex_stream(key)

    def encrypt(self, input: str) -> str:
        # calculate round keys
        key_zero = self.key
        key_one = calc_round_key(key_zero, 1)
        key_two = calc_round_key(key_one, 2)
        key_three = calc_round_key(key_two, 3)
        key_four = calc_round_key(key_three, 4)

        # preliminary
        hex_stream: list[str] = get_hex_stream(input)
        round_zero = calc_xor(hex_stream, key_zero)

        # round 1
        round_one = calc_s(round_zero)
        round_one = calc_sigma_hat(round_one)
        round_one = calc_t(round_one)
        round_one = calc_xor(round_one, key_one)

        # round 2
        round_two = calc_s(round_one)
        round_two = calc_sigma_hat(round_two)
        round_two = calc_t(round_two)
        round_two = calc_xor(round_two, key_two)

        # round 3
        round_three = calc_s(round_two)
        round_three = calc_sigma_hat(round_three)
        round_three = calc_t(round_three)
        round_three = calc_xor(round_three, key_three)

        # round 4
        round_four = calc_s(round_three)
        round_four = calc_sigma_hat(round_four)
        round_four = calc_xor(round_four, key_four)

        # apply string concatenation
        output = "".join(round_four)
        return output

    def decrypt(self, input: str) -> str:
        # calculate round keys
        key_zero = self.key
        key_one = calc_round_key(key_zero, 1)
        key_two = calc_round_key(key_one, 2)
        key_three = calc_round_key(key_two, 3)
        key_four = calc_round_key(key_three, 4)

        # round zero
        hex_stream: list[str] = get_hex_stream(input)

        round_zero = calc_xor(hex_stream, key_four)
        round_zero = calc_sigma_hat(round_zero)
        round_zero = calc_inverse_s(round_zero)

        # round one
        round_one = calc_xor(round_zero, key_three)
        round_one = calc_inverse_t(round_one)
        round_one = calc_sigma_hat(round_one)
        round_one = calc_inverse_s(round_one)

        # round two
        round_two = calc_xor(round_one, key_two)
        round_two = calc_inverse_t(round_two)
        round_two = calc_sigma_hat(round_two)
        round_two = calc_inverse_s(round_two)

        # round three
        round_three = calc_xor(round_two, key_one)
        round_three = calc_inverse_t(round_three)
        round_three = calc_sigma_hat(round_three)
        round_three = calc_inverse_s(round_three)

        # round four
        round_four = calc_xor(round_three, key_zero)

        # apply string concatenation
        output = "".join(round_four)
        return output
