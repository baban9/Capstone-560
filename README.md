# Capstone 560: Utility Pole Detection

End-to-end computer vision pipeline for detecting utility poles with crossarms (UPC) from street-view imagery. Built as an IDS 560 capstone under Prof. Kyle Cheek.

## Problem

Manual utility pole inspection is costly and does not scale across large geographic regions. Automated detection from street-view images enables prioritization of maintenance spend.

## Approach

| Stage | Artifact | Method |
|-------|----------|--------|
| Data collection | `get_images_api.py`, GPS notebooks | Google Street View API over a lat/lon grid |
| EDA | `Data Visualization.ipynb` | Distribution and quality checks |
| Preprocessing | `Image_Pre_processing (1).ipynb` | Histogram equalization, Laplacian transforms |
| Classification | `A_CNN.ipynb`, `pole_features.ipynb` | Custom CNN (81% val accuracy) |
| Detection | Mask R-CNN notebooks | Instance segmentation and bounding boxes |

Model weights and datasets are published in [GitHub Releases](https://github.com/baban9/Capstone-560/releases).

## Team

- Babandeep Singh
- Danielle Strejc
- Rongchuan Guo
- Utkarsh Ujwal

## Repository structure

```
Final Code and Data/
  get_images_api.py       Street View image downloader
  A_CNN.ipynb             Classification model
  requirements.txt        Pinned dependencies
  ...                     Notebooks for each pipeline stage
```

## Reproducibility

```bash
cd "Final Code and Data"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Download model weights and labeled data from Releases before running detection notebooks.

## Tech stack

Python 3.7+, TensorFlow 1.x/Keras, OpenCV, Mask R-CNN, Google Street View API

## Results

- CNN classifier with 81% validation accuracy (precision 0.57, recall 0.35)
- Mask R-CNN pipeline for pole instance segmentation
- Automated image ingestion over GPS grids

## Limitations and next steps

- Migrate from TF 1.x to TF 2.x or PyTorch
- Package pipeline as installable module with CLI entry point
- Add Docker image with pinned CUDA and dependency stack
- Move large assets out of git history into object storage
