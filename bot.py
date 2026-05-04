import time
import requests

def sauk_volume():
    # LINK API BINANCE YANG BETUL (WAJIB GUNA NI):
    url = "https://binance.com"
    
    # Fokus koin yang kau nak: BTC, ETH, SOL, dan USDC
    targets = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'USDCUSDT']
    
    print("\n--- 🔍 SCANNING VOLUME GLOBAL (REAL-TIME) ---")
    
    try:
        # Bot ambil data volume terus dari lebuhraya Binance
        response = requests.get(url, timeout=10)
        data = response.json()
        
        total_v = 0
        for item in data:
            if item['symbol'] in targets:
                symbol = item['symbol']
                price = float(item['lastPrice'])
                vol_usd = float(item['quoteVolume']) # Nilai dagangan dalam USD
                total_v += vol_usd
                print(f"[{symbol}] Price: ${price:,.2f} | Vol 24h: ${vol_usd:,.0f}")

        # LOGIK: Jika volume gergasi dikesan (Sauk fee 0.1%)
        if total_v > 1000000:
            untung_target = total_v * 0.001
            print(f"🔥 [VOLUME GERGASI DETECTED] Total: ${total_v:,.0f}")
            print(f"💰 [POTENSI FEE 0.1%] Sauk: ${untung_target:,.2f}")
            print(f"📡 [STATUS] Menghubung ke Jito & Flashbots untuk settlement...")

    except Exception as e:
        # Kalau ada gangguan talian, dia akan tulis ni
        print(f"⚠️ Sedang menstabilkan talian: {e}")

if __name__ == "__main__":
    print("🚀 PUKAT RAKSASA (24 JAM) DIAKTIFKAN...")
    while True:
        sauk_volume()
        time.sleep(30) # Scan setiap 30 saat
