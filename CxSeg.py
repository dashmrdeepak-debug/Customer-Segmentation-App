import streamlit as st
import numpy as np
import pickle

#Load Train Kmeans Model
kmeans=pickle.load(open("kmeans.pkl",'rb'))

def clustering(age,avg_spend,visit_per_week,promotion_interest):
    new_customer=np.array([[age,avg_spend,visit_per_week,promotion_interest]])
    predicted_cluster=kmeans.predict(new_customer)
    if predicted_cluster[0]==0:
        return "Daily"
    elif predicted_cluster[0]==1:
        return "weekend"
    else:
        return "Promotion"



#lets build app
st.title("customer Segmentation App ")
st.write("Enter Customer Details")

#row1
col1,col2=st.columns(2)

with col1:
   st.subheader("Customer Age")
   age=st.number_input('Age',min_value=18,max_value=100,value=40)
with col2:
   st.subheader("Average Spend in minute")
   avg_spend=st.number_input('Average Spend',min_value=0.0,max_value=1000.0,value=30.0)

col1,col2=st.columns(2)

with col1:
   st.subheader("Visits Per Week")
   visit_per_week=st.number_input('Visits Per Week',min_value=0,max_value=28,value=4)
with col2:
   st.subheader("Promotion Interest")
   promotion_interest=st.number_input('promotion interest',min_value=0.0,max_value=10.0,value=7.0)

if st.button("Predicted Cluster"):
   cluster_label=clustering(age,avg_spend,visit_per_week,promotion_interest)
   st.success(f'The customer belongs to the "{cluster_label}" cluster.')