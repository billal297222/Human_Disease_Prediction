# 🧠 Human Disease Prediction using Symptoms

A web-based application that predicts the most probable human disease based on the symptoms provided by the user.  
Built with **Django** and trained on a custom healthcare dataset using multiple machine learning models.

---

## 🩺 Features

- 🤒 User can input symptoms via a web form  
- 📊 Machine learning models: Support Vector Machine (SVM), Random Forest (RF), K-Nearest Neighbors (KNN), Naive Bayes (NB), Decision Tree (DT)  
- 📁 CSV-based dataset for training  
- 📋 Final report displays:  
  - Predicted disease  
  - Description  
  - Precautionary advice  
- 🎨 Clean and responsive UI built with HTML & CSS  

---

## 🧪 Machine Learning Models

The following trained models are used for disease prediction:    
- Random Forest (RF)  
- Decision Tree (DT)  
- K-Nearest Neighbors (KNN)  
- Naive Bayes (NB)  

All models are stored as `.pkl` files in the `trained_models/` directory.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/DiseasePrediction.git
cd DiseasePrediction


## 🚀 Getting Started

### 1. Clone the repository

```bash
 ## 1.git clone https://github.com/your-username/DiseasePrediction.git
cd DiseasePrediction

## 2. Install dependencies

```bash
pip install -r requirements.txt

## 3. Run the project

```bash
python manage.py runserver

