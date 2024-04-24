# VisioNex AI python服务
## 依赖关系和安装


##### 创建虚拟环境
```
python3 -m venv <venv_name>
```
##### 激活虚拟环境  
```
source <venv_name>/bin/activate
```


##### 下载django（先激活）
```
pip3 install django
```
##### 下载依赖


```
pip3 install -r requirements.txt
```




下载预训练模型：GFPGANv1.3.pth
在myapi目录下执行
```
wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth -P pretrained_models/

```
或者去https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth下载后放到



## 启动
```
python manage.py runserver
```