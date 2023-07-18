import pandas as pd
import plotly.express as px
import streamlit as st
import analiseExpCeaps

meses = {'Anual': '', 'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6, 'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12}

# Página de análise geral
def analise_geral():
    st.title('Análise Geral')
    st.text('Nessa seção você encontra a análise geral dos indicadores de gastos dos Senadores\n'
            'no ano de 2022.')

    selec_mes = st.sidebar.selectbox('Selecione o mês:', list(meses))
    selec_parametro = st.sidebar.selectbox('Selecione o parâmetro:', ['Média dos gastos', 'Total dos gastos'])

    analiseExpCeaps.metrica_mesValor(meses[selec_mes], selec_parametro)
    analiseExpCeaps.metrica_topSenador(meses[selec_mes], selec_parametro)
    analiseExpCeaps.metrica_topCategorias(meses[selec_mes], selec_parametro)
