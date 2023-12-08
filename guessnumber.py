import random

sayi = random.randint(1, 20)
i = 3

while i > 0:
    tahmin = input("Sayı tahmin oyununa hoş geldiniz. 1 ile 20 arasında bir tamsayı giriniz: ")

    try:
        tahmin = int(tahmin)
    except ValueError:
        print("Lütfen bir tamsayı giriniz!!!")
        continue

    if tahmin == sayi:
        print("Doğru tahmin, tebrikler!!")
        break
    else:
        i -= 1
        if tahmin < sayi:
            print("Daha büyük bir sayı giriniz!")
        else:
            print("Daha küçük bir sayı giriniz!")
        print(f"Yanlış tahmin, kalan tahmin hakkınız: {i}")

        if i == 0:
            print(f"Doğru sayı: {sayi}")
