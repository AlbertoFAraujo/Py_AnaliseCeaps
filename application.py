import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Clean_despesas_CEASP.csv', sep=';')

meses_invertidos = {
    'Janeiro': 1,
    'Fevereiro': 2,
    'Março': 3,
    'Abril': 4,
    'Maio': 5,
    'Junho': 7,
    'Agosto': 6,
    'Julho': 8,
    'Setembro': 9,
    'Outubro': 10,
    'Novembro': 11,
    'Dezembro': 12
}

# Seleção dos meses

# Qual mês?
meses_lista = [mes for mes in meses_invertidos]

# Sidebar >>> Menu lateral
mes = st.sidebar.selectbox(
    'Escolha um mês de referência?',
    meses_lista)

st.write('Você selecionou:', mes)

# Filtragem dos meses e exibição do top 5 gastos por mês
valorMes = df.loc[df.Mes == meses_invertidos[mes],].groupby('Senador')['Valor_reembolsado'].sum().head(5).sort_values(ascending=False)

# Criando a plotagem e tipo de gráfico
fig02 = px.line(valorMes, title = 'Valor x Mês')

# Redefinindo alguns parâmetros
fig02.update_layout(
    xaxis_title = 'Mês: {}/2022'.format(meses_invertidos[mes]),
    yaxis_title = 'Valor Reembolsado (R$)',
    title = {'x':0.45} # Posição do título
)

st.title('ANÁLISE CEASP')
st.write('Essa aplicação apresenta uma análise de Cota para Exercício da Atividade Parlamentar dos Senadores')

# Plotagem no streamlit
st.plotly_chart(fig02, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com')
