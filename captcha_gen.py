# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
import random as rd
import captcha_setting


def generate_captcha(save_path, num):
    """
    :param save_path: the path to save img
    :param num:       the num of spider img
    :return:
    """
    max_captcha = captcha_setting.MAX_CAPTCHA       # 验证码字符个数
    all_char_set = captcha_setting.ALL_CHAR_SET     # 字符集合
    img_width = captcha_setting.IMAGE_WIDTH
    img_height = captcha_setting.IMAGE_HEIGHT
    for i in range(num):
        ran_str = ''.join(rd.sample(all_char_set, max_captcha))
        file_name = save_path + '{}_'.format(i) + ran_str + '.png'
        ImageCaptcha(width=img_width, height=img_height).write(ran_str, file_name)


def main():
    # 通过改变此处目录，以生成 训练、测试和预测用的验证码集 TRAIN VAL TEST
    save_path = captcha_setting.TRAIN_DATASET_PATH
    generate_captcha(save_path, 100)


if __name__ == '__main__':
    main()
