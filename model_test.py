# -*- coding: UTF-8 -*-
"""
test the trained model, by using test_data
"""
from captcha_cnn_model import CNN
import torch
from captcha_main import model_evaluate
import my_dataset
import captcha_setting

test_data = my_dataset.get_data(captcha_setting.TEST_DATASET_PATH,
                                batch=256, shuffle=False)
cnn = CNN()
cnn.cuda()      # use gpu
cnn.load_state_dict(torch.load('./model/-lr:0.0014-acc:0.829.pkl'))
test_acc = model_evaluate(cnn, test_data, test_flag=True)
info_log = "-test_acc:{}\n\n".format(test_acc)
print(info_log)






'''
import torch
import my_dataset
import captcha_setting

from captcha_cnn_model import CNN
from visualize import make_dot
from torch.autograd import Variable

test_data = my_dataset.get_data(captcha_setting.TEST_DATASET_PATH, batch=512, shuffle=False)
model = CNN()
for i, (images, labels) in enumerate(test_data):
	if i>0:
		break
	images = Variable(images)
	labels = Variable(labels.float())
	predict_labels = model(images)
	print(predict_labels)

g = make_dot(predict_labels)
g.view()
# g.render('here', view=False)

'''


from torchvision import datasets,transforms

# writer就相当于一个日志，保存你要做图的所有信息。
# 第二句就是在你的项目目录下建立一个文件夹log，存放画图用的文件。
# 刚开始的时候是空的
import torch
# import my_dataset
# import captcha_setting
# from captcha_cnn_model import CNN
# from torch.autograd import Variable
#
# import torchvision
# from tensorboardX import SummaryWriter
# writer = SummaryWriter('./log')  # 建立一个保存数据用的东西
#
# test_data = my_dataset.get_data(captcha_setting.TEST_DATASET_PATH, batch=1, shuffle=False)
# model = CNN()
# for i, (images, labels) in enumerate(test_data):
# 	if i > 0:
# 		break
# 	images = Variable(images)
# 	labels = Variable(labels.float())
#
# 	writer.add_graph(model, images)

	# predict_labels = model(images)
	# print(predict_labels)
	# with SummaryWriter(comment='MyCNN') as w:
	# 	w.add_graph(model, images)

# model = torchvision.models.resnet18(False)
# writer.add_graph(model, torch.rand([1,3,224,224]))   # 自己定义的网络有时显示错误
