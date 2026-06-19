import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Compras.csv', sep=';')

st.set_page_config(page_title='Dashboard - Vendas')

st.sidebar.header('Filtros')
st.title('Vendas Por Regiões')

st.write('Top 5 produtos mais vendidos')

top5_produtos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)
grafico1 = plt.figure(figsize=(10,5))
plt.barh(top5_produtos.index,top5_produtos.values)
plt.tight_layout()
st.pyplot(grafico1)