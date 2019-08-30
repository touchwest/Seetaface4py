%module faceext

%{
#include "Faceext.h"
%}


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
