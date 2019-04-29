# -*- coding: UTF-8 -*-
import os
# 验证码中的字符
# string.digits + string.ascii_uppercase
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# low_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)
MAX_CAPTCHA = 4

# 图像大小
# IMAGE_HEIGHT = 70
# IMAGE_WIDTH = 200
# TRAIN_DATASET_PATH = './dataset/200_70/train/'
# TEST_DATASET_PATH = './dataset/200_70/test/'
# VAL_DATASET_PATH = './dataset/200_70/val/'

# TRAIN_DATASET_PATH = './dataset/train000/'
# TEST_DATASET_PATH = './dataset/test000/'
# VAL_DATASET_PATH = './dataset/val000/'

# 图像大小
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160
TRAIN_DATASET_PATH = './dataset/160_60/train/'
TEST_DATASET_PATH = './dataset/160_60/test/'
VAL_DATASET_PATH = './dataset/160_60/val/'

