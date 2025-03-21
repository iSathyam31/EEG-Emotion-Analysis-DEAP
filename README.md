# Emotion Classification Using DEAP Dataset

![GitHub](https://img.shields.io/badge/license-MIT-blue) ![GitHub](https://img.shields.io/badge/python-3.8%2B-green) ![GitHub](https://img.shields.io/badge/pytorch-1.10%2B-orange) ![GitHub](https://img.shields.io/badge/scikit--learn-1.0%2B-yellow)

This repository contains the implementation of an emotion classification pipeline using the DEAP (Database for Emotion Analysis using Physiological Signals) dataset. The project involves preprocessing EEG signals, extracting features, reducing dimensionality using PCA, and training machine learning and deep learning models for emotion classification.

---

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Pipeline Overview](#pipeline-overview)
- [Features](#features)
- [Models](#models)
- [Results](#results)
- [Installation](#installation)
- [License](#license)

---

## Introduction
Emotion classification is a critical task in affective computing, with applications in healthcare, human-computer interaction, and entertainment. This project leverages the DEAP dataset, which contains EEG signals from 32 participants watching 40 music videos. The goal is to classify emotions based on valence and arousal scores using machine learning and deep learning techniques.

---

## Dataset
The DEAP dataset consists of:
- **32 EEG channels** (sampled at 128 Hz).
- **40 trials** per participant (1-minute music videos).
- Self-reported emotional ratings for **valence**, **arousal**, **dominance**, and **liking**.

For more details, visit the [DEAP Dataset Website](http://www.eecs.qmul.ac.uk/mmv/datasets/deap/).

---

## Pipeline Overview
The emotion classification pipeline consists of the following steps:
1. **Preprocessing**: Standardize and clean EEG signals.
2. **Feature Extraction**: Extract time-domain, frequency-domain, and wavelet-based features.
3. **Dimensionality Reduction**: Apply PCA to reduce features to 20 components.
4. **Model Training**: Train machine learning (SVM, Random Forest, etc.) and deep learning (Neural Network) models.
5. **Evaluation**: Evaluate models using precision, recall, F1 score, and accuracy.

---

## Features
### Time-Domain Features
- Mean, Standard Deviation, Skewness, Kurtosis, etc.
- First and second derivatives.
- Hjorth parameters (Activity, Mobility, Complexity).

### Frequency-Domain Features
- Power Spectral Density (PSD).
- Bandpower for Delta, Theta, Alpha, Beta, and Gamma bands.
- Wavelet coefficients and entropy-based features.

### Region-Averaged Features
- Features are averaged across 5 brain regions: Frontal, Central, Temporal, Parietal, and Occipital.

---

## Models
The following models were implemented and evaluated:
1. **Machine Learning Models**:
   - Support Vector Machine (SVM)
   - Random Forest
   - Decision Tree
   - XGBoost
   - Gradient Boosting

2. **Deep Learning Model**:
   - Neural Network (PyTorch) with hyperparameter tuning using Optuna.

---

## Results
The Neural Network achieved the best performance with the following metrics:

| Model            | Accuracy | Precision | Recall  | F1-Score  |
|------------------|----------|-----------|---------|-----------|
| SVM              | 0.8000   | 0.7972    | 0.8000  | 0.7972    |
| Random Forest    | 0.6750   | 0.6740    | 0.6750  | 0.6706    |
| Decision Tree    | 0.4964   | 0.4970    | 0.4964  | 0.4965    |
| XGBoost          | 0.6964   | 0.6965    | 0.6964  | 0.6965    |
| Gradient Boosting| 0.7286   | 0.7290    | 0.7286  | 0.7287    |
| **Neural Network** | **0.8500** | **0.8496** | **0.8500** | **0.8492** |
---

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/EmoClassify-DEAP.git
   cd EmoClassify-DEAP
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the DEAP dataset from the official website and place it in the 'data/' directory.   


## LICENSE
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
* The DEAP dataset creators for providing the dataset.
* The open-source community for libraries like PyTorch, scikit-learn, and Optuna.