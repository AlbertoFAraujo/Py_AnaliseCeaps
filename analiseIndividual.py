import pandas as pd
import streamlit as st
import analiseExpCeaps

meses = {'Anual': '', 'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6, 'Julho': 7, 'Agosto': 8,
         'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12}


# Página de análise individual
def analise_individual():
    st.title('Análise Individual')
    st.text('Nessa seção você encontra a análise individual dos indicadores de gastos dos Senadores\n'
            'no ano de 2022.')

    # Lista com nome dos Senadores
    lista_senador = list(analiseExpCeaps.df['Senador'].unique())

    # Composição Sidebar
    selec_senador = st.sidebar.selectbox('Selecione o Senador:', lista_senador)
    selec_mes = st.sidebar.selectbox('Selecione o mês:', list(meses))
    selec_parametro = st.sidebar.selectbox('Selecione o parâmetro:', ['Média dos gastos', 'Total dos gastos'])

    # Chamada ao gráfico
    analiseExpCeaps.metrica_SenadorMes(selec_senador, meses[selec_mes], selec_parametro)
    analiseExpCeaps.metrica_SenadorCat(selec_senador, meses[selec_mes], selec_parametro)