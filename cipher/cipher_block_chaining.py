from .block_cipher import BlockCipher
from .utils import xor

__all__ = ["cbc_encrypt", "cbc_decrypt"]


def cbc_encrypt(
    plaintext: str,
    key: str,
    initialisation_vector: str,
    block_cipher: BlockCipher,
) -> str:
    # remove 0x prefix if present
    if plaintext.startswith("0x"):
        plaintext = plaintext[2:]
    if key.startswith("0x"):
        key = key[2:]
    if initialisation_vector.startswith("0x"):
        initialisation_vector = initialisation_vector[2:]

    # split plaintext into 16bit blocks
    blocks = [plaintext[i : i + 4] for i in range(0, len(plaintext), 4)]  # noqa

    # set result to iv (for first block)
    result = initialisation_vector

    # encrypt each block
    output = ""
    for i in range(len(blocks)):
        # xor plaintext block with result
        xor_result = xor(blocks[i], result)

        # encrypt block
        result = block_cipher.encrypt(xor_result, key)

        # append result to output
        output += result

    return output


def cbc_decrypt(
    ciphertext: str,
    key: str,
    initialisation_vector: str,
    block_cipher: BlockCipher,
) -> str:
    # remove 0x prefix if present
    if ciphertext.startswith("0x"):
        ciphertext = ciphertext[2:]
    if key.startswith("0x"):
        key = key[2:]
    if initialisation_vector.startswith("0x"):
        initialisation_vector = initialisation_vector[2:]

    # split ciphertext into 16bit blocks
    blocks = [ciphertext[i : i + 4] for i in range(0, len(ciphertext), 4)]  # noqa

    # set result to initialisation_vector (for first block)
    result = initialisation_vector

    # decrypt each block
    output = ""
    for i in range(len(blocks)):
        # decrypt block
        decrypted = block_cipher.decrypt(blocks[i], key)

        # xor decrypted block with result
        xor_result = xor(decrypted, result)

        # append result to output
        output += xor_result

        # set result to current block
        result = blocks[i]

    return output
