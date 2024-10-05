import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

model = joblib.load('employee_promotion_payraise_model.pkl')


def load_unique_values(file_name):
    with open(file_name, 'r') as f:
        values = f.read().splitlines()
    return values


unique_departments = load_unique_values('unique_departments.txt')
unique_job_titles = load_unique_values('unique_job_titles.txt')


st.title("Employee Promotion and Pay Raise Prediction")


st.header("Enter Employee Details")


department = st.selectbox('Department Title', unique_departments)


job_title = st.selectbox('Job Title', unique_job_titles)


regular_pay = st.number_input('Regular Pay', min_value=0.0, value=50000.0)
overtime_pay = st.number_input('Overtime Pay', min_value=0.0, value=2000.0)


if st.button("Predict Promotion/Pay Raise"):
    
    department_encoded = unique_departments.index(department)
    job_title_encoded = unique_job_titles.index(job_title)

    employee_data = np.array([[department_encoded, job_title_encoded, regular_pay, overtime_pay]])

    
    prediction = model.predict(employee_data)

    
    if prediction[0] == 1:
        st.success("The employee is likely to receive a promotion or pay raise.")
    else:
        st.warning("The employee is not likely to receive a promotion or pay raise.")

    
    st.header("Pay Breakdown")

    
    pay_components = ['Regular Pay', 'Overtime Pay', 'Total Pay']
    pay_values = [regular_pay, overtime_pay, regular_pay + overtime_pay]

    fig, ax = plt.subplots()
    ax.bar(pay_components, pay_values)
    ax.set_ylabel('Amount in USD')
    ax.set_title('Pay Breakdown')

    
    st.pyplot(fig)


