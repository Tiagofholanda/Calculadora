import streamlit as st

# Título do aplicativo
st.title('Calculadora de Preço Médio de Ações')

# Função para alternar entre temas
def toggle_theme():
    if st.button('Alternar Tema'):
        current_theme = st.config.get_option('theme')
        new_theme = 'dark' if current_theme == 'light' else 'light'
        st.experimental_set_query_params(theme=new_theme)

# Botão para alternar tema
toggle_theme()

# Incluir logo do GitHub no canto superior esquerdo
st.image("https://github.com/Tiagofholanda/Calculadora/raw/main/imagem/logo.jpeg", width=150)

# Entrada de dados pelo usuário
acoes_iniciais = st.number_input('Número de ações iniciais', min_value=1, value=190)
preco_medio_inicial = st.number_input('Preço médio inicial (R$)', min_value=0.0, value=84.00, format="%.2f")
preco_atual = st.number_input('Preço atual da ação (R$)', min_value=0.0, value=70.00, format="%.2f")
novas_acoes = st.number_input('Número de novas ações a comprar', min_value=1, value=50)

# Cálculo do novo preço médio
valor_total_inicial = acoes_iniciais * preco_medio_inicial
valor_total_novas = novas_acoes * preco_atual

total_acoes = acoes_iniciais + novas_acoes
valor_total = valor_total_inicial + valor_total_novas

preco_medio_novo = valor_total / total_acoes

# Exibição do novo preço médio
st.write(f'O seu novo preço médio será aproximadamente **R$ {preco_medio_novo:.2f}**.')

# Exibição das redes sociais com logo do GitHub e imagem de perfil
st.write('### Minhas Redes Sociais')
st.markdown('''
<a href="https://www.linkedin.com/in/seu-perfil" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width:50px;height:50px;margin-right:10px;">
</a>
<a href="https://github.com/account" target="_blank">
    <img src="Octocat.png" alt="GitHub" style="width:50px;height:50px;margin-right:10px;">
</a>
<a href="https://twitter.com/seu-usuario" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" style="width:50px;height:50px;">
</a>
''', unsafe_allow_html=True)

# Incluir a imagem de perfil do Tiago Holanda
st.image("https://i1.rgstatic.net/ii/profile.image/11431281112306515-1673387103365_Q128/Tiago-Holanda.jpg", width=128, caption='Tiago Holanda')
