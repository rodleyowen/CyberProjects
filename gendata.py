import pandas as pan
import numpy as num
import streamlit as stl

# Create some dummy data for testing
data = pan.DataFrame( {
                                        'Incident_ID': range(1,101),
                                        'Risk_Level': num.random.choice(['Low', 'Medium', 'High', 'Extreme'], size=100, p=[0.1, 0.4, 0.3, 0.2]),
                                        'Attack_Type': num.random.choice(['Phishing', 'Malware', 'DDoS', 'Ransomware', 'Script Kiddy'], size=100),
                                        'Loss_Amount($)': num.random.randint(1000, 50000, size=100),
                                        'Date': pan.date_range('2024-01-01', periods=100, freq='D')
                                     })

stl.title('CyberSecurity Risk Dashboard')

# sidbar filters
risk_levels = data['Risk_Level'].unique()
selected_risk = stl.sidebar.selectbox('Select Risk Level', risk_levels)

attack_types = data['Attack_Type'].unique()
selected_attack = stl.sidebar.selectbox('Select Attack Type',  attack_types)

date_range = stl.sidebar.date_input('Select Date Range',[])

# filter data based on selections
filtered_data = data[(data['Risk_Level'] == selected_risk) & (data['Attack_Type'] == selected_attack)]

if date_range:
    start_date, end_date = date_range
    filtered_data = filtered_data[(filtered_data['Date'] >= pan.Timestamp(start_date)) &
                                                   (filtered_data['Date'] <= pan.Timestamp(end_date))]


#display the prepared data
stl.write(filtered_data)
