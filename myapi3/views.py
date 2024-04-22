# 导入所需的库
from django.shortcuts import render, HttpResponse
import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import json
from django.views.decorators.csrf import csrf_exempt
import paddleocr
import base64
import requests

'''
对象移除
'''
@csrf_exempt
def obj_removal(request):
    # 检查请求是否为POST
    if request.method == "POST":
        # 从请求的JSON数据中加载信息
        json_data = json.loads(request.body)
        # 获取输入图片的URL
        input_url = json_data.get("input_location")
        # 从URL获取图片内容
        response = requests.get("http://sb9lsai7u.hn-bkt.clouddn.com/" + input_url)
        image = response.content
        # 将图片内容保存到指定路径下
        with open("obj_remove_img\\input_location.png", 'wb') as o:
            o.write(image)

        # 获取输入的mask信息并解码
        base64_str = json_data.get('input_mask_location')
        base64_str = base64_str.split(",")
        input_mask = base64.b64decode(base64_str[1])
        # 将mask内容保存到指定路径下
        with open("obj_remove_img\\input_mask_location.png", 'wb') as o:
            o.write(input_mask)

        # 设置输入的图片路径和mask路径
        input_location = "obj_remove_img\\input_location.png"
        input_mask_location = "obj_remove_img\\input_mask_location.png"

        # 构建输入字典
        input = {
            'img': input_location,
            'mask': input_mask_location,
        }

        # 初始化一个图像修复的pipeline
        inpainting = pipeline(Tasks.image_inpainting, model='damo/cv_fft_inpainting_lama')
        # 执行图像修复操作
        result = inpainting(input)
        # 获取修复后的图片
        vis_img = result[OutputKeys.OUTPUT_IMG]
        # 将修复后的图片保存到指定路径下
        cv2.imwrite('obj_remove_img\\obj_remove.png', vis_img)

        # 将修复后的图片读取为二进制格式
        with open("obj_remove_img\\obj_remove.png", "rb") as f:
            ret = f.read()
        # 返回修复后的图片
        return HttpResponse(ret)
    else:
        # 返回空消息
        return HttpResponse(json.dumps({"mesg": "null"}))