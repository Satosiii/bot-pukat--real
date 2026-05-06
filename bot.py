import time
import requests

def pukat_harimau():
    # URL ASAL PALING STABIL
    url = "https://binance.com"
    targets = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'USDCUSDT']
    
    print("\n--- 🔍 SCANNING VOLUME GLOBAL (REAL-TIME) ---")
    
    try:
        # Kita tambah 'headers' supaya server Binance nampak bot kau macam orang betul
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            total_v = 0
            for item in data:
                if item['symbol'] in targets:
                    symbol = item['symbol']
                    vol_usd = float(item['quoteVolume'])
                    price = float(item['lastPrice'])
                    total_v += vol_usd
                    fee_01 = vol_usd * 0.001
                    print(f"[{symbol}] Price: ${price:,.2f} | Vol: ${vol_usd:,.0f} | Fee 0.1%: ${fee_01:,.2f}")

            total_fee = total_v * 0.001
            print(f"----------------------------------------------")
            print(f"🔥 TOTAL VOLUME: ${total_v:,.0f}")
            print(f"💰 TOTAL FEE KAU (0.1%): ${total_fee:,.2f}")
            print(f"📡 STATUS: Pukat tengah sauk volume...")
        
        elif response.status_code == 202:
            print("⚠️ Server Binance tengah sesak. Bot tengah beratur, tunggu jap...")
        else:
            print(f"⚠️ Status {response.status_code}. Tengah cuba hubung semula...")

    except Exception as e:
        print(f"⚠️ Menstabilkan talian... {e}")

if __name__ == "__main__":
    print("🚀 PUKAT HARIMAU (24 JAM) DIAKTIFKAN...")
    while True:
        pukat_harimau()
        # Kita buat 30 saat supaya server tak sekat IP kau
        time.sleep(30)
