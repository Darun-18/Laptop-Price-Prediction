## Laptop Price Prediction using Machine Learning

##  Overview

This project predicts the price of a laptop based on its specifications using Machine Learning. 
The model was trained on a Kaggle laptop dataset and deployed with Streamlit.

## Features

- Predict laptop prices instantly
- Interactive Streamlit web application
- Data preprocessing
- One-Hot Encoding for categorical features
- Random Forest Regressor model

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Dataset

- Source: Kaggle
- Records: 893
- Features: 18

## Model Performance

- Model: Random Forest Regressor
- R² Score: **0.81**
- Evaluation Metrics:
  - R² Score
  - MAE

## Application

The user selects laptop specifications such as:

- Brand
- Processor
- CPU
- RAM
- Storage
- GPU
- Display Size
- Operating System
- Warranty

The application predicts the estimated laptop price.

## How to Run

Clone the repository:

```bash
git clone https://github.com/Darun-18/Laptop-Price-Prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run web.py
```

## Project Structure

```
Laptop-Price-Prediction/
│
├── web.py
├── data.csv
├── laptop_price_model.pkl
├── features.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
```

## Author

**Darun**

GitHub: https://github.com/Darun-18
