import time
import requests

def pukat_harimau():
    # ALAMAT DATA REAL-TIME (WAJIB ADA PERKATAAN 'api.')
    url = "https://binance.com"
    
    # Koin sasaran: BTC, ETH, SOL, dan USDC (Termasuk USDT volume)
    targets = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'USDCUSDT']
    
    print("\n--- 🔍 SCANNING VOLUME GLOBAL (REAL-TIME) ---")
    
    try:
        # Bot ambil data terus dari server (Timeout 15 saat supaya tak jem)
        response = requests.get(url, timeout=15)
        
        # Check kalau server bagi respon betul (200)
        if response.status_code == 200:
            data = response.json()
            total_v = 0
            
            for item in data:
                if item['symbol'] in targets:
                    symbol = item['symbol']
                    price = float(item['lastPrice'])
                    vol_usd = float(item['quoteVolume']) # Nilai dagangan dalam USD
                    total_v += vol_usd
                    
                    # Kira fee 0.1% untuk setiap koin
                    fee_individu = vol_usd * 0.001
                    print(f"[{symbol}] Price: ${price:,.2f} | Vol: ${vol_usd:,.0f} | Fee 0.1%: ${fee_individu:,.2f}")

            # KIRA TOTAL FEE KESELURUHAN (TANPA SYARAT VOLUME)
            total_fee = total_v * 0.001
            print(f"----------------------------------------------")
            print(f"🔥 VOLUME TERKUMPUL: ${total_v:,.0f}")
            print(f"💰 TOTAL FEE KAU (0.1%): ${total_fee:,.2f}")
            print(f"📡 STATUS: Pukat sedang sauk volume market...")
        else:
            print(f"⚠️ Alamat data sibuk. Status: {response.status_code}")

    except Exception as e:
        print(f"⚠️ Sedang menstabilkan talian: {e}")

if __name__ == "__main__":
    print("🚀 PUKAT HARIMAU (SAUK SEMUA) DIAKTIFKAN...")
    while True:
        pukat_harimau()
        # Bot berehat 20 saat sebelum sauk lagi
        time.sleep(20)
