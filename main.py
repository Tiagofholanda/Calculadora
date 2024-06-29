import streamlit as st
import requests

# Lista expandida de exemplos de códigos de ações, FIIs, BDRs e FII agros da bolsa brasileira
exemplo_acoes = [
    # Ações
    'PETR4.SAO', 'VALE3.SAO', 'BBDC4.SAO', 'ITUB4.SAO', 'B3SA3.SAO', 'ABEV3.SAO', 'ITSA4.SAO', 'BBAS3.SAO', 
    'BRFS3.SAO', 'JBSS3.SAO', 'LREN3.SAO', 'MGLU3.SAO', 'WEGE3.SAO', 'VVAR3.SAO', 'GGBR4.SAO', 'SUZB3.SAO', 
    'RADL3.SAO', 'RAIL3.SAO', 'NTCO3.SAO', 'HYPE3.SAO', 'YDUQ3.SAO', 'EQTL3.SAO', 'MRFG3.SAO', 'BRML3.SAO', 
    'MULT3.SAO', 'FLRY3.SAO', 'BTOW3.SAO', 'EGIE3.SAO', 'CSNA3.SAO', 'IGTA3.SAO', 'CPLE6.SAO', 'HGTX3.SAO', 
    'TOTS3.SAO', 'EVEN3.SAO', 'MRVE3.SAO', 'RENT3.SAO', 'QUAL3.SAO', 'CVCB3.SAO', 'IRBR3.SAO', 'BIDI4.SAO', 
    
    # FIIs
    'BRCR11.SAO', 'HGLG11.SAO', 'BCFF11.SAO', 'KNRI11.SAO', 'MXRF11.SAO', 'FIIB11.SAO', 'HGBS11.SAO', 
    'VRTA11.SAO', 'RBRP11.SAO', 'XPML11.SAO', 'HGRU11.SAO', 'VISC11.SAO', 'BTLG11.SAO', 'SDIL11.SAO', 
    'KNCR11.SAO', 'RBRR11.SAO', 'HFOF11.SAO', 'GGRC11.SAO', 'HGRU11.SAO', 'OUJP11.SAO', 'OUFF11.SAO', 
    'HGBS11.SAO', 'HGRE11.SAO', 'FIIB11.SAO', 'FIIP11B.SAO', 'FVPQ11.SAO', 'HCTR11.SAO', 'HLOG11.SAO', 
    'HOSI11.SAO', 'HSLG11.SAO', 'RBED11.SAO', 'RBRD11.SAO', 'XPCI11.SAO', 'XPLG11.SAO', 'XPML11.SAO',
    
    # BDRs
    'ITUB34.SAO', 'VALE5.SAO', 'NDAQ34.SAO', 'AAPL34.SAO', 'MSFT34.SAO', 'GOGL34.SAO', 'FBOK34.SAO',
    
    # FII Agros
    'AGRO3.SAO', 'SLCE3.SAO', 'SMTO3.SAO', 'SMLS3.SAO', 'AGXY3.SAO', 'BRML3.SAO'
]

# Função para buscar o preço atual da ação usando a API do Alpha Vantage
def get_current_price(symbol):
    try:
        # Chave da API do Alpha Vantage (substitua pela sua própria chave)
        api_key = 'SUA_CHAVE_API_AQUI'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if 'Global Quote' in data:
            global_quote = data['Global Quote']
            
            # Tentar acessar o preço de diferentes chaves
            if '05. price' in global_quote:
                current_price = float(global_quote['05. price'])
            elif '05. preco' in global_quote:
                current_price = float(global_quote['05. preco'])
            else:
                st.error(f"Não foi possível obter o preço para o símbolo {symbol}. Verifique o código e tente novamente.")
                return None
            
            return current_price
        else:
            st.error(f"Não foi possível obter o preço para o símbolo {symbol}. Verifique o código e tente novamente.")
            return None
    except Exception as e:
        st.error(f"Erro ao obter preço: {e}")
        return None

# Título do aplicativo
st.title('Calculadora de Preço Médio de Ações')

# Entrada de dados pelo usuário
st.sidebar.title('Configurações')
acoes_iniciais = st.sidebar.number_input('Número de ações iniciais', min_value=1, value=190)
preco_medio_inicial = st.sidebar.number_input('Preço médio inicial (R$)', min_value=0.0, value=84.00, format="%.2f")

# Entrada para digitar o preço atual da ação manualmente ou buscar automaticamente
st.sidebar.markdown('**Preço atual da ação:**')
option = st.sidebar.radio('', ['Digitar manualmente', 'Buscar automaticamente'])

if option == 'Digitar manualmente':
    preco_manual = st.sidebar.number_input('Digite o preço atual da ação (R$)', min_value=0.0, format="%.2f")
    codigo_ativo = st.sidebar.selectbox('Código da ação', exemplo_acoes, index=0)
else:
    codigo_ativo = st.sidebar.selectbox('Código da ação', exemplo_acoes, index=0)
    preco_manual = None

novas_acoes = st.sidebar.number_input('Número de novas ações a comprar', min_value=1, value=50)

# Botão para buscar o preço atual
if st.sidebar.button('Buscar preço atual'):
    if option == 'Buscar automaticamente':
        preco_atual = get_current_price(codigo_ativo)
        if preco_atual is not None:
            st.sidebar.write(f'O preço atual de {codigo_ativo} é R$ {preco_atual:.2f}')
        else:
            st.sidebar.warning('Digite um código válido para buscar o preço.')
    else:
        st.sidebar.write('Preço atual da ação inserido manualmente.')

# Cálculo do novo preço médio com base no preço atual (automático ou manual)
if 'preco_atual' in locals() or preco_manual is not None:
    if preco_manual is not None:
        preco_atual = preco_manual

    if preco_atual is not None:  # Verifica se o preço atual foi obtido com sucesso
        valor_total_inicial = acoes_iniciais * preco_medio_inicial
        valor_total_novas = novas_acoes * preco_atual
        total_acoes = acoes_iniciais + novas_acoes
        valor_total = valor_total_inicial + valor_total_novas
        preco_medio_novo = valor_total / total_acoes

        # Exibição do novo preço médio
        st.write(f'O seu novo preço médio será aproximadamente **R$ {preco_medio_novo:.2f}**.')
