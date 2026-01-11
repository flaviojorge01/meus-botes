import os
import time
from ccxt import kucoin

# O robô pega as chaves que o senhor salvou na Koyeb
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
api_passphrase = os.getenv('API_PASSPHRASE')

# Configuração da conexão com a KuCoin
exchange = kucoin({
    'apiKey': api_key,
    'secret': api_secret,
    'password': api_passphrase,
    'enableRateLimit': True,
})

def iniciar_robo():
    print("------------------------------------------")
    print("👑 BOT REAL INICIALIZADO - KUCOIN 👑")
    print("------------------------------------------")
    
    try:
        # Testa a conexão buscando o saldo
        balance = exchange.fetch_balance()
        usdt_balance = balance['total'].get('USDT', 0)
        print(f"✅ Conexão bem-sucedida!")
        print(f"💰 Saldo disponível: {usdt_balance} USDT")
        
    except Exception as e:
        print(f"❌ Erro ao conectar na KuCoin: {e}")

if __name__ == "__main__":
    iniciar_robo()
