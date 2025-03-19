import streamlit as st
import pandas as pd

# Replace 'Salidafinal.xlsx' with the actual file path if it's not in the current directory
try:
  df = pd.read_excel('Salidafinal.xlsx')
  st.dataframe(df) # Use st.dataframe to display the DataFrame in Streamlit
except FileNotFoundError:
  st.error("Error: 'Salidafinal.xlsx' not found. Please check the file path.")
except Exception as e:
  st.error(f"An error occurred: {e}")

# prompt: crear una grafica de las ventas por region del dataframe df usando streamlit

import plotly.express as px

# Assuming 'Region' and 'Sales' are column names in your DataFrame
try:
  fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región')
  st.plotly_chart(fig)
except KeyError as e:
  st.error(f"Error: Column '{e}' not found in the DataFrame. Please check the column names.")
except Exception as e:
  st.error(f"An error occurred while creating the chart: {e}")

# Create filters for Region and State
selected_region = st.selectbox('Select Region:', df['Region'].unique())
selected_state = st.selectbox('Select State:', df['State'].unique())

# Filter the DataFrame based on selected Region and State
filtered_df = df[(df['Region'] == selected_region) & (df['State'] == selected_state)]

# Display the filtered results
if not filtered_df.empty:
  st.write("Filtered Results:")
  st.dataframe(filtered_df)  # Display only the first row
else:
  st.write("No results found for the selected criteria.")
