

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Título da aplicação
st.title("Análise de Ações")

# Lista de códigos de ações (tickers) mais populares
tickers = ['PETR4.SA','BBAS3.SA','BRSR6.SA','BEES3.SA', 'BGIP4.SA', 'BNBR3.SA', 'BDORY', 'MGLU3.SA', 'MGLU3.BA', 'FB']

# Input para selecionar o código da ação
ticker = st.selectbox("Selecione o código da ação:", tickers)

# Input para selecionar as datas
dt_inicial = st.date_input("Selecione a data inicial:")
dt_final = st.date_input("Selecione a data final:")

# Busca os dados da ação
if ticker and dt_inicial and dt_final:
    dados = yf.Ticker(ticker)
    tabela = dados.history(start=dt_inicial, end=dt_final)

    # Exibe a tabela de preços de fechamento
    st.write(tabela[['Close']])

    # Gera um gráfico de linha dos preços de fechamento
    st.subheader(f"Gráfico de Preços de Fechamento - {ticker}")
    plt.figure(figsize=(10, 4))
    plt.plot(tabela['Close'])
    plt.title(f"Preço de Fechamento da Ação {ticker}")
    plt.xlabel("Data")
    plt.ylabel("Preço de Fechamento (USD)")
    plt.grid(True)

    # Exibe o gráfico no Streamlit
    st.pyplot(plt)
