from django.shortcuts import render,HttpResponse
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

    if request.method =="POST":

        json_data = json.loads(request.body)
        # input_location = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/image_inpainting/image_inpainting.png'
        # input_mask_location = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/image_inpainting/image_inpainting_mask.png'
        # input_location = "http://sb9lsai7u.hn-bkt.clouddn.com/" + json_data.get("input_location")
        # print(input_location,"----")
        #获取
        input_url =  json_data.get("input_location")
        response = requests.get("http://sb9lsai7u.hn-bkt.clouddn.com/" + input_url)
        image = response.content
        with open("obj_remove_img\\input_location.png", 'wb') as o:
                o.write(image)

        #获取mask的base64在写入临时文件
        base64_str = json_data.get('input_mask_location')
        base64_str = base64_str.split(",")
        input_mask = base64.b64decode(base64_str[1])
        with open("obj_remove_img\\input_mask_location.png", 'wb') as o:
                o.write(input_mask)
                # cv2.imwrite('restored_img.png', output)


        # 获取input和mask的路径
        input_location = "obj_remove_img\\input_location.png"
        input_mask_location = "obj_remove_img\\input_mask_location.png"
        print(type(input_mask_location))
        input = {
                'img':input_location,
                'mask':input_mask_location,
        }
        print("-------")
        inpainting = pipeline(Tasks.image_inpainting, model='damo/cv_fft_inpainting_lama')
        result = inpainting(input)
        print("--------")
        vis_img = result[OutputKeys.OUTPUT_IMG]#去除对象后的图片：
        #放入临时文件
        cv2.imwrite('obj_remove_img\\obj_remove.png', vis_img)
        #读取并返回结果图像
        with open("obj_remove_img\\obj_remove.png","rb") as f:
            ret = f.read()
        return  HttpResponse(ret)
    else:
        return HttpResponse(json.dumps({"mesg":"null"}))