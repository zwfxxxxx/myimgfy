from django.shortcuts import render, HttpResponse
import json
import numpy as np
import cv2
import requests
from django.views.decorators.csrf import csrf_exempt
from gfpgan import GFPGANer

# 定义一个接收POST请求并处理图像的函数
@csrf_exempt
def process_image(request):
    if request.method == "POST":
        # 解析请求中的json数据
        json_data = json.loads(request.body)
        print(json_data)
        # 获取图像链接
        image_url = json_data.get('image_url')
        image_url = "http://sb9lsai7u.hn-bkt.clouddn.com/" + image_url
        print(image_url)
        # 从链接获取图像数据
        response = requests.get(image_url)
        image = response.content

        # 初始化GFPGANer对象
        gfpgan = GFPGANer(model_path="myapi\pretrained_models\GFPGANv1.3.pth")
        print("********1************")
        
        # 将图像数据转换为numpy数组
        numpy_image = np.frombuffer(image, np.uint8)  
        # 将numpy数组解码为OpenCV中的Mat
        MatLike_image = cv2.imdecode(numpy_image, cv2.IMREAD_COLOR) 
        print(type(image),"---------996-------")
        # 使用GFPGAN增强图像
        a, b, output = gfpgan.enhance(img=MatLike_image)

        print(type(output),"类型")
        # 将增强后的图像保存为文件
        cv2.imwrite('restored_img.png', output)

        # 读取增强后的图像文件并返回HttpResponse对象
        with open('restored_img.png', 'rb') as image_file:
            image_data = image_file.read()
        
        return HttpResponse(image_data, content_type='image/jpeg')
    else:
        # 如果请求不是POST，则返回空消息
        return HttpResponse(json.dumps({"mesg":"null"}))