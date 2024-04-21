from django.shortcuts import render, HttpResponse
from django.shortcuts import render,HttpResponse
import json
import cv2
from django.views.decorators.csrf import csrf_exempt
import requests
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

@csrf_exempt
def ocr(request):
    if request.method == "POST":
        json_data = json.loads(request.body)

        target_img = json_data.get('input_location')
        response = requests.get("http://sb9lsai7u.hn-bkt.clouddn.com/" + target_img)
        image = response.content
        with open("ocr_img\\ocr.png", "wb") as o:
            o.write(image)
        # load model
        # Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改 lang参数进行切换
        # lang参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`
        #ocr对象
        ocr = PaddleOCR(lang="ch",
                        use_gpu=False,
                        det_model_dir="../paddleORC_model/ch_ppocr_server_v2.0_det_infer/",
                        cls_model_dir="ch_ppocr_mobile_v2.0_cls_infer/",
                        rec_model_dir="ch_ppocr_server_v2.0_rec_infer/")
        


        ret = ''

        # 识别打印
        img_path = "ocr_img\\ocr.png"
        result = ocr.ocr(img_path)
        for idx in range(len(result)):
            res = result[idx]
            with open("ocr.txt", "w") as f:
                for line in res:
                    f.write(line[1][0]+"/n")
                    print(line[1][0])
                    ret = ret + line[1][0] + "\n"
        # # 注：
        # # result是一个list，每个item包含了文本框，文字和识别置信度
        # # line的格式为：
        # # [[[3.0, 149.0], [43.0, 149.0], [43.0, 163.0], [3.0, 163.0]], ('人心安', 0.6762619018554688)]
        # # 文字框 boxes = line[0]，包含文字框的四个角的(x,y)坐标
        # # 文字 txts = line[1][0]
        # # 识别置信度 scores = line[1][1]

        # # visual
        # image = Image.open(img_path).convert('RGB')
        # boxes = [line[0] for line in result]
        # txts = [line[1][0] for line in result]
        # scores = [line[1][1] for line in result]
        # im_show = draw_ocr(image, boxes, txts, scores)
        # im_show = Image.fromarray(im_show)
        # im_show.save('result.jpg')





        # 文字识别：
        # 保存在本地
        # with open("rembg_img.png", 'wb') as o:
        #     o.write(output)
        # with open("rembg_img.png", "rb") as image_file:
        #     image_data = image_file.read()
    
        return HttpResponse(ret)
    else:
        return HttpResponse(json.dumps({"mesg":"null"}))