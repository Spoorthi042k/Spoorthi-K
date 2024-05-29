#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import pickle
import streamlit as st


# In[4]:


model=pickle.load(open('rf_model.pkl','rb'))


# In[11]:


st.title('Model Deployment using Random Forest')
st.sidebar.subheader('User Input Parameters')

st.write()


# In[14]:


import streamlit as st
import pandas as pd

def user_input_parameters():
    make = st.sidebar.text_input('Make')
    model = st.sidebar.text_input('Model')
    vehicle_class = st.sidebar.selectbox('Vehicle Class', ['Compact', 'SUV', 'Sedan', 'Truck', 'Van'])
    engine_size = st.sidebar.number_input('Engine Size (L)')
    cylinders = st.sidebar.slider('No. of Cylinders:',min_value=1,max_value=20,step=1)
    transmission = st.sidebar.selectbox('Transmission Type', ['Automatic', 'Manual','Automated Manual','Automatic Select Shift','Continuous Variable'])
    fuel_type = st.sidebar.selectbox('Fuel Type', ['Regular Gasoline', 'Premium Gasoline', 'Diesel','Ethanol','Natural Gas'])
    fuel_consumption_city = st.sidebar.number_input('Fuel consumption in city (L/100km)')
    fuel_consumption_hwy = st.sidebar.number_input('Fuel consumption in Highway (L/100km)')
    fuel_consumption_comb_l100km = st.sidebar.number_input('Fuel consumption combo (L/100km)')
    fuel_consumption_comb_mpg = st.sidebar.number_input('Fuel consumption combo (MPG)')
    st.sidebar.button("Submit")
    data = {
        'make': make,
        'model': model,
        'vehicle_class': vehicle_class,
        'engine_size': engine_size,
        'cylinders': cylinders,
        'transmission': transmission,
        'fuel_type': fuel_type,
        'fuel_consumption_city': fuel_consumption_city,
        'fuel_consumption_hwy': fuel_consumption_hwy,
        'fuel_consumption_comb(l100km)': fuel_consumption_comb_l100km,
        'fuel_consumption_comb(mpg)': fuel_consumption_comb_mpg
    }

    feature = pd.DataFrame(data, index=[0])
    return feature

df = user_input_parameters()
st.subheader('User Input Parameters')

def calculate_co2_emission(df):
    # Formula to calculate CO2 emission (assuming grams per kilometer)
    # Source: https://www.fueleconomy.gov/feg/Find.do?action=sbs&id=26821
    co2_emission = (df['fuel_consumption_comb(l100km)'] * 8887) / 1000  # Convert grams per mile to grams per kilometer
    df['CO2 Emission (g/km)'] = co2_emission
    return df

# Calculate CO2 emission
df = calculate_co2_emission(df)
output = st.write(df)

# In[15]:





# In[ ]:


  

