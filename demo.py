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

# Create a filter for Region
selected_region = st.selectbox('Select Region:', df['Region'].unique())

# Filter the DataFrame based on the selected Region
filtered_df_region = df[df['Region'] == selected_region]

# Create a filter for State using the filtered DataFrame
selected_state = st.selectbox('Select State:', filtered_df_region['State'].unique())

# Filter the DataFrame based on the selected State
filtered_df = filtered_df_region[filtered_df_region['State'] == selected_state]

# Display the filtered DataFrame
if not filtered_df.empty:
    st.write("Filtered Result:")
    st.dataframe(filtered_df)
else:
    st.write("No results found for the selected filters.")

# Create a pie chart with the 'Category' column from the filtered DataFrame
try:
    category_counts = filtered_df['Category'].value_counts()
    fig = px.pie(values=category_counts.values, names=category_counts.index, title='Category Distribution')
    st.plotly_chart(fig)
except KeyError as e:
    st.error(f"Error: Column '{e}' not found in the DataFrame. Please check the column names.")
except Exception as e:
    st.error(f"An error occurred while creating the chart: {e}")
