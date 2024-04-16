# from cipher.block_cipher import BabyRijndael
# from cipher.cipher_block_chaining import cbc_decrypt, cbc_encrypt
# from cipher.utils import is_hexadecimal
import argparse
from enum import StrEnum


class EncryptionDirection(StrEnum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"


class EncryptionMode(StrEnum):
    ECB = "ecb"
    CBC = "cbc"


def main():
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

    print("Welcome to Baby Rijndael!\n")
    print(
        f"You have chosen to {args.direction} the file '{args.filename}' using '{args.mode}' mode with the key '{args.key}' and the IV '{args.iv}'"  # noqa
    )

    # baby_rijndael = BabyRijndael()
    with open(args.filename, "rb") as f:
        data = f.read()
        print(data)
    # if args.direction == EncryptionDirection.ENCRYPT:
    #     if args.mode == EncryptionMode.ECB:
    #         result = baby_rijndael.encrypt(data, args.key)
    #     elif args.mode == EncryptionMode.CBC:
    #         result = cbc_encrypt(data, args.key, args.iv, baby_rijndael)
    # elif args.direction == EncryptionDirection.DECRYPT:

    # # initial welcome
    # print("Welcome to Baby Rijndael!")

    # # choose direction
    # print("\nWill you encrypt or decrypt?")
    # print("1. Encrypt")
    # print("2. Decrypt")

    # direction = input("Enter the number of the action you would like to perform: ")
    # if direction == "1":
    #     direction = EncryptionDirection.ENCRYPT
    # elif direction == "2":
    #     direction = EncryptionDirection.DECRYPT
    # else:
    #     print("Invalid action. Exiting...")
    #     return

    # # choose encryption mode
    # print("\nWhat encryption mode would you like to use?")
    # print("1. ECB")
    # print("2. CBC")
    # mode = input("Enter the number of the encryption mode you would like to use: ")

    # if mode == "1":
    #     mode = EncryptionMode.ECB
    # elif mode == "2":
    #     mode = EncryptionMode.CBC
    # else:
    #     print("Invalid encryption mode. Exiting...")
    #     return

    # print(f"Selected Encryption mode: {mode}")

    # # choose filename
    # filename = input("\nEnter the filename you would like to encrypt/decrypt: ")
    # print(f"Selected filename: {filename}")

    # # verify that file exists
    # try:
    #     with open(filename, "rb") as f:
    #         data = f.read()
    # except FileNotFoundError:
    #     print("File not found. Exiting...")
    #     return

    # # choose key
    # key = input("\nEnter the key you would like to use: ")

    # # verify that key is hexadecimal
    # if not is_hexadecimal(key):
    #     print("Invalid key. Exiting...")
    #     return
    # print(f"Selected key: {key}")

    # # only get iv if using CBC
    # if mode == EncryptionMode.CBC:
    #     # choose iv
    #     iv = input("\nEnter the IV you would like to use: ")

    #     # verify that iv is hexadecimal
    #     if not is_hexadecimal(iv):
    #         print("Invalid IV. Exiting...")
    #         return

    #     print(f"Selected IV: {iv}")
    # # encrypt/decrypt
    # print("\nProcessing...")
    # baby_rijndael = BabyRijndael()

    # if direction == EncryptionDirection.ENCRYPT:
    #     if mode == EncryptionMode.ECB:
    #         print("Encrypting using ECB...")
    #         result = baby_rijndael.encrypt(data, key)
    #     elif mode == EncryptionMode.CBC:
    #         print("Encrypting using CBC...")
    #         result = cbc_encrypt(data, key, iv, baby_rijndael)
    # elif direction == EncryptionDirection.DECRYPT:
    #     if mode == EncryptionMode.ECB:
    #         print("Decrypting using ECB...")
    #         result = baby_rijndael.decrypt(data, key)
    #     elif mode == EncryptionMode.CBC:
    #         print("Decrypting using CBC...")
    #         result = cbc_decrypt(data, key, iv, baby_rijndael)

    # print(f"Result: {result}")

    # # write result to file as 'filename.out'
    # with open(f"{filename}.out", "w") as f:
    #     f.write(result)

    # print("Done!")


if __name__ == "__main__":
    main()
