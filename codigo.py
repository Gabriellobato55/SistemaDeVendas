#                       ========== PASSO A PASSO DO PROJETO ==========
#           PASSO 1: Criar a tela do sistema
#           PASSO 2: Criar o formulário de cadastro
#           PASSO 3: Salvar a venda na base de dados
#           PASSO 4: Mostrar a base de dados na tela
#           PASSO 5: Criar o dashboard com os gráficos

import streamlit as st
import pandas as pd
import plotly.express as px

# ========== Carregar a base de dados ===========
tabela_vendas = pd.read_csv("vendas.csv")
st.write("# SISTEMA DE VENDAS")


# ========== Seção de cadastro de vendas ==========
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone de Ouvido"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")

botao_cadastrar = st.sidebar.button("Cadastrar Venda")
# Lógica de cadastro através do botão:
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # 121 linhas
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada!")

# ========== Seção visualizar as vendas ==========
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


# ========== Seção dashboard ==========
st.write("## Dashboard")

#       Card/Métrica -> faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", faturamento)

#       Gráfico de Barra/Coluna -> Vendas por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

#       Gráfico de pizza -> Vendas por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)