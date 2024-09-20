import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/alura-cursos/bibliotecas_visualizacao/main/Dados/imigrantes_canada.csv"

try:
    data = pd.read_csv(url)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()  # Stop execution if the data cannot be loaded

# Set up the Streamlit dashboard
st.title("Dashboard of Immigrants in Canada")

# Display the first few rows of the dataset
st.subheader("Dataset Overview")
st.write(data.head())

# Display some basic statistics
st.subheader("Basic Statistics")
st.write(data.describe())

# Create a pie chart of immigrants by country of origin
st.subheader("Immigrants by Country of Origin")
top_countries = data.groupby('Country')['Total'].sum().nlargest(10)

fig, ax = plt.subplots()
ax.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%')
ax.set_title('Top 10 Countries of Immigrants to Canada')
st.pyplot(fig)

# Run the Streamlit app
if __name__ == "__main__":
    st.run()