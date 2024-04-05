from baby_rijndael.enums import EncryptionDirection, EncryptionMode
from baby_rijndael.rijndael import BabyRijndael


def main() -> None:
    # # initial welcome
    # print("Welcome to Baby Rijndael!")

    # # choose direction
    # print("Will you encrypt or decrypt?")
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
    # print("What encryption mode would you like to use?")
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
    # filename = input("Enter the filename you would like to encrypt/decrypt: ")
    # print(f"Selected filename: {filename}")

    # # choose key
    # key = input("Enter the key you would like to use: ")

    # # verify that key is 16bit integer
    # if len(key) != 16:
    #     print("Invalid key. Exiting...")
    #     return

    # # choose iv
    # iv = input("Enter the IV you would like to use: ")
    mode = EncryptionMode.ECB
    direction = EncryptionDirection.ENCRYPT
    filename = "test.txt"
    key = "6b5d"
    iv = None
    block = "2ca5"

    baby_rijndael = BabyRijndael(mode, direction, filename, key, iv)
    baby_rijndael.run(block)


if __name__ == "__main__":
    main()
