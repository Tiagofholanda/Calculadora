import streamlit as st
import requests

exemplo_acoes = [
    # Ações
    'ABEV3.SAO', 'ASAI3.SAO', 'AZUL4.SAO', 'BTOW3.SAO', 'B3SA3.SAO',
    'BBSE3.SAO', 'BRML3.SAO', 'BBDC3.SAO', 'BBDC4.SAO', 'BRAP4.SAO',
    'BBAS3.SAO', 'BRKM5.SAO', 'BRFS3.SAO', 'BPAC11.SAO', 'CRFB3.SAO',
    'CCRO3.SAO', 'CMIG4.SAO', 'HGTX3.SAO', 'CIEL3.SAO', 'COGN3.SAO',
    'CPLE6.SAO', 'CSAN3.SAO', 'CPFE3.SAO', 'CVCB3.SAO', 'CYRE3.SAO',
    'ECOR3.SAO', 'ELET3.SAO', 'ELET6.SAO', 'EMBR3.SAO', 'ENBR3.SAO',
    'ENGI11.SAO', 'ENEV3.SAO', 'EGIE3.SAO', 'EQTL3.SAO', 'EZTC3.SAO',
    'FLRY3.SAO', 'GGBR4.SAO', 'GOLL4.SAO', 'NTCO3.SAO', 'HAPV3.SAO',
    'HYPE3.SAO', 'IGTA3.SAO', 'GNDI3.SAO', 'ITSA4.SAO', 'ITUB4.SAO',
    'JBSS3.SAO', 'JHSF3.SAO', 'KLBN11.SAO', 'RENT3.SAO', 'LCAM3.SAO',
    'LAME4.SAO', 'LREN3.SAO', 'MGLU3.SAO', 'MRFG3.SAO', 'BEEF3.SAO',
    'MRVE3.SAO', 'MULT3.SAO', 'PCAR3.SAO', 'PETR3.SAO', 'PETR4.SAO',
    'BRDT3.SAO', 'PRIO3.SAO', 'QUAL3.SAO', 'RADL3.SAO', 'RAIL3.SAO',
    'SBSP3.SAO', 'SANB11.SAO', 'CSNA3.SAO', 'SULA11.SAO', 'SUZB3.SAO',
    'TAEE11.SAO', 'TIET11.SAO', 'UGPA3.SAO', 'USIM5.SAO', 'VALE3.SAO',
    'VIVT3.SAO', 'VVAR3.SAO', 'WEGE3.SAO', 'YDUQ3.SAO', 'ALPA4.SAO',
    'ALUP11.SAO', 'ALUP3.SAO', 'ALUP4.SAO', 'APER3.SAO', 'ARZZ3.SAO',
    'ATOM3.SAO', 'BAHI3.SAO', 'BALM4.SAO', 'BBDC3F.SAO', 'BBDC4F.SAO',
    'BIDI3.SAO', 'BIDI4.SAO', 'BKBR3.SAO', 'BRDT3F.SAO', 'BRGE11.SAO',
    'BRGE12.SAO', 'BRIV3.SAO', 'BRSR6.SAO', 'BSEV3.SAO', 'BTOW3F.SAO',
    'CARD3.SAO', 'CCRO3F.SAO', 'CESP6.SAO', 'CIEL3F.SAO', 'CMIG3.SAO',
    'CMIG3F.SAO', 'COGN3F.SAO', 'CPFE3F.SAO', 'CRDE3.SAO', 'CVCB3F.SAO',
    'CYRE3F.SAO', 'DIRR3.SAO', 'DMMO11.SAO', 'DOHL4.SAO', 'EALT4.SAO',
    'ECOR3F.SAO', 'EGIE3F.SAO', 'EKTR4.SAO', 'ELET3F.SAO', 'ELET6F.SAO',
    'EMAE4.SAO', 'EMBR3F.SAO', 'ENBR3F.SAO', 'ENEV3F.SAO', 'ENGI11F.SAO',
    'EQTL3F.SAO', 'EZTC3F.SAO', 'FESA4.SAO', 'FESA4F.SAO', 'FLRY3F.SAO',
    'GGBR3.SAO', 'GGBR3F.SAO', 'GOAU3.SAO', 'GOAU3F.SAO', 'GOLL4F.SAO',
    'HAPV3F.SAO', 'HYPE3F.SAO', 'IGTA3F.SAO', 'IRBR3.SAO', 'IRBR3F.SAO',
    'ITSA3.SAO', 'ITSA4F.SAO', 'ITUB3.SAO', 'ITUB3F.SAO', 'JBSS3F.SAO',
    'JHSF3F.SAO', 'JPSA3.SAO', 'KEPL3.SAO', 'KLBN11F.SAO', 'LAME3.SAO',
    'LAME3F.SAO', 'LAVV3.SAO', 'LCAM3F.SAO', 'LIGT3.SAO', 'LIGT3F.SAO',
    'LINX3.SAO', 'LJQQ3.SAO', 'LOGG3.SAO', 'LOGG3F.SAO', 'LUPA3.SAO',
    'LUPA3F.SAO', 'LWSA3.SAO', 'MDIA3.SAO', 'MDIA3F.SAO', 'MGLU3F.SAO',
    'MOAR3.SAO', 'MOAR3F.SAO', 'MRFG3F.SAO', 'MRVE3F.SAO', 'MYPK3.SAO',
    'NEOE3.SAO', 'NEOE3F.SAO', 'NTCO3F.SAO', 'ODPV3.SAO', 'OMGE3.SAO',
    'PARD3.SAO', 'PCAR3F.SAO', 'PETR3F.SAO', 'PETR4F.SAO', 'PFRM3.SAO',
    'PINE4.SAO', 'PLAS3.SAO', 'PLPL3.SAO', 'POMO4.SAO', 'POMO4F.SAO',
    'POSI3.SAO', 'PSSA3.SAO', 'PSSA3F.SAO', 'PTBL3.SAO', 'PTBL3F.SAO',
    'QUAL3F.SAO', 'RADL3F.SAO', 'RAIL3F.SAO', 'RAPT3.SAO', 'RAPT4.SAO',
    'RDNI3.SAO', 'RNEW11.SAO', 'RNEW3.SAO', 'RNEW4.SAO', 'RPMG3.SAO',
    'SAPR11.SAO', 'SAPR3.SAO', 'SAPR4.SAO', 'SBFG3.SAO', 'SBFG3F.SAO',
    'SMLS3.SAO', 'SMLS3F.SAO', 'SMTO3.SAO', 'SMTO3F.SAO', 'SULA11F.SAO',
    'SUZB3F.SAO', 'TAEE11F.SAO', 'TIET11F.SAO', 'TOTS3.SAO', 'TOTS3F.SAO',
    'TRIS3.SAO', 'TRIS3F.SAO', 'TRPL3.SAO', 'TRPL4.SAO', 'TUPY3.SAO',
    'UGPA3F.SAO', 'UNIP3.SAO', 'UNIP3F.SAO', 'UNIP6.SAO', 'UNIP6F.SAO',
    'USIM5F.SAO', 'VALE3F.SAO', 'VIVT3F.SAO', 'VULC3.SAO', 'VVAR3F.SAO',
    'WEGE3F.SAO', 'WHRL3.SAO', 'WHRL4.SAO', 'WIZS3.SAO', 'WSON33.SAO',
    'YDUQ3F.SAO' 
    
    # FIIs
    'ABCP11.SAO', 'AEFI11.SAO', 'AFCR11.SAO', 'AGCX11.SAO', 'AIEC11.SAO',
    'ALMI11.SAO', 'ALZR11.SAO', 'ARFI11B.SAO', 'ATSA11.SAO', 'AURB11.SAO',
    'AVFF11.SAO', 'AVIN11.SAO', 'BBFI11B.SAO', 'BBPO11.SAO', 'BCFF11B.SAO',
    'BCIA11.SAO', 'BFIG11.SAO', 'BHYG11.SAO', 'BLCP11.SAO', 'BMII11.SAO',
    'BNFS11.SAO', 'BRCR11.SAO', 'BPFF11.SAO', 'BPML11.SAO', 'BPRP11.SAO',
    'BRCO11.SAO', 'CARE11.SAO', 'CPTS11B.SAO', 'CRFF11.SAO', 'CVBI11.SAO',
    'DIFI11.SAO', 'DRIT11B.SAO', 'EDFO11B.SAO', 'EURO11.SAO', 'FAED11.SAO',
    'FAMB11B.SAO', 'FEXC11.SAO', 'FLMA11.SAO', 'FLRP11.SAO', 'FOFT11.SAO',
    'FPAB11.SAO', 'FVPQ11.SAO', 'FVPQ11.SAO', 'GBFF11.SAO', 'GGRC11.SAO',
    'GRLV11.SAO', 'GTWR11.SAO', 'HABT11.SAO', 'HAGA11.SAO', 'HCTR11.SAO',
    'HFOF11.SAO', 'HGBS11.SAO', 'HGFF11.SAO', 'HGLG11.SAO', 'HGRE11.SAO',
    'HGPO11.SAO', 'HGRU11.SAO', 'HLOG11.SAO', 'HLSA11.SAO', 'HOSI11.SAO',
    'HPDP11.SAO', 'HREC11.SAO', 'HTMX11.SAO', 'IRDM11.SAO', 'JSRE11.SAO',
    'JRDM11.SAO', 'KNCR11.SAO', 'KNIP11.SAO', 'KNRE11.SAO', 'KNSC11.SAO',
    'LASC11.SAO', 'LAVI11.SAO', 'LVBI11.SAO', 'MALL11.SAO', 'MCCI11.SAO',
    'MFII11.SAO', 'MXRF11.SAO', 'NCHB11.SAO', 'NSLU11.SAO', 'NVHO11.SAO',
    'ONEF11.SAO', 'OUJP11.SAO', 'OUJP11B.SAO', 'PABY11.SAO', 'PBLV11.SAO',
    'PATC11.SAO', 'PORD11.SAO', 'PRSV11.SAO', 'PVBI11.SAO', 'PVBI11B.SAO',
    'RBBV11.SAO', 'RBCB11.SAO', 'RBED11.SAO', 'RBRP11.SAO', 'RBRR11.SAO',
    'RBRF11.SAO', 'RCRB11.SAO', 'RDPD11.SAO', 'RECT11.SAO', 'RECR11.SAO',
    'REIT11.SAO', 'RBRR11.SAO', 'RDPD11.SAO', 'RECT11.SAO', 'RECR11.SAO',
    'REIT11.SAO', 'RFOF11.SAO', 'RNGO11.SAO', 'RPAD11.SAO', 'RSPD11.SAO',
    'SADI11.SAO', 'SAIC11.SAO', 'SARE11.SAO', 'SHPH11.SAO', 'SHOP11.SAO',
    'SPAF11.SAO', 'TBOF11.SAO', 'TORD11.SAO', 'TRXF11.SAO', 'UBSR11.SAO',
    'VCJR11.SAO', 'VILG11B.SAO', 'VINO11.SAO', 'VISC11.SAO', 'VRTA11.SAO',
    'WPLZ11.SAO', 'XPCI11.SAO', 'XPHT11.SAO', 'XPLG11.SAO', 'XPPR11.SAO',
    'XPSF11.SAO', 'XTED11.SAO', 'YCHY11.SAO', 'AGRO11.SAO', 'SLCE3.SAO', 
    'SMTO3.SAO', 'SMLS3.SAO', 'AGXY3.SAO',
    'BRML3.SAO', 'CNES11.SAO', 'FEXC11.SAO', 'HGCR11.SAO', 'FDMC11.SAO',
    'HTMX11.SAO', 'CTXT11.SAO', 'HTAG11.SAO', 'RBED11.SAO', 'HFOF11.SAO',
    'HABT11.SAO', 'MALL11.SAO', 'RBRP11.SAO', 'RBVA11.SAO', 'TRNT11.SAO',
    'XPLG11.SAO', 'CPTS11.SAO', 'HGLG11.SAO', 'HGRU11.SAO', 'HSML11.SAO',
    'JRDM11.SAO', 'KNRI11.SAO', 'LVBI11.SAO', 'MXRF11.SAO', 'OUCY11.SAO',
    'PQDP11.SAO', 'RECT11.SAO', 'SAAG11.SAO', 'SDIL11.SAO', 'SPTW11.SAO',
    'SUNO11.SAO', 'VINO11.SAO', 'VRTA11.SAO'
    
    # BDRs
    'AAPL34.SAO', 'ABEV34.SAO', 'ADRs.ISA', 'AMD34.SAO', 'AMZO34.SAO',
    'ARZNY.ISA', 'AURA33.SAO', 'BAESY.ISA', 'BBAJ34.SAO', 'BIDU34.SAO',
    'BIIB34.SAO', 'BPAC34.SAO', 'BRDT3.SAO', 'BRFS3.SAO', 'BRKM5.SAO',
    'BRML3.SAO', 'BTOW3.SAO', 'CARR34.SAO', 'CCRO3.SAO', 'CIPL34.SAO',
    'CMCSA34.SAO', 'COCA34.SAO', 'COGN3.SAO', 'CSCO34.SAO', 'CSNA3.SAO',
    'CVX.US', 'DISB34.SAO', 'DIS.US', 'DOLY34.SAO', 'EBAY34.SAO',
    'ENGI11.SAO', 'FEDR34.SAO', 'FBOK34.SAO', 'FCX.US', 'FSLR34.SAO',
    'GE.NY', 'GOGL34.SAO', 'GOLD34.SAO', 'GOOGL34.SAO', 'GS.NY',
    'HD.US', 'HON.NY', 'HPQ.US', 'IBM.US', 'IBOV34.SAO', 'INTB34.SAO',
    'ITSA34.SAO', 'ITUB4.SAO', 'JBSAY.ISA', 'JNJ.US', 'KO.US',
    'LAME4.SAO', 'LBRN34.SAO', 'LILY34.SAO', 'LREN3.SAO', 'MCD.US',
    'MDIA3.SAO', 'MDLZ34.SAO', 'MGLU3.SAO', 'MNST34.SAO', 'MRFG3.SAO',
    'MRKT34.SAO', 'MSFT34.SAO', 'MTBR34.SAO', 'NKE.US', 'NVDC34.SAO',
    'NVDB34.SAO', 'NVDA34.SAO', 'OIBR3.SAO', 'OIBR4.SAO', 'PBR.ARG',
    'PBR34.SAO', 'PCAR34.SAO', 'PCKA34.SAO', 'PFE.US', 'PG.US',
    'PSSA3.SAO', 'QCOM34.SAO', 'RADL3.SAO', 'RANI34.SAO', 'RENT3.SAO',
    'RNGO34.SAO', 'RNGO34.ISA', 'ROST34.SAO', 'SBS.US', 'SCHW34.SAO',
    'SGPS3.SAO', 'SPOT34.SAO', 'SQIA3.SAO', 'STBP34.SAO', 'TOTS3.SAO',
    'TRIS3.SAO', 'TWTR34.SAO', 'UBER34.SAO', 'UBSF34.SAO', 'ULVR3.SAO',
    'UNH.US', 'UNIP6.SAO', 'USIM5.SAO', 'VALE3.SAO', 'VIVT3.SAO',
    'VVAR3.SAO', 'WEGE3.SAO', 'WFC.US', 'WMTB34.SAO', 'WMSA34.SAO',
    'XOM.US', 'YDUQ3.SAO'
    
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
