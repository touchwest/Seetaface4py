#include "Faceext.h"

Faceext::Faceext():FD(nullptr), FL(nullptr), FR(nullptr){}


void Faceext::init()
{
    seeta::ModelSetting::Device device = seeta::ModelSetting::CPU;
    int id = 0;
    seeta::ModelSetting FD_model( "./model/fd_2_00.dat", device, id );
    seeta::ModelSetting FL_model( "./model/pd_2_00_pts5.dat", device, id );
    seeta::ModelSetting FR_model( "./model/fr_2_10.dat", device, id );
        
    FD = new seeta::FaceDetector(FD_model);
	FL = new seeta::FaceLandmarker(FL_model);
    FR = new seeta::FaceRecognizer(FR_model);
    
    FD->set(seeta::FaceDetector::PROPERTY_VIDEO_STABLE, 1);
}


Feature Faceext::getFeatures(char* image_path)
{
    Feature feature;

    std::cout<<"Loading image... " << image_path << std::endl;
    auto img = cv::imread(image_path);
    seeta::cv::ImageData image = img;
    
    if(image.empty())
    {
        std::cerr << "Can not load image " << image_path << " , Please check your image path." << std::endl;
        feature.isRec = false;
        return feature;
    }

    auto faces = FD->detect(image);

    if(faces.size != 1)
    {
        std::cerr << "detect more than one face, Please check image" << image_path << std::endl;
        feature.isRec = false;
        return feature;
    }

    
    auto face = faces.data[0];
    auto points = FL->mark(image, face.pos);
    auto pps = &points[0];

    std::cout<<"start extract..."<<std::endl;
    if(FR->Extract(image, pps, feature.data))
    {
        feature.isRec = true;
        return feature;
    }
    else
    {
        feature.isRec = false;
        return feature;
    }
    feature.isRec = false;
	return feature;
}

float Faceext::CalSimilar(float *fc1, float *fc2)
{
    long dim = FR->GetExtractFeatureSize();
    double dot = 0;
    double norm1 = 0;
    double norm2 = 0;
    for( size_t i = 0; i < dim; ++i ) 
    {
        dot += fc1[i] * fc2[i];
        norm1 += fc1[i] * fc1[i];
        norm2 += fc2[i] * fc2[i];
    }   
    double similar = dot / ( sqrt( norm1 * norm2 ) + 1e-5 );
    //cout <<"similar(C):" << similar <<endl;
    return float(similar);
}

