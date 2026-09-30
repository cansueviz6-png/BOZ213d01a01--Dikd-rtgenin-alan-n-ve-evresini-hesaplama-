def dikdortgen_hesapla(kisa_kenar, uzun_kenar):
    cevre = 2 * (kisa_kenar + uzun_kenar)
    alan = kisa_kenar * uzun_kenar
    return cevre, alan


def main():
    try:
        a = float(input("Dikdörtgenin kısa kenarı: "))
        b = float(input("Dikdörtgenin uzun kenarı: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if a <= 0 or b <= 0:
        print("Kenar uzunlukları pozitif olmalıdır.")
        return

    cevre, alan = dikdortgen_hesapla(a, b)
    print(f"Çevre: {cevre}")
    print(f"Alan: {alan}")


main()

