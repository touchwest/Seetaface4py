#ifndef FACEREC_H__
#define FACEREC_H__

#pragma warning(disable: 4819)

#include <seeta/FaceDetector.h>
#include <seeta/FaceLandmarker.h>
#include <seeta/FaceRecognizer.h>

#include <seeta/Struct.h>
#include <seeta/Struct_cv.h>
#include <seeta/CFaceInfo.h>

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <vector>
#include <cmath>
#include <map>
#include <iostream>
#include <string>

struct Feature{
    bool isRec;
    float data[1025];
};

class Faceext
{
  public:
    Faceext();

    void init();
    Feature getFeatures(char*);
    float CalSimilar(float*, float*);

    seeta::FaceDetector *FD;
    seeta::FaceLandmarker *FL;
    seeta::FaceRecognizer *FR;
       
};

#endif // FACEREC_H__
