from django.test import TestCase

# Create your tests here.
from django.shortcuts import render, HttpResponse
import json
from django.shortcuts import render,HttpResponse
from gfpgan import GFPGANer
# from rembg import remove
# import base64
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
import requests
with open('D:/study/pydjango/img_django/myimgfy/img/3.webp', 'rb') as image_file:
    # 读取图像数据  
    image_data = image_file.read()
gfpgan = GFPGANer(model_path="D:\study\pydjango\img_django\myimgfy\myapi\pretrained_models\GFPGANCleanv1-NoCE-C2.pth")
print("********1************")
numpy_image = np.frombuffer(image_data, np.uint8)  # 将二进制数据转为 numpy 数组
MatLike_image = cv2.imdecode(numpy_image, cv2.IMREAD_COLOR)  # 解码为图片矩阵
print(type(MatLike_image),"---------996-------")
a, b, output = gfpgan.enhance(img=MatLike_image)

print(type(output),"类型")
# 保存在本地
# with open("restored_img.png", 'wb') as o:
#     o.write(output)
cv2.imwrite('restored_img.png', output)