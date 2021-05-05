# Capstone IDS 560 - Project Under the guidance of Prof. Kyle Cheek

The maintenance of utility poles is a cost extensive operation, and a proper plan must be in place to make it economically viable. Things that drive these investment calls are first of all the widespread nature of these utility poles. Utilities are scattered around the geographical jurisdiction of Northern Illinois, and detecting deterioration manually is very inefficient both economically and operationally. As the budget is limited, smart and informed decisions need to be made to justify the investment. 

Chalking down the location of all the poles manually is a tedious task, we try to achieve through Deep Learning . We plan to use object detection to detect utility poles with street view optical images. To automatically map roadside utility poles with crossarms (UPC), we can either use Google Street View (GSV) or high resolution aerial images detecting the shadow of the pole. Then, we will try to localize the UPCs, detect the damage to the structure, figure out how urgent it is to be repaired, and accordingly invest time and money into it.

This repository encompasses Data gathering APIs to classification models for detecting images with Utility poles and creating the bounding boxes and masks around the object of interest. 
This is a coalation of mini projects which hcan be tailored into data gathering to getting the object of interest location features.
- Environment Setup 
    - Since this project is a group collaboration we relied on Google Colab for most of the basic programming which has capabilities of python 3.7 version.
    - [requirements.txt](https://github.com/baban9/Capstone-560/blob/main/Final%20Code%20and%20Data/requirements.txt) provides the necessary libraries and versions we worked during the course of the project. (Note: there are many libraries inbuilt in googleColab. If you miss any library use 
    !pip install library_name 
    inside the colab notebook cell
    - 
- Data Gathering 
- Image processing
- Classification 
- Object Detection
- Weight releases.
-  Natural Language Processing and Deep Learning
    - [Sentiment Analysis.ipynb](https://github.com/baban9/Personal-Projects/blob/master/Sentiment%20Analysis.ipynb) - Sentiment analysis refers to the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information
