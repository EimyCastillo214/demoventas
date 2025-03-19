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

# Crear un filtro de selección múltiple para la columna 'Region'
regiones = df['Region'].unique()
regiones_seleccionadas = st.multiselect('Selecciona una o más regiones', regiones)

# Filtrar el dataframe basado en las regiones seleccionadas
if regiones_seleccionadas:
    df_filtrado = df[df['Region'].isin(regiones_seleccionadas)]
else:
    df_filtrado = df

# Mostrar el dataframe filtrado
st.write('DataFrame Filtrado:')
st.dataframe(df_filtrado)
