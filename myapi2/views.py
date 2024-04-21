from django.shortcuts import render,HttpResponse
import json
import cv2
from rembg import remove
import base64
from django.views.decorators.csrf import csrf_exempt
import requests
from PIL import Image
from io import BytesIO
@csrf_exempt
def background_removal(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        # 获取图像的网络地址
        image_url = json_data.get('image_url')
        image_url = "http://sb9lsai7u.hn-bkt.clouddn.com/" + image_url
        # 用requests库获取图像的二进制
        response = requests.get(image_url)
        image = response.content

        # base64_str = json_data.get('image_data')
        # image_data = base64.b64decode(base64_str)
        # 移除背景
        output = remove(data=image,bgcolor=(255, 255, 255, 255))
        print(type(output),"type____")
        # 保存在本地
        with open("rembg_img.png", 'wb') as o:
            o.write(output)
        # cv2.imwrite('restored_img.png', output)
        with open("rembg_img.png", "rb") as image_file:
            image_data = image_file.read()
        return HttpResponse(image_data, content_type='image/png')
    else:
        return HttpResponse(json.dumps({"mesg":"null"}))