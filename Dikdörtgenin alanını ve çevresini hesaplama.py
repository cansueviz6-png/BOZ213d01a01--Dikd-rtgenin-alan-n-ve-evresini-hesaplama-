# Kullanıcıdan kısa ve uzun kenar uzunluklarını alıyoruz
kisa_kenar = float(input("Lütfen kısa kenar uzunluğunu girin: "))
uzun_kenar = float(input("Lütfen uzun kenar uzunluğunu girin: "))

# Alan hesaplama
alan = kisa_kenar * uzun_kenar

# Çevre hesaplama
cevre = 2 * (kisa_kenar + uzun_kenar)

# Sonuçları ekrana yazdırma
print(f"Dikdörtgenin Alanı: {alan}")
print(f"Dikdörtgenin Çevresi: {cevre}")
