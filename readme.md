# VisioNex AI python服务
## 依赖关系和安装


下载django
```
pip install django
```

#### 图像修复所需依赖
- Python >= 3.7（建议使用 Anaconda 或 Miniconda）
- PyTorch >= 1.7
- NVIDIA GPU + CUDA
```
pip install basicsr
pip install facexlib
pip install -r requirements.txt
python setup.py develop
<!-- pip install realesrgan -->
```
下载预训练模型：GFPGANv1.3.pth
```
wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth -P experiments/pretrained_models
```
或者去https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth下载后放到
#### 背景去除所需依赖
```
pip install rembg # for library
pip install rembg[cli] # for library + cli
```
#### 对象移除所需依赖
```
pip install modelscope
```
#### ocr 
```
pip install paddleocr
```

## 启动
```
python manage.py runserver
```