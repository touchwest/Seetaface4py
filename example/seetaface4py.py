import ctypes
import time

lib = ctypes.cdll.LoadLibrary('./libfacerec.so')

def ConvertString2CTyoeStr(str):
    result = (ctypes.c_char * len(str))(*str)
    return result


class StructPointer(ctypes.Structure):
    _fields_ = [("isRec", ctypes.c_bool),
                ("data", ctypes.c_float * 1025)]


class FaceExt(object):
    def __init__(self):
        self.obj = lib.FaceExt_new()

    def init(self):
        lib.FaceExt_init(self.obj)

    def getFeature(self, image_path):
        return lib.FaceExt_getFeature(self.obj, image_path)


lib.FaceExt_getFeature.restype = ctypes.POINTER(StructPointer)
fe = FaceExt()
fe.init()
for i in range(0, 3):
    t1 = time.clock()
    image_path = ctypes.c_char_p(bytes("./test.jpg", 'utf-8'))
    t2 = time.clock()
    f = fe.getFeature(image_path)
    t3 = time.clock()
    print("isRec:", f.contents.isRec)
    print("data[0]:")
    print(f.contents.data[0])
    print("1", t2 - t1)
    print("2", t3 - t2)
