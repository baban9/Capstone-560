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
- Data Gathering and visualization 
    - [GPS cordinates.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/GPScordinates%20CSV.ipynb) - This notebook takes in 2 GPS cordinates of the region of interest boundary and increment of the images to be captures and produces a CSV file with all the cordinates and incremental cordinates for the specified grid.
    - [Data insights.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/Data%20Visualization.ipynb) - This notebooks helped us take crucial decisions from the captured data of the images.
- [Image processing.ipynb](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/Image_Pre_processing%20(1).ipynb) - 
- Classification 
We used 2 different neural networks to detect if the image has poles or not. We manually picked 1000 images and labelled data into required train/val/test dataset. the dataset is available here : https://github.com/baban9/Capstone-560/releases/tag/dataset 
    - [Artificial CNN](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/A_CNN.ipynb) - This neural network contains 2 million trainable parameters trained for 25 epochs with RMSprop optimizer and learning rate of 1e-4. this model was able to give us 81% Validation accuracy. However, we relied mainly on precision (0.57) and recall (0.35) to assess the model efficacy. 
    - [Resnet Model](
- Object Detection
- Weight releases.
-  Natural Language Processing and Deep Learning
    - [Sentiment Analysis.ipynb](https://github.com/baban9/Personal-Projects/blob/master/Sentiment%20Analysis.ipynb) - Sentiment analysis refers to the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information
