import streamlit as st
import pandas as pd

# etapas:
# Passo 1 - Testar o conjunto de dados (dataset)
# Passo 2 - Criar os KPI's
#   Quais informações posso extrair do conjunto de dados
# Passo 3 - Desenvolver/programar os KPI's
#   Filtrar, agrupar, contar, calcular, etc...
# Passo 4 - Criar os gráficos, cards

df = pd.read_csv('Salaries.csv')

df = df.rename(columns={
    "Id": "Identificador",
    "EmployeeName": "NomeDoFuncionario",
    "JobTitle": "Cargo",
    "BasePay": "SalarioBase",
    "OvertimePay": "PagamentoHorasExtras",
    "OtherPay": "OutrosPagamentos",
    "Benefits": "Beneficios",
    "TotalPay": "PagamentoTotal",
    "TotalPayBenefits": "TotalPagamentoEBeneficios",
    "Year": "Ano",
    "Notes": "Notas",
    "Agency": "Agencia",
    "Status": "Status"
})

st.set_page_config(
    page_title='Dashboard de Vendas'
)
#------------------------------------------------- sidebar
st.sidebar.image('logo.png')
st.sidebar.title('Dashboard de Vendas')
st.sidebar.header('Filtros')
cargo = st.sidebar.selectbox(
    'Selecione o Cargo:',
    ['Todas'] + list(df['Cargo'].unique())
)
#------------------------------------------------ sidebar
st.title('Apresentando o RH da Prefeitura')

st.write('Dados')

st.dataframe(df[['Cargo','NomeDoFuncionario']])