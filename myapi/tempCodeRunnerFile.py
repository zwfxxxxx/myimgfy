
import requests
with open('D:/study/pydjango/img_django/myimgfy/img/3.webp', 'rb') as image_file:
    # 读取图像数据  
    image_data = image_file.read()
gfpgan = GFPGANer(model_path="D:\study\pydjango\img_django\myimgfy\myapi\pr