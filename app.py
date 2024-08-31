import streamlit as st

# Função para gerar o link da imagem com base no índice
def get_image_url(index):
    return f"https://picsum.photos/800/600?{index}"

# Definindo o índice inicial
if 'index' not in st.session_state:
    st.session_state.index = 1

# Funções para avançar e voltar as imagens
def next_image():
    st.session_state.index += 1

def previous_image():
    if st.session_state.index > 1:
        st.session_state.index -= 1

# Centralizando o título usando HTML e CSS
st.markdown(
    """
    <h1 style="text-align: center;">Carrossel de Fotos</h1>
    """,
    unsafe_allow_html=True
)

# Exibindo a imagem centralizada
st.image(get_image_url(st.session_state.index), use_column_width=True)

# Dividindo os botões em duas colunas para centralização e controle
col1, col2 = st.columns([1, 1])

with col1:
    st.button("Voltar", on_click=previous_image)

with col2:
    st.button("Avançar", on_click=next_image)

# CSS para melhorar a aparência dos botões
st.markdown(
    """
    <style>
        .stButton > button {
            width: 100%;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True
)


