
import numpy as np
import pickle
import streamlit as st

# Load the trained SVM modelC:\Users\user\Desktop\webb
loadedModel = pickle.load(open('SVM_customers_prediction.sav', 'rb'))

def customers_predictions(input_data):
    # Convert input data to numpy array and reshape for prediction
    data_as_array = np.array(input_data).reshape(1, -1)
    # Make prediction
    prediction = loadedModel.predict(data_as_array)
    st.success(prediction)
    # Return prediction result
    if prediction == 0:
        return 'The client is likely to leave !!!'
    else:
        return 'The client is likely to stay !!!'

def main():
    st.title('Customer Attrition Prediction')

    # Define custom mappings
    education_map = {'Uneducated': 0, 'High School': 1, 'College': 2, 'Graduate': 3, 'Post-Graduate': 4, 'Doctorate': 5, 'Unknown': -1}
    gender_map = {'M': 1, 'F': 0}
    income_map = {'Less than $40K': 0, '$40K - $60K': 1, '$60K - $80K': 2, '$80K - $120K': 3, '$120K +': 4, 'Unknown': -1}
    martal_s_map = {'Single': 0, 'Married': 1, 'Divorced': 2, 'Unknown': -1}
    card_c_map = {'Blue': 0, 'Gold': 1, 'Silver': 2, 'Platinum': 4}

    # Numerical inputs
    Customer_Age = st.number_input('Customer Age', min_value=0, max_value=100, step=1)
    Gender = st.selectbox('Gender', options=list(gender_map.keys()))
    Dependent_count = st.number_input('Dependent Count', min_value=0, step=1)
    Education_Level = st.selectbox('Education Level', options=list(education_map.keys()))
    Marital_Status = st.selectbox('Marital Status', options=list(martal_s_map.keys()))
    Income_Category = st.selectbox('Income Category', options=list(income_map.keys()))
    Card_Category = st.selectbox('Card Category', options=list(card_c_map.keys()))
    Months_on_book = st.number_input('Months on Book', min_value=0, step=1)
    Total_Relationship_Count = st.number_input('Total Relationship Count', min_value=0, step=1)
    Months_Inactive_12_mon = st.number_input('Months Inactive (12 months)', min_value=0, step=1)
    Contacts_Count_12_mon = st.number_input('Contacts Count (12 months)', min_value=0, step=1)
    Credit_Limit = st.number_input('Credit Limit', min_value=0.0, step=0.01)
    Total_Revolving_Bal = st.number_input('Total Revolving Balance', min_value=0.0, step=0.01)
    Avg_Open_To_Buy = st.number_input('Average Open to Buy', min_value=0.0, step=0.01)
    Total_Amt_Chng_Q4_Q1 = st.number_input('Total Amount Change (Q4 to Q1)', step=0.01)
    Total_Trans_Amt = st.number_input('Total Transaction Amount', min_value=0.0, step=0.01)
    Total_Trans_Ct = st.number_input('Total Transaction Count', min_value=0, step=1)
    Total_Ct_Chng_Q4_Q1 = st.number_input('Total Count Change (Q4 to Q1)', step=0.01)
    Avg_Utilization_Ratio = st.number_input('Average Utilization Ratio', min_value=0.0, max_value=1.0, step=0.01)

    # Map selected categorical values to their numerical equivalents
    Gender_value = gender_map[Gender]
    Education_Level_value = education_map[Education_Level]
    Marital_Status_value = martal_s_map[Marital_Status]
    Income_Category_value = income_map[Income_Category]
    Card_Category_value = card_c_map[Card_Category]

    # Initialize customer_status
    customer_status = ''

    # Create button for prediction
    if st.button('Predict Client Status'):
        # Create input array with mapped values
        input_data = [
            Customer_Age,
            Gender_value,
            Dependent_count,
            Education_Level_value,
            Marital_Status_value,
            Income_Category_value,
            Card_Category_value,
            Months_on_book,
            Total_Relationship_Count,
            Months_Inactive_12_mon,
            Contacts_Count_12_mon,
            Credit_Limit,
            Total_Revolving_Bal,
            Avg_Open_To_Buy,
            Total_Amt_Chng_Q4_Q1,
            Total_Trans_Amt,
            Total_Trans_Ct,
            Total_Ct_Chng_Q4_Q1,
            Avg_Utilization_Ratio
        ]
        # Get prediction
        customer_status = customers_predictions(input_data)
        st.success(customer_status)

if __name__ == '__main__':

    main()
