from distutils.core import setup, Extension

FACEEXT_EXT = Extension(
    name="_faceext",
    swig_opts=["-c++"],
    include_dirs=[
        '/usr/local/include',
    ],
    library_dirs=[
        '/usr/local/lib'
    ],
    libraries=[
        'opencv_core',
        'opencv_highgui',
        'opencv_imgproc',
        'opencv_imgcodecs',
        'opencv_videoio',
        'SeetaFaceRecognizer',
        'SeetaFaceLandmarker',
        'SeetaFaceDetector',
    ],
    sources=[
        "Faceext.cpp",
        "Faceext.i",
    ],
    extra_compile_args=[
        '-g',
        '-std=c++11'
    ],
)

setup(name = "faceext",
      version = "1.0",
      ext_modules = [FACEEXT_EXT]
     )