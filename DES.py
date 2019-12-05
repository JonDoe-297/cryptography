ip = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
pc1 = [57, 49, 41, 33, 25, 17, 9, 1,
       58, 50, 42, 34, 26, 18, 10, 2,
       59, 51, 43, 35, 27, 19, 11, 3,
       60, 52, 44, 36, 63, 55, 47, 39,
       31, 23, 15, 7, 62, 54, 46, 38,
       30, 22, 14, 6, 61, 53, 45, 37,
       29, 21, 13, 5, 28, 20, 12, 4]
pc2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]
d = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
e = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]
s = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
     [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
     [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
     [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
     [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
     [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
     [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
     [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
p = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]
ip_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]


def text_change(IP_text):
    changed_text = ''
    for i in range(64):
        changed_text += IP_text[ip[i] - 1]
    return changed_text


def key_change(IP_key):
    changed_key = ''
    for i in range(56):
        changed_key += IP_key[pc1[i] - 1]
    return changed_key


def round_key(first_changed_key):
    key_list = []
    key_l = first_changed_key[0:28]
    key_r = first_changed_key[28:56]
    for i in range(16):
        # 旋转密钥
        key_l = key_l[d[i]:28] + key_l[0:d[i]]
        key_r = key_r[d[i]:28] + key_r[0:d[i]]
        key = key_l + key_r
        return_list = ''
        for i in range(48):
            return_list += key[pc2[i] - 1]
        key_list.append(return_list)
    return key_list


def expend_E(text):
    return_list = ''
    for i in range(48):
        return_list += text[e[i] - 1]
    return return_list


def Sbox_change(text):
    return_list = ''
    for i in range(8):
        row = int(str(text[i * 6]) + str(text[i * 6 + 5]), 2)  # 选择行
        raw = int(str(text[i * 6 + 1]) + str(text[i * 6 + 2]) + str(text[i * 6 + 3]) + str(text[i * 6 + 4]), 2)  # 选择列
        return_list += hex_to_four_binary(s[i][row][raw], 4)  # 选择一个数，并转换为4位2进制数
    return return_list


def Pbox_change(text):
    return_list = ''
    for i in range(32):
        return_list += text[p[i] - 1]
    return return_list


def xor(text, key):
    code_len = len(key)
    return_list = ''
    # print(text)
    for i in range(code_len):
        return_list += str(int(text[i]) ^ int(key[i]))
    return return_list


def final_change(text):
    return_list = ''
    for i in range(64):
        return_list += text[ip_1[i] - 1]
    return return_list


def unicode_to_hex(string):
    hex_string = ''
    for i in string:
        hex_string += "%02x" % ord(i)
    return hex_string


def hex_to_unicode(string):
    return_string = ''
    string_len = len(string)
    for i in range(0, string_len, 2):
        return_string += chr(int(string[i:i + 2], 16))
    return return_string


def bin_to_hex(string):
    lens = len(string)
    tohex = ''
    for i in range(0, lens, 4):
        list = string[i] + string[i + 1] + string[i + 2] + string[i + 3]
        tohex += "%x" % int(list, 2)
    return tohex


def hex_to_four_binary(o, lens):
    return_code = ''
    for i in range(lens):
        return_code = str(o >> i & 1) + return_code
    return return_code


def complement_residue(string):
    res = 64 - len(string)
    string += '0' * res
    return string


def des_encryption(des_binary_text, des_binary_key):
    # text_len = len(des_binary_text)
    output = ''
    first_changed_key = key_change(des_binary_key)
    key_list = round_key(first_changed_key)
    for n in range(0, len(des_binary_text), 64):
        current_text = des_binary_text[n:n + 64]
        current_text_changed = text_change(current_text)
        for m in range(16):
            text_l = current_text_changed[0:32]
            text_r = current_text_changed[32:64]
            current_text_changed = text_r
            text_r = expend_E(text_r)
            text_r = xor(text_r, key_list[m])
            text_r = Sbox_change(text_r)
            text_r = Pbox_change(text_r)
            text_r = xor(text_l, text_r)
            current_text_changed += text_r
        text_l = current_text_changed[0:32]
        text_r = current_text_changed[32:64]
        current_text_changed = text_r + text_l
        output += final_change(current_text_changed)
    return output


if __name__ == "__main__":
    way = input("ECB加密模式请输入：ECB\nCBC加密模式请输入：CBC\nCFB加密模式请输入：CFB\nOFB加密模式请输入：OFB\n")
    # way = 'OFB'
    while way != 'ECB' and way != 'CBC' and way != 'CFB' and way != 'OFB':
        print("输入格式错误，请重新输入！")
        way = input("ECB模式请输入：ECB\nCBC模式请输入：CBC\n")
    plaintext = input("请输入明文：")
    key = input("请输入密钥：")
    # plaintext = 'asdfasdf'
    # key = '123456'
    if way == 'ECB':
        binary_text = bin(int(unicode_to_hex(plaintext), 16))[2:]
        binary_key = bin(int(unicode_to_hex(key), 16))[2:]
        binary_text = complement_residue(binary_text)
        binary_key = complement_residue(binary_key)
        ciphertext = des_encryption(binary_text, binary_key)
        ciphertext = bin_to_hex(ciphertext)
        # ciphertext = hex_to_unicode(ciphertext)
        print(ciphertext)
    elif way == 'CBC':
        # plaintext = 'asdfasdf'
        # key = '123456'
        rage = ["0011000100110011001100110011011000110110001110000011010100110101"]
        ciphertext = ''
        output = ''
        binary_text = bin(int(unicode_to_hex(plaintext), 16))[2:]
        binary_key = bin(int(unicode_to_hex(key), 16))[2:]
        binary_text = complement_residue(binary_text)
        binary_key = complement_residue(binary_key)
        lens = len(binary_text)
        j = 0
        for i in range(0, lens, 64):
            mix_binary_text = xor(binary_text[i:i + 64], rage[j])
            ciphertext = des_encryption(mix_binary_text, binary_key)
            output += ciphertext
            rage.append(ciphertext)
            j = j + 1
        print(bin_to_hex(ciphertext))
        # print('CBC')
    elif way == 'CFB':
        # plaintext = 'asdfasdf'
        # key = '123456'
        rage = ["0011000100110011001100110011011000110110001110000011010100110101"]
        ciphertext = ''
        output = ''
        binary_text = bin(int(unicode_to_hex(plaintext), 16))[2:]
        binary_key = bin(int(unicode_to_hex(key), 16))[2:]
        binary_text = complement_residue(binary_text)
        binary_key = complement_residue(binary_key)
        lens = len(binary_text)
        j = 0
        for i in range(0, lens, 64):
            ciphertext = des_encryption(rage[i], binary_key)
            ciphertext = xor(binary_text, ciphertext)
            output += ciphertext
            rage.append(ciphertext)
            j = j + 1
        print(bin_to_hex(ciphertext))
        # print('CFB')
    elif way == 'OFB':
        # plaintext = 'asdfasdf'
        # key = '123456'
        rage = ["0011000100110011001100110011011000110110001110000011010100110101"]
        ciphertext = ''
        output = ''
        binary_text = bin(int(unicode_to_hex(plaintext), 16))[2:]
        binary_key = bin(int(unicode_to_hex(key), 16))[2:]
        binary_text = complement_residue(binary_text)
        binary_key = complement_residue(binary_key)
        lens = len(binary_text)
        j = 0
        for i in range(0, lens, 64):
            ciphertext = des_encryption(rage[i], binary_key)
            rage.append(ciphertext)
            ciphertext = xor(binary_text, ciphertext)
            output += ciphertext
            j = j + 1
        print(bin_to_hex(ciphertext))
        # print('OFB')