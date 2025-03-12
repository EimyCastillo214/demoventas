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

# prompt: crear una grafica de las ventas por region del dataframe df

import matplotlib.pyplot as plt

# prompt: Leer archivo Salidafinal.xlsx

import pandas as pd

# Assuming 'Region' and 'Sales' are column names in your DataFrame
try:
    sales_by_region = df.groupby('Region')['Sales'].sum()
    plt.figure(figsize=(10, 6))  # Adjust figure size as needed
    plt.bar(sales_by_region.index, sales_by_region.values)
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.title('Sales by Region')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    st.pyplot(plt)  # Display the plot in Streamlit
except KeyError:
    st.error("Error: 'Region' or 'Sales' column not found in the DataFrame.")
except Exception as e:
    st.error(f"An error occurred while creating the plot: {e}")
