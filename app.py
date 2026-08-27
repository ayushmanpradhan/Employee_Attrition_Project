import streamlit as st
import pickle
import pandas as pd


# Load trained Logistic Regression model
with open('employee_attrition_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load StandardScaler
with open('scaler.pkl', 'rb') as file:
    sc = pickle.load(file)

# Load feature names
with open('feature_names.pkl', 'rb') as file:
    feature_names = pickle.load(file)


 
# Application title
st.title("Employee Attrition Prediction")

st.write(
    "Enter employee details below to predict whether the employee is likely to leave the organization."
)

st.divider()

st.subheader("Employee Information")

# Create two columns
col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

    business_travel = st.selectbox(
        "Business Travel",
        ["Non-Travel", "Travel_Rarely", "Travel_Frequently"]
    )

    daily_rate = st.number_input(
        "Daily Rate",
        min_value=100,
        value=800
    )

    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=30,
        value=5
    )

    department = st.selectbox(
        "Department",
        ["Human Resources", "Research & Development", "Sales"]
    )

    education_field = st.selectbox(
        "Education Field",
        [
            "Human Resources",
            "Life Sciences",
            "Marketing",
            "Medical",
            "Other",
            "Technical Degree"
        ]
    )

    job_role = st.selectbox(
        "Job Role",
        [
            "Healthcare Representative",
            "Human Resources",
            "Laboratory Technician",
            "Manager",
            "Manufacturing Director",
            "Research Director",
            "Research Scientist",
            "Sales Executive",
            "Sales Representative"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Divorced", "Married", "Single"]
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )


with col2:

    environment_satisfaction = st.selectbox(
        "Environment Satisfaction",
        [1, 2, 3, 4]
    )

    job_involvement = st.selectbox(
        "Job Involvement",
        [1, 2, 3, 4]
    )

    job_level = st.selectbox(
        "Job Level",
        [1, 2, 3, 4, 5]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [1, 2, 3, 4]
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        value=30000
    )

    stock_option_level = st.selectbox(
        "Stock Option Level",
        [0, 1, 2, 3]
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        value=5
    )

    training_times_last_year = st.number_input(
        "Training Times Last Year",
        min_value=0,
        max_value=6,
        value=2
    )

    work_life_balance = st.selectbox(
        "Work Life Balance",
        [1, 2, 3, 4]
    )

    years_at_company = st.number_input(
        "Years At Company",
        min_value=0,
        value=3
    )

    years_in_current_role = st.number_input(
        "Years In Current Role",
        min_value=0,
        value=2
    )

    years_with_curr_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        value=2
    )

# Encode Business Travel
if business_travel == "Non-Travel":
    business_travel_encoded = 0

elif business_travel == "Travel_Rarely":
    business_travel_encoded = 1

else:
    business_travel_encoded = 2



# Create input data for prediction
input_data = pd.DataFrame({
    'Age': [age],
    'BusinessTravel': [business_travel_encoded],
    'DailyRate': [daily_rate],
    'DistanceFromHome': [distance_from_home],
    'EnvironmentSatisfaction': [environment_satisfaction],
    'JobInvolvement': [job_involvement],
    'JobLevel': [job_level],
    'JobSatisfaction': [job_satisfaction],
    'MonthlyIncome': [monthly_income],
    'StockOptionLevel': [stock_option_level],
    'TotalWorkingYears': [total_working_years],
    'TrainingTimesLastYear': [training_times_last_year],
    'WorkLifeBalance': [work_life_balance],
    'YearsAtCompany': [years_at_company],
    'YearsInCurrentRole': [years_in_current_role],
    'YearsWithCurrManager': [years_with_curr_manager],

    'Department_Research & Development':
        [1 if department == "Research & Development" else 0],

    'Department_Sales':
        [1 if department == "Sales" else 0],

    'EducationField_Marketing':
        [1 if education_field == "Marketing" else 0],

    'EducationField_Technical Degree':
        [1 if education_field == "Technical Degree" else 0],

    'JobRole_Laboratory Technician':
        [1 if job_role == "Laboratory Technician" else 0],

    'JobRole_Manager':
        [1 if job_role == "Manager" else 0],

    'JobRole_Manufacturing Director':
        [1 if job_role == "Manufacturing Director" else 0],

    'JobRole_Research Director':
        [1 if job_role == "Research Director" else 0],

    'JobRole_Sales Representative':
        [1 if job_role == "Sales Representative" else 0],

    'MaritalStatus_Married':
        [1 if marital_status == "Married" else 0],

    'MaritalStatus_Single':
        [1 if marital_status == "Single" else 0],

    'OverTime_Yes':
        [1 if overtime == "Yes" else 0]
})


# Keep the same feature order used during model training
input_data = input_data[feature_names]


# Predict employee attrition
if st.button("Predict Attrition"):

    # Scale input data
    input_scaled = sc.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    # Display prediction result
    if prediction[0] == 1:
     st.error("⚠️ High Attrition Risk: Employee is likely to leave the organization.")
    else:
     st.success("✅ Low Attrition Risk: Employee is likely to stay with the organization.")

     