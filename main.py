import argparse
from enum import StrEnum

from cipher.block_cipher import BabyRijndael
from cipher.cipher_block_chaining import cbc_decrypt, cbc_encrypt


class EncryptionDirection(StrEnum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


class EncryptionMode(StrEnum):
    ECB = "ecb"
    CBC = "cbc"


def main():
    # get arguments from command line
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a file using the Baby Rijndael Block Cipher."
    )
    parser.add_argument(
        "direction",
        type=str,
        choices=list(EncryptionDirection),
        help="Encrypt or Decrypt the File",
    )
    parser.add_argument(
        "mode",
        type=str,
        choices=list(EncryptionMode),
        help="Use ECB or CBC Mode",
    )
    parser.add_argument(
        "filename",
        type=str,
        help="The filename to encrypt/decrypt",
    )
    parser.add_argument(
        "key",
        type=str,
        help="The key to use",
    )
    parser.add_argument(
        "iv",
        type=str,
        help="The IV to use",
    )
    args = parser.parse_args()

    # print welcome message
    print("Welcome to Baby Rijndael!\n")
    print(
        f"You have chosen to {args.direction} the file '{args.filename}' using '{args.mode}' mode with the key '{args.key}' and the IV '{args.iv}'"  # noqa
    )

    # read in file as binary and then convert to hex
    with open(args.filename, "rb") as f:
        print(f"Reading file '{args.filename}'...")
        data = f.read()
        print(f"Input Data: {data}")

    data = data.hex()
    print(f"Input Data (hex): {data}")

    # encrypt/decrypt
    baby_rijndael = BabyRijndael()
    if args.direction == EncryptionDirection.ENCRYPT:
        print("\nEncrypting...")
        if args.mode == EncryptionMode.ECB:
            result = baby_rijndael.encrypt(data, args.key)
        elif args.mode == EncryptionMode.CBC:
            result = cbc_encrypt(data, args.key, args.iv, baby_rijndael)
    elif args.direction == EncryptionDirection.DECRYPT:
        print("\nDecrypting...")
        if args.mode == EncryptionMode.ECB:
            result = baby_rijndael.decrypt(data, args.key)
        elif args.mode == EncryptionMode.CBC:
            result = cbc_decrypt(data, args.key, args.iv, baby_rijndael)

    print(f"Result: {result}")

    # write result to file as 'filename.out' as binary
    with open(f"{args.filename}.out", "wb") as f:
        # convert result to bytes
        result = bytes.fromhex(result)
        print("Result (bytes):", result)
        f.write(result)

    print("Done!")


if __name__ == "__main__":
    main()
