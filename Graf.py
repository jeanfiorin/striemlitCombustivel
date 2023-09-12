import altair as alt
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")
# Função para ler o arquivo xlsx
@st.cache_data  # Use st.cache_data para dados que não mudam com o tempo
def ler_arquivo_xlsx():
    df = pd.read_excel(r"C:/Users/Clayton Medeiros/PycharmProjects/proj_preços_gas/preco_mensal_estados-desde_jan2013.xlsx")
    return df

# Ler o arquivo XLSX
df = ler_arquivo_xlsx()

colunas_interessantes = ['MÊS', 'PRODUTO', 'ESTADO', 'PREÇO MÉDIO REVENDA']

with st.sidebar:
    st.subheader('Agência Nacional do Petróleo Gás Natural e Biocombustíveis')
    logo_teste = Image.open('logo.png')  # Certifique-se de que 'logo.png' esteja no mesmo diretório
    st.image(logo_teste, use_column_width=True)
    st.subheader('Seleção de Filtros')
    fProduto = st.selectbox(
        "Selecione o Combustível:",
        options=df['PRODUTO'].unique()  # Correção em 'Produto' para 'PRODUTO'
    )
    fEstado = st.selectbox(
        "Selecione o Estado:",
        options= df['ESTADO'].unique()
    )

# Filtrar os dados com base nas seleções do usuário
dadosUsuario = df.loc[
    (df['PRODUTO'] == fProduto) &
    (df['ESTADO'] == fEstado)
]

# Atualizar o formato da coluna 'MÊS'
updateDatas = dadosUsuario['MÊS'].dt.strftime('%Y/%b')
dadosUsuario['MÊS'] = updateDatas

# Exibir os dados filtrados
st.header('PREÇO DO COMBUSTÍVEl EM TODO TERRITÓRIO NACIONAL')
st.markdown('**Combustível Selecionado:** '+ fProduto)
st.markdown('**Estado:** '+ fEstado)

grafCombEstado = alt.Chart(dadosUsuario).mark_line(
    point=alt.OverlayMarkDef(color='green', size=20)
).encode(
    x='MÊS:T',
    y='PREÇO MÉDIO REVENDA',
    strokeWidth=alt.value(3)
).properties(
    height = 500,
    width = 1000
)
st.altair_chart(grafCombEstado)





