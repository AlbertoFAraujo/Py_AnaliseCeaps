import pandas as pd
import plotly.express as px
import streamlit as st
import analiseGeral
import analiseIndividual

df = pd.read_csv('Clean_despesas_CEASP.csv', sep=';')

st.sidebar.title('Menu')
pagina = st.sidebar.radio(
    'Selecione o tipo de análise:',
    ['Geral', 'Individual'])

if pagina == 'Geral':
    # Chama a função da página Geral
    analiseGeral.analise_geral()
elif pagina == 'Individual':
    # Chama a função da página Individual
    analiseIndividual.analise_individual()

frase = "<span style='font-size: 12px;'>Os dados podem ser consultados em: <a href='https://www12.senado.leg.br'>https://www12.senado.leg.br</a></span>"
st.markdown(frase, unsafe_allow_html=True)
