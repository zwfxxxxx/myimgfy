# 导入所需的库和模块
from django.shortcuts import render, HttpResponse
import json
import cv2
from django.views.decorators.csrf import csrf_exempt
import requests
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

# 定义一个视图函数，用于处理OCR请求
@csrf_exempt
def ocr(request):
    # 判断请求是否为POST方法
    if request.method == "POST":
        # 解析请求中的JSON数据
        json_data = json.loads(request.body)

        # 从JSON数据中获取目标图片的位置
        target_img = json_data.get('input_location')
        
        # 从特定URL请求目标图片的内容
        response = requests.get("http://sb9lsai7u.hn-bkt.clouddn.com/" + target_img)
        image = response.content
        
        # 将获取的图片内容写入本地文件
        with open("ocr_img\\ocr.png", "wb") as o:
            o.write(image)
        
        # 初始化PaddleOCR模型
        ocr = PaddleOCR(lang="ch",
                        use_gpu=False,
                        det_model_dir="../paddleORC_model/ch_ppocr_server_v2.0_det_infer/",
                        cls_model_dir="ch_ppocr_mobile_v2.0_cls_infer/",
                        rec_model_dir="ch_ppocr_server_v2.0_rec_infer/")
        
        ret = ''  # 初始化结果字符串
        img_path = "ocr_img\\ocr.png"
        
        # 使用OCR模型识别图片中的文字
        result = ocr.ocr(img_path)
        
        # 遍历识别结果，并将识别的文字保存到文件和返回结果字符串中
        for idx in range(len(result)):
            res = result[idx]
            with open("ocr.txt", "w") as f:
                for line in res:
                    f.write(line[1][0] + "/n")
                    ret = ret + line[1][0] + "\n"
        
        # 返回识别结果字符串
        return HttpResponse(ret)
    else:
        # 返回空消息的JSON格式
        return HttpResponse(json.dumps({"mesg": "null"}))