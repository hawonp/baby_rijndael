# # 0x3516bd2b	0x1111	0x0000	0xe6d25de9
# # data key iv result
# from baby_rijndael.rijndael import BabyRijndael
# from baby_rijndael.utils import calc_xor, get_hex_stream


# def cbc_encrypt(
#     input: str,
#     key: str,
#     iv: str,
# ):
#     # remove 0x prefix
#     input = input[2:]

#     # split input into 16bit blocks
#     blocks = [input[i : i + 4] for i in range(0, len(input), 4)]
#     result = get_hex_stream(iv)
#     baby_rijndael = BabyRijndael(key)
#     output = ""
#     for i in range(len(blocks)):
#         plaintext_block = get_hex_stream(blocks[i])
#         xor_result_list = calc_xor(plaintext_block, result)
#         xor_result = "".join(xor_result_list)
#         result: str = baby_rijndael.encrypt(xor_result)
#         output += result

#     return output
