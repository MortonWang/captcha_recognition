# -*- coding: UTF-8 -*-
import numpy as np
import captcha_setting


def encode(text):
    vector = np.zeros(captcha_setting.ALL_CHAR_SET_LEN * captcha_setting.MAX_CAPTCHA, dtype=float)
    for i, c in enumerate(text):
        idx = i * captcha_setting.ALL_CHAR_SET_LEN + char2pos(c)
        vector[idx] = 1.0
    return vector


def char2pos(c):    # 字符 c 对应的位置
    if c == '_':
        k = 62
        return k
    k = ord(c)-48
    if k > 9:
        k = ord(c) - 65 + 10
        if k > 35:
            k = ord(c) - 97 + 26 + 10
            if k > 61:
                raise ValueError('error')
    return k


def decode(vec):
    char_pos = vec.nonzero()[0]
    text = []
    for i, c in enumerate(char_pos):
        char_idx = c % captcha_setting.ALL_CHAR_SET_LEN
        if char_idx < 10:
            char_code = char_idx + ord('0')
        elif char_idx < 36:
            char_code = char_idx - 10 + ord('A')
        elif char_idx < 62:
            char_code = char_idx - 36 + ord('a')
        elif char_idx == 62:
            char_code = ord('_')
        else:
            raise ValueError('error')
        text.append(chr(char_code))
    return "".join(text)


if __name__ == '__main__':
    e = encode("RXRX")
    print(e)
    print(decode(e))
