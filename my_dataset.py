# -*- coding: UTF-8 -*-
import os
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image
import one_hot_encoding as ohe


class mydataset(Dataset):

    def __init__(self, folder, transform=None):
        self.train_image_file_paths = [os.path.join(folder, image_file) for image_file in os.listdir(folder)]
        self.transform = transform

    def __len__(self):
        return len(self.train_image_file_paths)

    def __getitem__(self, idx):
        image_root = self.train_image_file_paths[idx]
        image_name = image_root.split(os.path.sep)[-1]
        image = Image.open(image_root)
        if self.transform is not None:
            image = self.transform(image)
        label = ohe.encode(image_name.split('_')[1].split('.')[0])
        # 为了方便，在生成图片的时候，图片文件的命名格式 "序号_4个字符.PNG",
        # 4个字符即是图片的验证码的值，字母大写,同时对该值做 one-hot 处理
        return image, label


transform = transforms.Compose([
    # transforms.ColorJitter(),     # 随机改变图像的亮度对比度和饱和度
    transforms.Grayscale(),         # 将图像转换为灰度图像
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def get_data(path, batch, shuffle):
    dataset = mydataset(path, transform=transform)
    return DataLoader(dataset, batch_size=batch, shuffle=shuffle)
