import streamlit as st

# Título do aplicativo
st.title('Calculadora de Preço Médio de Ações')

# Entrada de dados pelo usuário
st.sidebar.title('Configurações')
acoes_iniciais = st.sidebar.number_input('Número de ações iniciais', min_value=1, value=190)
preco_medio_inicial = st.sidebar.number_input('Preço médio inicial ou atual (R$)', min_value=0.0, value=84.00, format="%.2f")
preco_atual = st.sidebar.number_input('Preço atual da ação (R$)', min_value=0.0, value=70.00, format="%.2f")
novas_acoes = st.sidebar.number_input('Número de novas ações a comprar', min_value=1, value=50)

# Cálculo do novo preço médio
valor_total_inicial = acoes_iniciais * preco_medio_inicial
valor_total_novas = novas_acoes * preco_atual
total_acoes = acoes_iniciais + novas_acoes
valor_total = valor_total_inicial + valor_total_novas
preco_medio_novo = valor_total / total_acoes

# Exibição do novo preço médio
st.write(f'O seu novo preço médio será aproximadamente **R$ {preco_medio_novo:.2f}**.')

# Adicionar gráfico se aplicável
# Exemplo de gráfico: evolução do preço médio ao longo do tempo
# import matplotlib.pyplot as plt
# plt.plot([0, 1, 2, 3, 4], [preco_medio_inicial, preco_medio_novo, preco_medio_novo, preco_medio_novo, preco_medio_novo])
# st.pyplot(plt)

# Exibição das redes sociais com ícones
st.sidebar.title('Redes Sociais e Contato')
st.sidebar.markdown('''
<a href="https://www.linkedin.com/in/seu-perfil" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width:50px;height:50px;margin-right:10px;">
</a>
<a href="https://github.com/Tiagofholanda" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111465.png" alt="GitHub" style="width:50px;height:50px;margin-right:10px;">
</a>
<a href="https://twitter.com/seu-usuario" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/145/145812.png" alt="Twitter" style="width:50px;height:50px;">
</a>
<a href="https://www.instagram.com/tiagofholanda?igsh=MXRlcTVmYWx1YjZleA%3D%3D&utm_source=qr" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" style="width:50px;height:50px;margin-right:10px;">
</a>
<a href="mailto:tfholanda@gmail.com" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email" style="width:50px;height:50px;">
</a>
''', unsafe_allow_html=True)
