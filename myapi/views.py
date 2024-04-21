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

@csrf_exempt
def process_image(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        print(json_data)
        # sb9lsai7u.hn-bkt.clouddn
        # 获取图像的网络地址
        image_url = json_data.get('image_url')
        image_url = "http://sb9lsai7u.hn-bkt.clouddn.com/" + image_url
        print(image_url)
        # 用requests库获取图像的二进制
        response = requests.get(image_url)
        image = response.content

        gfpgan = GFPGANer(model_path="myapi\pretrained_models\GFPGANv1.3.pth")
        print("********1************")
        numpy_image = np.frombuffer(image, np.uint8)  # 将二进制数据转为 numpy 数组
        MatLike_image = cv2.imdecode(numpy_image, cv2.IMREAD_COLOR)  # 解码为图片矩阵
        print(type(image),"---------996-------")
        a, b, output = gfpgan.enhance(img=MatLike_image)

        print(type(output),"类型")
        # 保存在本地
        # with open("restored_img.png", 'wb') as o:
        #     o.write(output)
        cv2.imwrite('restored_img.png', output)

        with open('restored_img.png', 'rb') as image_file:
            # 读取图像数据  
            image_data = image_file.read()
        
    # 返回图像数据，设置合适的MIME类型
        return HttpResponse(image_data, content_type='image/jpeg')
        # data = {"mesg":"ok","image_data":image_data}
        # return HttpResponse(json.dumps(data))
    else:
        return HttpResponse(json.dumps({"mesg":"null"}))



        # if request.method == "POST":
        #     json_data = json.loads(request.body)
        #     base64_str = json_data.get('image_data')
        #     image_data = base64.b64decode(base64_str)
        #     print("----------")
        #     gfpgan = GFPGANer(model_path="myapi\pretrained_models\GFPGANv1.3.pth")
        #     print("********1************")
        #     image_data = np.frombuffer(image_data, np.uint8)  # 将二进制数据转为 numpy 数组
        #     image_data = cv2.imdecode(image_data, cv2.IMREAD_COLOR)  # 解码为图片矩阵
        #     print(type(image_data),"---------996-------")
        #     a, b, output = gfpgan.enhance(img=image_data)
        #     print("********2************")
        #     # 保存在本地
        #     cv2.imwrite('restored_img.png', output)
        #     print(type(output))
        #     # 转格式
        #     output = output.tobytes()
        #     output = base64.b64encode(output)
        #     output = output.decode('utf-8')
        #     # 返json
        #     data = {"img":output}
        #     return HttpResponse(json.dumps(data))
        # else:
        #     return HttpResponse(json.dumps({"mesg":"null"}))