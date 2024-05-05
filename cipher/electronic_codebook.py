from .block_cipher import BlockCipher


def ecb_encrypt(
    plaintext: str,
    key: str,
    block_cipher: BlockCipher,
) -> str:
    # remove 0x prefix if present
    if plaintext.startswith("0x"):
        plaintext = plaintext[2:]
    if key.startswith("0x"):
        key = key[2:]

    # split plaintext into 16bit blocks
    blocks = [plaintext[i : i + 4] for i in range(0, len(plaintext), 4)]  # noqa

    # if the last block is not 16 bits, pad it with 0xff
    if len(blocks[-1]) < 4:
        blocks[-1] = blocks[-1].ljust(4, "f")

    # encrypt each block
    output = ""
    for block in blocks:
        result = block_cipher.encrypt(block, key)
        output += result

    return output


def ecb_decrypt(
    ciphertext: str,
    key: str,
    block_cipher: BlockCipher,
) -> str:
    # remove 0x prefix if present
    if ciphertext.startswith("0x"):
        ciphertext = ciphertext[2:]
    if key.startswith("0x"):
        key = key[2:]

    # split ciphertext into 16bit blocks
    blocks = [ciphertext[i : i + 4] for i in range(0, len(ciphertext), 4)]  # noqa

    # decrypt each block
    output = ""
    for block in blocks:
        result = block_cipher.decrypt(block, key)
        output += result

    # if last block contains ff, remove the last 2 characters
    if output.endswith("ff"):
        output = output[:-2]

    return output
