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


