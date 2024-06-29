import streamlit as st

# Título do aplicativo
st.title('Calculadora de Preço Médio de Ações')

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

# Exibição do resultado
st.write(f'Você possui inicialmente {acoes_iniciais} ações com preço médio de R$ {preco_medio_inicial:.2f}')
st.write(f'O preço atual da ação é R$ {preco_atual:.2f}')
st.write(f'Se você comprar {novas_acoes} ações a R$ {preco_atual:.2f} cada, seu novo preço médio será aproximadamente R$ {preco_medio_novo:.2f}')

# Exibição das redes sociais com ícones
st.write('### Minhas Redes Sociais')
st.markdown('''
<a href="https://www.linkedin.com/in/tiago-holanda-082928141/" target="_blank">
    <img src="linkedin.png" alt="LinkedIn" style="width:50px;height:50px;">
</a>
<a href="https://github.com/Tiagofholanda" target="_blank">
    <img src="github.png" alt="GitHub" style="width:50px;height:50px;">
</a>
<a href="https://twitter.com/seu-usuario" target="_blank">
    <img src="twitter.png" alt="Twitter" style="width:50px;height:50px;">
</a>
''', unsafe_allow_html=True)