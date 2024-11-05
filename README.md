# logistic-regression
A repository for experimenting with linear regression and building a project based on it.

## About

This project focuses on building, experimenting with, and visualizing logistic regression models to predict survival outcomes on the Titanic dataset, available on Kaggle[https://www.kaggle.com/competitions/titanic]. Using GridSearchCV for model optimization, this project aims to achieve a performance score around 75% in the competition. The optimal model parameters are: 'C': 0.1, 'penalty': 'l1', and 'solver': 'liblinear'.

The user interface is built with **Streamlit** to provide a simple, interactive experience for selecting and comparing regression models.

## Features
1. Model Selection: Automatically tunes and selects the best logistic regression model through GridSearchCV.
2. Model Training: Trains the selected model on the Titanic dataset and displays performance metrics.
3. Prediction Visualization: Plots predictions and evaluates model performance.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python 3.x
- pip package manager

### Installation
1. Clone the repository: 
    ```bash
    git clone https://github.com/nageCasillas/logistic-regression.git
    cd logistic-regression
    ```
2. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
4. Open your browser and go to http://localhost:8501 to start interacting with the app.

## Usage
1. Model Training: Adjust parameters, if needed, and train the model on the dataset.
2. Results and Metrics: View results and performance metrics for the trained model, including accuracy, precision, and recall.

## Contribution
Contributions are welcome! If you would like to contribute, please:

1. Fork this repository.
2. Create a new branch (feature-branch-name).
3. Make changes and test them.
4. Create a pull request.


