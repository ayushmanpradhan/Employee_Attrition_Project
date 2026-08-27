# Employee Attrition Prediction

A machine learning web application that predicts whether an employee is likely to leave an organization based on employee-related factors such as age, income, job satisfaction, work-life balance, overtime, job role, and years at the company.

The project covers the complete machine learning workflow, including data preprocessing, feature selection, model training, model evaluation, and deployment using Streamlit.

## Live Application

The deployed application is available here:

https://empl-attrition-prediction.streamlit.app

## Project Objective

The objective of this project is to build a machine learning model that can predict whether an employee is likely to leave the organization.

Employee attrition can affect an organization's productivity, recruitment costs, and workforce stability. This project uses employee-related information to identify employees who may be at risk of leaving.

## Dataset Information

The project uses the IBM HR Analytics Employee Attrition dataset.

The dataset contains approximately **1,470 employee records** with information related to:

- Age
- Business Travel
- Department
- Distance From Home
- Job Role
- Job Satisfaction
- Monthly Income
- OverTime
- Total Working Years
- Work Life Balance
- Years At Company
- Other employee-related attributes

The target variable is **Attrition**, which indicates whether an employee left the organization.

- `No` → Employee stayed
- `Yes` → Employee left

## Project Workflow

The project follows the complete machine learning workflow:

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Categorical Data Encoding
6. Feature Selection using `f_classif`
7. Train-Test Split
8. Feature Scaling using StandardScaler
9. Logistic Regression Model
10. Support Vector Classifier (SVC)
11. Model Evaluation
12. Model Comparison
13. Final Model Selection
14. Model Saving using Pickle
15. Streamlit Web Application
16. Deployment using Streamlit Community Cloud

## Machine Learning Models

Two classification algorithms were trained and evaluated in this project:

### Logistic Regression

Logistic Regression was used as the first classification model for predicting employee attrition.

### Support Vector Classifier (SVC)

Support Vector Classifier was also trained to compare its performance with Logistic Regression.

## Model Performance

| Model | Training Accuracy | Testing Accuracy | Attrition Precision | Attrition Recall | Attrition F1-Score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 87.93% | 89.12% | 0.65 | 0.38 | 0.48 |
| SVC | 90.14% | 88.78% | 0.71 | 0.26 | 0.38 |

The Logistic Regression model achieved an **AUC score of approximately 0.77**.

Although both models achieved similar overall accuracy, Logistic Regression provided better recall and F1-score for the attrition class. Therefore, **Logistic Regression was selected as the final model for deployment**.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Pickle
- Google Colab
- VS Code
- Git & GitHub

## Project Structure

Employee_Attrition_Project/

- `app.py` - Streamlit web application
- `employee_attrition_model.pkl` - Trained Logistic Regression model
- `scaler.pkl` - Fitted StandardScaler
- `feature_names.pkl` - Selected feature names used by the model
- `requirements.txt` - Required Python libraries
- `README.md` - Project documentation

## How to Run the Project Locally

1. Clone or download the GitHub repository.

2. Install the required libraries:

   `pip install -r requirements.txt`

3. Run the Streamlit application:

   `python -m streamlit run app.py`

4. Open the local Streamlit URL in your browser.

5. Enter the employee details and click **Predict Attrition** to get the prediction.

## Deployment

The trained Logistic Regression model and StandardScaler were saved using Pickle and integrated with a Streamlit web application.

The application was deployed using **Streamlit Community Cloud** through the GitHub repository.

### Live App

https://empl-attrition-prediction.streamlit.app

## Conclusion

This project demonstrates an end-to-end machine learning workflow for employee attrition prediction.

Logistic Regression and SVC were compared, and Logistic Regression was selected as the final model because it provided better testing accuracy, recall, and F1-score for the attrition class.

The final model was integrated into an interactive Streamlit application and deployed online for real-time predictions.

