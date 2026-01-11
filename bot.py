import ccxt
import time
import pandas as pd
from dotenv import load_dotenv
import os

# 1. Carregar as chaves do cofre (.env)
load_dotenv()

# 2. Configurar a conexão com a MEXC
mexc = ccxt.mexc({
    'apiKey': os.getenv('MEXC_API_KEY'),
    'secret': os.getenv('MEXC_SECRET_KEY'),
})

def get_vwap(symbol):
    # Busca dados para calcular o preço médio dos grandes players
    bars = mexc.fetch_ohlcv(symbol, timeframe='1h', limit=24)
    df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
    tp = (df['high'] + df['low'] + df['close']) / 3
    vwap = (tp * df['vol']).sum() / df['vol'].sum()
    return vwap

def executar_patrulha():
    symbol = 'LINK/USDT'
    print(f"🏰 Patrulha Imperial Ativa... {time.ctime()}")
    
    # Busca o preço atual da LINK
    ticker = mexc.fetch_ticker(symbol)
    current_price = ticker['last']
    vwap_val = get_vwap(symbol)
    
    # Estratégia Profissional (Versão 3)
    if current_price > vwap_val:
        print(f"✅ SINAL: Preço (${current_price}) acima do VWAP (${vwap_val:.2f}). Mercado Forte!")
    else:
        print(f"📉 AGUARDANDO: Preço abaixo do VWAP. Não é hora de arriscar.")

# Inicia o robô para vigiar o mercado a cada 60 segundos
while True:
    try:
        executar_patrulha()
    except Exception as e:
        print(f"Aviso ao Trono: {e}")
    time.sleep(60)
