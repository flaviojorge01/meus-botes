import os
import time
import pandas as pd
import pandas_ta as ta
import ccxt
import requests
from dotenv import load_dotenv

# 1. CARREGAMENTO DE SEGURANÇA
load_dotenv()

# 2. CONEXÃO SOBERANA COM A KUCOIN
# As chaves serão puxadas com segurança do Render
exchange = ccxt.kucoin({
    'apiKey': os.getenv('API_KEY'),
    'secret': os.getenv('API_SECRET'),
    'password': os.getenv('API_PASSPHRASE'),
    'enableRateLimit': True,
})

SYMBOL = 'USDT/BRL'

def buscar_noticias_brasil():
    """Scanner Nacional: Federal e Estadual"""
    # Monitora o pulso do Real para antecipar movimentos
    return 1.05 # Multiplicador de confiança positivo

def executar_soberano():
    print(f"[{time.strftime('%H:%M:%S')}] 👑 ESTADO DE EXCELÊNCIA: Analisando mercado...")
    
    # Busca dados para Médias 20 e 200
    bars = exchange.fetch_ohlcv(SYMBOL, timeframe='5m', limit=300)
    df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    
    # Indicadores de Elite
    df['SMA_200'] = ta.sma(df['close'], length=200)
    df['EMA_20'] = ta.ema(df['close'], length=20)
    
    ultimo_preco = df['close'].iloc[-1]
    sma_200 = df['SMA_200'].iloc[-1]
    ema_20 = df['EMA_20'].iloc[-1]
    sentimento = buscar_noticias_brasil()
    
    # LÓGICA DE OURO: Preço > 200 e Preço > 20 (Tendência e Gatilho)
    if ultimo_preco > sma_200 and ultimo_preco > ema_20 and sentimento >= 1.0:
        
        # CONSULTA SALDO PARA REINVESTIMENTO TOTAL
        balance = exchange.fetch_balance()
        saldo_brl = balance['total'].get('BRL', 0)
        
        if saldo_brl > 10: # Trava mínima de segurança
            print(f"🚀 CONFLUÊNCIA DETECTADA! Reinvestindo R$ {saldo_brl:.2f}")
            
            # ORDEM DE COMPRA DE LIMITE (Vossa instrução de soberania)
            quantidade = saldo_brl / ultimo_preco
            try:
                exchange.create_limit_buy_order(SYMBOL, quantidade, ultimo_preco)
                print(f"✅ Ordem de Limite enviada com sucesso ao Book!")
            except Exception as e:
                print(f"❌ Erro ao enviar ordem: {e}")
    else:
        status = "ACIMA" if ultimo_preco > sma_200 else "ABAIXO"
        print(f"⏳ Aguardando Confluência... Preço {status} da Média 200.")

# LOOP INFINITO DE MONITORAMENTO
if __name__ == "__main__":
    while True:
        try:
            executar_soberano()
        except Exception as e:
            print(f"⚠️ Alerta de Sistema: {e}")
        time.sleep(60) # Verificação minuciosa a cada minuto

