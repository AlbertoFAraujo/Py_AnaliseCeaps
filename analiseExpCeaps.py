from typing import List, Any

import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Clean_despesas_CEASP.csv', sep=';')

texto = """
<sup>**Cat01:** Aluguel de imóveis para escritório político, compreendendo despesas concernentes a eles;</sup>  
<sup>**Cat02:** Divulgação da atividade parlamentar;</sup>  
<sup>**Cat03:** Passagens aéreas, aquáticas e terrestres nacionais;</sup>  
<sup>**Cat04:** Contratação de consultorias, assessorias, pesquisas, trabalhos técnicos e outros serviços de 
apoio ao exercício do mandato parlamentar;</sup>  
<sup>**Cat05:** Locomoção, hospedagem, alimentação, combustíveis e lubrificantes;</sup>  
<sup>**Cat06:** Aquisição de material de consumo para uso no escritório político, 
inclusive aquisição ou locação de software, despesas postais, aquisição de publicações, locação de móveis e de 
equipamentos;</sup>  
<sup>**Cat07:** Serviços de Segurança Privada.</sup>
"""


# Análise Geral
def metrica_mesValor(mes, parametro):
    global result
    if mes != '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(df[df['Mes'] == mes].groupby('Dia')['Valor_reembolsado'].mean())
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(df[df['Mes'] == mes].groupby('Dia')['Valor_reembolsado'].sum())
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.line(result, eixo_x, eixo_y, title='Mês x Valor Total Gasto(R$)')
        fig.update_layout(
            dragmode=False,
            legend_title_text='Legenda:',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Mês: {}/2022'.format('0' + str(mes) if mes < 10 else mes),
            xaxis=dict(dtick='2', tickangle=0),
            yaxis_title='Valor Total (R$)',
            title={'x': 0.5},
            showlegend=False
        )
        fig.update_xaxes(range=['1', '31'])
        st.plotly_chart(fig, use_container_width=True)
    elif mes == '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(df.groupby('Mes')['Valor_reembolsado'].mean())
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(df.groupby('Mes')['Valor_reembolsado'].sum())
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.line(result, eixo_x, eixo_y, title='Mês x Valor Total Gasto(R$)')
        fig.update_layout(
            dragmode=False,
            legend_title_text='Legenda:',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Ano:2022',
            xaxis=dict(dtick='1', tickangle=0),
            yaxis_title='Valor Total (R$)',
            title={'x': 0.5},
            showlegend=False
        )
        fig.update_xaxes(range=['1', '12'])
        st.plotly_chart(fig, use_container_width=True)


def metrica_topSenador(mes, parametro):
    global result
    if mes != '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df[df['Mes'] == mes].groupby('Senador')['Valor_reembolsado'].mean().sort_values(ascending=False).head(
                    5))
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df[df['Mes'] == mes].groupby('Senador')['Valor_reembolsado'].sum().sort_values(ascending=False).head(
                    5))
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.bar(result, eixo_x, eixo_y, text_auto='.4s', title='Senador x Valor Médio Gasto(R$)')
        fig.update_layout(
            dragmode=False,
            legend_title_text='Legenda:',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Senador',
            yaxis_title='Valor Médio (R$)',
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    elif mes == '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(df.groupby('Senador')['Valor_reembolsado'].mean().sort_values(ascending=False).head(5))
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(df.groupby('Senador')['Valor_reembolsado'].sum().sort_values(ascending=False).head(5))
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.bar(result, eixo_x, eixo_y, text_auto='.4s', title='Senador x Valor Médio Gasto(R$)')
        fig.update_layout(
            dragmode=False,
            legend_title_text='Legenda:',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Senador',
            yaxis_title='Valor Médio (R$)',
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)



def metrica_topCategorias(mes, parametro):
    global result
    if mes != '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df[df['Mes'] == mes].groupby('categ_despesa')['Valor_reembolsado'].mean().sort_values(ascending=False))
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df[df['Mes'] == mes].groupby('categ_despesa')['Valor_reembolsado'].sum().sort_values(ascending=False))
        eixo_x = result['Valor_reembolsado']
        eixo_y = list(result.index)
        fig = px.funnel(result, eixo_x, eixo_y, title='Categoria Despesas x Valor Total Gasto(R$)')
        fig.update_layout(
            dragmode=False,
            xaxis_title='Categoria Despesas',
            yaxis_title='Valor Médio Gasto(R$)',
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        with st.expander("Legenda categorias"):
            st.markdown(texto, unsafe_allow_html=True)
    elif mes == '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df.groupby('categ_despesa')['Valor_reembolsado'].mean().sort_values(ascending=False))
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df.groupby('categ_despesa')['Valor_reembolsado'].sum().sort_values(ascending=False))
        eixo_x = result['Valor_reembolsado']
        eixo_y = list(result.index)
        fig = px.funnel(result, eixo_x, eixo_y, title='Categoria Despesas x Valor Total Gasto(R$)')
        fig.update_layout(
            dragmode=False,
            xaxis_title='Categoria Despesas',
            yaxis_title='Valor Médio Gasto(R$)',
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        with st.expander("Legenda categorias"):
            st.markdown(texto, unsafe_allow_html=True)



# Análise Individual
def metrica_SenadorMes(senador, mes, parametro):
    global result
    if mes != '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df[(df['Mes'] == mes) & (df['Senador'] == senador)].groupby('Dia')['Valor_reembolsado'].mean())
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df[(df['Mes'] == mes) & (df['Senador'] == senador)].groupby('Dia')['Valor_reembolsado'].sum())
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.line(result, eixo_x, eixo_y, title='{}(R$) x Mês - Senador(a): {}'.format(parametro, senador))
        fig.update_layout(
            legend_title_text='Legenda:',
            dragmode=False,
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Mês: {}/2022'.format('0' + str(mes) if mes < 10 else mes),
            xaxis=dict(dtick='2', tickangle=0),
            yaxis_title='{} (R$)'.format(parametro),
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    elif mes == '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df[df['Senador'] == senador].groupby('Mes')['Valor_reembolsado'].mean())
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df[df['Senador'] == senador].groupby('Mes')['Valor_reembolsado'].sum())
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.line(result, eixo_x, eixo_y, title='{}(R$) x Ano - Senador(a): {}'.format(parametro, senador))
        fig.update_layout(
            legend_title_text='Legenda:',
            dragmode=False,
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Ano: 2022',
            xaxis=dict(dtick='1', tickangle=0),
            yaxis_title='{} (R$)'.format(parametro),
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

def metrica_SenadorCat(senador, mes, parametro):
    global result
    if mes != '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df[(df['Mes'] == mes) & (df['Senador'] == senador)].groupby('categ_despesa')['Valor_reembolsado'].mean())
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df[(df['Mes'] == mes) & (df['Senador'] == senador)].groupby('categ_despesa')['Valor_reembolsado'].sum())
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.bar(result, eixo_x, eixo_y, text_auto='.4s', title='Categoria Despesas Mensal x {}(R$) - Senador(a): {}'.format(parametro, senador))
        fig.update_layout(
            legend_title_text='Legenda:',
            dragmode=False,
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Mês: {}/2022'.format('0' + str(mes) if mes < 10 else mes),
            xaxis=dict(dtick='1', tickangle=0),
            yaxis_title='{} (R$)'.format(parametro),
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    elif mes == '':
        if parametro == 'Média dos gastos':
            result = pd.DataFrame(
                df[df['Senador'] == senador].groupby('categ_despesa')['Valor_reembolsado'].mean())
        elif parametro == 'Total dos gastos':
            result = pd.DataFrame(
                df[df['Senador'] == senador].groupby('categ_despesa')['Valor_reembolsado'].sum())
        eixo_x = list(result.index)
        eixo_y = result['Valor_reembolsado']
        fig = px.bar(result, eixo_x, eixo_y, text_auto='.4s', title='Categoria Despesas Anual x {}(R$) - Senador(a): {}'.format(parametro, senador))
        fig.update_layout(
            dragmode=False,
            legend_title_text='Legenda:',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis_title='Ano: 2022',
            yaxis_title='{} (R$)'.format(parametro),
            title={'x': 0.5},
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    with st.expander("Legenda categorias"):
        st.markdown(texto, unsafe_allow_html=True)