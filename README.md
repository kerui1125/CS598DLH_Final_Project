# Reproducing and Validating Fair Conformal Predictors for Applications in Medical Imaging

This repository is the implementation of CS598DLH_Final_Project: Reproducing and Validating Fair Conformal Predictors for Applications in Medical Imaging

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## Dataset
The model is trained on IS-IC skin dataset: https://www.isic-archive.com/#!/topWithHeader/wideContentTop/main

## Training

To train the model(s) in the paper, run this command (The parameters are baked in at train.py):

```train
python src/train.py
```
To change the parameters(seed, epoch, monte carlo dropout), image folder, metadata csv and labels, please override the argparse objects at the main method of train.py\
See the training result in the root directory with name similar to run_2023_month_day_hour_minute

## Evaluation

Validation and Testings for Resnet model are included in train process\
Conformal prediction results are plotted in the jupyter notebook


## Results

Conformal prediction methods were applid in the notebook repro.ipynb. The diagrams are also included.
To run the jupyter notebook below, please make sure to have below ready:
  1. A kernal with all requirements installed
  2. A trained model from train.py

>📋  https://github.com/kerui1125/CS598DLH_Final_Project/blob/main/repro.ipynb
