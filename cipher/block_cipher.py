from abc import ABC

from .utils import round_key, sbox, sbox_inverse, sigma_hat, tbox, tbox_inverse, xor

__all__ = ["BlockCipher", "BabyRijndael"]


class BlockCipher(ABC):
    def encrypt(
        self,
        plaintext: str,
        key: str,
    ):
        raise NotImplementedError

    def decrypt(
        self,
        ciphertext: str,
        key: str,
    ):
        raise NotImplementedError


class BabyRijndael(BlockCipher):

    def encrypt(
        self,
        plaintext: str,
        key: str,
    ):

        if "0x" in plaintext:
            plaintext = plaintext[2:]
        if "0x" in key:
            key = key[2:]

        # calculate round keys
        key_zero = key
        key_one = round_key(key_zero, 1)
        key_two = round_key(key_one, 2)
        key_three = round_key(key_two, 3)
        key_four = round_key(key_three, 4)

        # round zero
        round_zero = xor(plaintext, key_zero)

        # round one
        round_one = sbox(round_zero)
        round_one = sigma_hat(round_one)
        round_one = tbox(round_one)
        round_one = xor(round_one, key_one)

        # round two
        round_two = sbox(round_one)
        round_two = sigma_hat(round_two)
        round_two = tbox(round_two)
        round_two = xor(round_two, key_two)

        # round three
        round_three = sbox(round_two)
        round_three = sigma_hat(round_three)
        round_three = tbox(round_three)
        round_three = xor(round_three, key_three)

        # round four
        round_four = sbox(round_three)
        round_four = sigma_hat(round_four)
        round_four = xor(round_four, key_four)

        return round_four

    def decrypt(
        self,
        ciphertext: str,
        key: str,
    ):
        if "0x" in ciphertext:
            ciphertext = ciphertext[2:]
        if "0x" in key:
            key = key[2:]

        # calculate round keys
        key_zero = key
        key_one = round_key(key_zero, 1)
        key_two = round_key(key_one, 2)
        key_three = round_key(key_two, 3)
        key_four = round_key(key_three, 4)

        # round four
        round_four = xor(ciphertext, key_four)
        round_four = sigma_hat(round_four)
        round_four = sbox_inverse(round_four)

        # round three
        round_three = xor(round_four, key_three)
        round_three = tbox_inverse(round_three)
        round_three = sigma_hat(round_three)
        round_three = sbox_inverse(round_three)

        # round two
        round_two = xor(round_three, key_two)
        round_two = tbox_inverse(round_two)
        round_two = sigma_hat(round_two)
        round_two = sbox_inverse(round_two)

        # round one
        round_one = xor(round_two, key_one)
        round_one = tbox_inverse(round_one)
        round_one = sigma_hat(round_one)
        round_one = sbox_inverse(round_one)

        # round zero
        round_zero = xor(round_one, key_zero)

        return round_zero
