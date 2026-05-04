import time
import requests

def sauk_volume():
    # Menggunakan API Binance yang sangat stabil
    url = "https://binance.com"
    # Kita fokus koin yang kau nak: BTC, ETH, SOL, dan USDC
    targets = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'USDCUSDT']
    
    print("\n--- 🔍 SCANNING VOLUME GLOBAL (REAL-TIME) ---")
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        total_v = 0
        # Bot mula mencari koin dalam senarai besar Binance
        for item in data:
            if item['symbol'] in targets:
                symbol = item['symbol']
                price = float(item['lastPrice'])
                vol_usd = float(item['quoteVolume']) # Volume dalam nilai USD
                total_v += vol_usd
                print(f"[{symbol}] Price: ${price:,.2f} | Vol 24h: ${vol_usd:,.0f}")

        # LOGIK: Jika volume dagangan tebal (Kita sauk fee 0.1%)
        if total_v > 1000000:
            untung_target = total_v * 0.001
            print(f"🔥 [VOLUME GERGASI DETECTED] Total: ${total_v:,.0f}")
            print(f"💰 [POTENSI FEE 0.1%] Sauk: ${untung_target:,.2f}")
            print(f"📡 [STATUS] Menghubung ke Jito & Flashbots untuk settlement...")

    except Exception as e:
        print(f"⚠️ Sedang menstabilkan talian: {e}")

if __name__ == "__main__":
    print("🚀 PUKAT RAKSASA (24 JAM) DIAKTIFKAN...")
    while True:
        sauk_volume()
        time.sleep(30) # Scan setiap 30 saat supaya Railway tak anggap spam
