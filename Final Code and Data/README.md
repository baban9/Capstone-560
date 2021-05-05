# Capstone IDS 560 - Project Under the guidance of Prof. Kyle Cheek

The maintenance of utility poles is a cost extensive operation, and a proper plan must be in place to make it economically viable. Things that drive these investment calls are first of all the widespread nature of these utility poles. Utilities are scattered around the geographical jurisdiction of Northern Illinois, and detecting deterioration manually is very inefficient both economically and operationally. As the budget is limited, smart and informed decisions need to be made to justify the investment. 

Chalking down the location of all the poles manually is a tedious task, we try to achieve through Deep Learning . We plan to use object detection to detect utility poles with street view optical images. To automatically map roadside utility poles with crossarms (UPC), we can either use Google Street View (GSV) or high resolution aerial images detecting the shadow of the pole. Then, we will try to localize the UPCs, detect the damage to the structure, figure out how urgent it is to be repaired, and accordingly invest time and money into it.

This repository encompasses Data gathering APIs to classification models for detecting images with Utility poles and creating the bounding boxes and masks around the object of interest. 
This is a coalation of mini projects which hcan be tailored into data gathering to getting the object of interest location features.
- Environment Setup 
    - Since this project is a group collaboration we relied on Google Colab for most of the basic programming which has capabilities of python 3.7 version.
    - [requirements.txt](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/requirements.txt) provides the necessary libraries and versions we worked during the course of the project. (Note: there are many libraries inbuilt in googleColab. If you miss any library use 
    ```
    !pip install library_name
    
    To install the libraries from requirments 
    pip install -r requirements.txt
    ```
1. Data Gathering and visualization 
    - [Image downloading API.py](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/get_images_api.py) - This API takes in latitude and longitude GPS cordinates and API Key with radius of the grid and downloads all the Google Street View Images in the specified folders. 
    - [GPS cordinates.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/GPScordinates%20CSV.ipynb) - This notebook takes in 2 GPS cordinates of the region of interest boundary and increment of the images to be captures and produces a CSV file with all the cordinates and incremental cordinates for the specified grid.
    - [Data insights.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/Data%20Visualization.ipynb) - This notebooks helped us take crucial decisions from the captured data of the images.
- [Image processing.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/Image_Pre_processing%20(1).ipynb) - 
- Classification 
We used 2 different neural networks to detect if the image has poles or not. We manually picked 1000 images and labelled data into required train/val/test dataset. the dataset is available here : https://github.com/baban9/Capstone-560/releases/tag/dataset 
    - [Artificial CNN](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/A_CNN.ipynb) - This neural network contains 2 million trainable parameters trained for 25 epochs with RMSprop optimizer and learning rate of 1e-4. this model was able to give us 81% Validation accuracy. However, we relied mainly on precision (0.57) and recall (0.35) to assess the model efficacy. 
    - [Resnet Model](
- Object Detection  
    - [Keras Model object detection.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/Keras_imagenet%20object%20detection.ipynb) - This is another approach we tried to detect pole in the image from pretrained keras model on the largest dataset from google imagenet. This further gave insights how the popular and most dominant objects in image can skew the efficacy of the detection.
    - [OpenCV - Template matching.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/OpenCV%20-%20template%20matching.ipynb) - OpenCV is amalgamation of various computer vision models and methods. These models ranges from classification to objectdetection. We utilized template matching technique to detect the object of interest (utility pole) could be located in the image. This falls short if you are looking for precise location of the object in the image.
    - [Pretrained BoundingBoxes](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/bounding%20box%20attempt3.ipynb) - This time we tried to generate boxes around the objects through ResNet architecture and Inception weights. However, we can close to detect prominent classes and their probabilities. A further debugging could lead to object of interest boxes.
- Weight releases.
-  Natural Language Processing and Deep Learning
    - [Sentiment Analysis.ipynb](https://github.com/baban9/Personal-Projects/blob/master/Sentiment%20Analysis.ipynb) - Sentiment analysis refers to the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information
