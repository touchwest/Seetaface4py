#seetaFace4py

这个项目基于中科院山世光老师的第二代开源人脸识别引擎Seetaface2开发的用于python的链接库。

目前仅支持linux下的编译。

## 编译


```bash
cd seetaface4py
g++ -std=c++11 -c -fPIC FaceRec.cpp -o FaceRec.o -I. -I/usr/local/include -L/usr/local/lib -lopencv_core -lopencv_highgui -lopencv_imgproc  -lopencv_imgcodecs -lopencv_videoio -lSeetaFaceRecognizer -lSeetaFaceLandmarker -lSeetaFaceDetector
g++ -shared -Wl,-soname,libfacerec.so -o libfacerec.so  FaceRec.o -I. -I/usr/local/include -L/usr/local/lib -lopencv_core -lopencv_highgui -lopencv_imgproc  -lopencv_imgcodecs -lopencv_videoio -lSeetaFaceRecognizer -lSeetaFaceLandmarker -lSeetaFaceDetector
```

去[SeetaFace2](https://github.com/seetafaceengine/SeetaFace2)下载模型文件
创建model文件夹，将下载的模型放入文件夹。

## Demo

将下载的模型放入model中

```python
import ctypes

lib = ctypes.cdll.LoadLibrary('./libexample.so')

def ConvertString2CTyoeStr(str):
    result = (ctypes.c_char * len(str))(*str)
    return result


class StructPointer(ctypes.Structure):
    _fields_ = [("isRec", ctypes.c_bool),
                ("data", ctypes.c_float * 1025)]


lib.getFeature.restype = ctypes.POINTER(StructPointer)

image_path = ctypes.c_char_p(bytes("./test.jpg",'utf-8'))

f = lib.getFeature(image_path)

print("isRec:", f.contents.isRec)
print("data[0]:")
print(f.contents.data[0])

```

####Output

```python
[INFO] FaceDetector: Core size: 640x480
[INFO] FaceLandmarker: Number: 81
[INFO] FaceRecognizer: Feature size: 1024
Loading image... ./test.jpg
start extract...
Extract pass
1024 features!
0.00573871
isRec: True
data[0]:
0.005738707724958658
```

## 结尾
感谢山世光老师对人脸识别领域做出的贡献，不忘初心，砥砺前行。
