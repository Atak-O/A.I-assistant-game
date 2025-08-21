# -- This Project created by Atak_o --
# -------------------------------------
# This Project is Open_source A.I project so you can change everything you want!
# -------------------------------------

import time
import random

# Küçültme/normalize yardımcısı (Türkçe için güvenli)
def norm(s: str) -> str:
    return " ".join(s.strip().casefold().split())

# Giriş yapma sistemi:
# --------------------
def giris_yap():
    print("Sistem başlatılıyor...")
    time.sleep(1.2)

    kullanici_adi = input("Lütfen kullanıcı adınızı yazınız: ")
    print("Kullanıcı adı kontrol ediliyor, lütfen bekleyiniz...")
    time.sleep(1)

    if kullanici_adi == "Atakan":
        print("✅ Kullanıcı adı doğru girildi.")
        time.sleep(0.5)

        parola = input("Lütfen parolayı giriniz: ")
        print("Parola kontrol ediliyor, lütfen bekleyiniz...")
        time.sleep(1)

        if parola == "141214":
            print("✅ Parola doğru girildi.")
            time.sleep(0.5)
            return True
        else:
            print("❌ Parola yanlış girildi.")
            parola = input("Lütfen parolayı tekrar giriniz: ")
            print("Parola tekrar kontrol ediliyor, lütfen bekleyiniz...")
            time.sleep(1)
            if parola == "141214":
                print("✅ Parola doğru girildi.")
                time.sleep(0.5)
                return True
            else:
                print("❌ Parola yine yanlış girildi. Giriş başarısız.")
                return False
    else:
        print("❌ Kullanıcı adı yanlış girildi.")
        print("Sistem kapanıyor...")
        time.sleep(1)
        return False

# Kapı oyunu komutu:
# --------------------
def kapı_oyunu():
    print("🎮 Kapı oyunu başlatılıyor...")
    time.sleep(0.8)
    print("Eğer kapıyı açtığında bir dinozor varsa 40 puan, eşek sürüsü varsa 30 puan ve ev varsa 100 puan.")
    kapi = norm(input("Lütfen bir kapı seçiniz! (1/2/3): "))

    if kapi == "1":
        print("🟥 Kırmızı kapıyı açtın ve bir dinozor ile karşılaştın. 🦖 Kaçabildin mi acaba?")
    elif kapi == "2":
        print("🟩 Yeşil kapıyı açtın ve bir eşek sürüsüyle karşılaştın. 😅 Seslerinden kulakların çınlıyor!")
    elif kapi == "3":
        print("🟦 Mavi kapıyı açtın ve güzel mi güzel evine ulaştın! 🏡 Artık şöminenin karşısına geçip güzelce dinlenebilirsin.")
    else:
        print("🚫 Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

# Çoklu bilmece:
# -----------------
def bilmece():
    bilmeceler = [
        {"soru": "🧠 Bilgi verir herkese! En güzel dosttur bize! Cevap nedir?", "cevaplar": {"kitap", "book"}},
        {"soru": "🧩 Hep ileri yürürüm, asla geri dönmem. Ben neyim?", "cevaplar": {"zaman", "time"}},
        {"soru": "✨ Ne kadar alırsan o kadar büyür. Nedir?", "cevaplar": {"delik", "hole"}},
        {"soru": "🌙 Gündüz görünmem, gece parlarım. Ben neyim?", "cevaplar": {"ay", "moon"}},
    ]
    soru = random.choice(bilmeceler)
    user = norm(input(soru["soru"] + " "))
    if user in soru["cevaplar"]:
        print("✅ Doğru cevap! Aferin! 😎")
    else:
        dogru = "/".join(sorted(soru["cevaplar"]))
        print(f"❌ Yanlış cevap. Doğrusu: {dogru}")

# Departman seçimi
# -------------------
def departman_secimi():
    q = norm(input("Kodlama, çizim veya test - bunlardan en çok hangisini seviyorsunuz? "))
    if q == "kodlama":
        print("👩‍💻 Geliştirme departmanına hoş geldiniz!")
    elif q in {"çizim", "cizim"}:
        print("🎨 Tasarım departmanına hoş geldiniz!")
    elif q == "test":
        print("🧪 Kalite kontrol departmanına hoş geldiniz!")
    else:
        print("🙃 Maalesef size sunabileceğimiz bir departman yok.")

# Oyun önerisi komutu:
# -------------------
def oyun_önerisi():
    q1 = norm(input("En sevdiğiniz oyun türü nedir? (yarış oyunu, dövüş oyunu, nişancı oyunu): "))
    q2 = norm(input("Arkadaşlarınız ile oyun oynamayı sever misiniz? (evet/hayır): "))

    if q1 == "dövüş oyunu" and q2 == "evet":
        print("Street Fighter oynamayı çok seversiniz.")
    elif q1 == "dövüş oyunu" and q2 == "hayır":
        print("Maalesef önerebileceğimiz bir oyun yok ):")
    elif q1 == "yarış oyunu" and q2 == "evet":
        print("Cars 3: Driven To Win oynamayı çok seveceksiniz!")
    elif q1 == "yarış oyunu" and q2 == "hayır":
        print("Assetto Corsa oynamayı çok seveceksiniz!")
    elif q1 == "nişancı oyunu" and q2 == "evet":
        print("Call of Duty oynamayı çok seveceksiniz!")
    elif q1 == "nişancı oyunu" and q2 == "hayır":
        print("Rainbow Six Siege oynamayı çok seveceksiniz!")
    else:
        print("Maalesef önerebileceğimiz bir oyun yok!")

# Stajyer testi komutu:
# -------------------
def stajyer_testi():
    print("📝 Stajyer testi başladı!")
    print("Seviyeni seç: 'başlangıç', 'orta', 'ileri'")
    python_seviyesi = norm(input("Ne kadar Python bilgin var? "))

    if python_seviyesi in {"orta", "ileri"}:
        print("✅ Hoş geldin stajyer! Şimdi minik bir Python quiz'i başlıyor...")
        time.sleep(1)

        sorular = [
            {"soru": "1) Turtle'da çizimi durdurmak için hangisi?\nA) t.pendown()  B) t.penup()  C) t.goto()", "cevap": "b"},
            {"soru": "2) Aşağıdakilerden hangisi bir Python veri tipidir?\nA) int  B) fast  C) speed", "cevap": "a"},
            {"soru": "3) 'print()' fonksiyonu ne işe yarar?\nA) Uzunluğu döndürür  B) Yazıyı küçültür  C) Ekrana yazı yazar", "cevap": "c"},
        ]

        dogru_sayisi = 0
        for s in sorular:
            cevap = norm(input(s["soru"] + " "))
            if cevap == s["cevap"]:
                print("✅ Doğru!")
                dogru_sayisi += 1
            else:
                print("❌ Yanlış cevap!")

        print(f"📊 Test bitti! {dogru_sayisi}/{len(sorular)} doğru yaptın.")

        if dogru_sayisi == len(sorular):
            print("🎉 Tebrikler! Tüm soruları doğru bildin, gerçekten iyi bir seviyedesin!")
        else:
            print("😅 İdare eder ama daha çalışmalısın!")
    elif python_seviyesi in {"başlangıç", "baslangic"}:
        print("❌ Üzgünüz, koşulları karşılamıyorsunuz 😕")
    else:
        print("🚫 Anlamadım, lütfen 'başlangıç', 'orta' veya 'ileri' yaz.")

# Yardım komutu:
# -------------------
def yardım():
    print("Komut listesi yükleniyor...")
    time.sleep(0.6)
    print(
        "\nKomutlar:\n"
        " • kapı oyunu           : Bir kapı seçme oyunu başlatır.\n"
        " • stajyer testi        : Seviyeye göre mini Python testi.\n"
        " • bilmece              : Rastgele bilmeceler sorar.\n"
        " • oyun önerisi         : Tercihlere göre oyun önerir.\n"
        " • departman            : Sana uygun departmanı önerir.\n"
        " • yazı tura            : Yazı–tura atar.\n"
        " • yardım               : Bu menüyü gösterir.\n"
        " • çıkış                : Programı kapatır.\n"
    )

# --- YAZI–TURA ENTEGRASYONU ---
def yazi_tura(atim_sayisi: int = 1):
    """Yazı–tura atar. atim_sayisi > 1 ise ardışık birden fazla atım yapar."""
    print("🪙 Para havaya fırlatılıyor...")
    time.sleep(0.6)
    sonuclar = []
    for _ in range(max(1, int(atim_sayisi))):
        sonuclar.append(random.choice(["Yazı", "Tura"]))
        time.sleep(0.2)
    if len(sonuclar) == 1:
        print("Sonuç:", sonuclar[0])
    else:
        print("Sonuçlar:", ", ".join(sonuclar))
        print(f"Özet → Yazı: {sonuclar.count('Yazı')} | Tura: {sonuclar.count('Tura')}")



# --- ANA DÖNGÜ ---
def main():
    if giris_yap():
        print("🧠 Hoş geldiniz efendim, size nasıl yardımcı olabilirim?")
        while True:
            raw = input("Komut girin (yardım için 'yardım', çıkmak için 'çıkış'): ")
            command = norm(raw)

            # Komut eşlemeleri (takma adlar)
            if command in {"kapı oyunu", "kapi oyunu"}:
                kapı_oyunu()
            elif command == "bilmece":
                print("Bilmece yükleniyor, lütfen bekleyiniz...")
                time.sleep(0.5)
                bilmece()
            elif command == "stajyer testi":
                print("Stajyer testi başlıyor, lütfen bekleyiniz...")
                time.sleep(0.5)
                stajyer_testi()
            elif command == "oyun önerisi":
                print("Oyun önerisi programı başlıyor, lütfen bekleyiniz...")
                time.sleep(0.5)
                oyun_önerisi()
            elif command == "yardım":
                yardım()
            
            elif command in {"yazı tura", "yazi tura", "yazı-tura", "tura"}:
                # Kullanıcı "yazı tura 3" gibi atım sayısı verirse yakala
                parts = raw.strip().split()
                # sayı son parçada olabilir: yazı tura 3
                atim = 1
                if parts and parts[-1].isdigit():
                    atim = int(parts[-1])
                yazi_tura(atim_sayisi=atim)
            elif command == "departman":
                departman_secimi()
            elif command in {"çıkış", "cikis"}:
                print("Program kapanıyor... Görüşürüz!")
                break
            else:
                print("🚫 Geçersiz komut. 'yardım' yazarak komutları görebilirsiniz.")
    else:
        print("Giriş yapılamadı. Program kapanıyor...")

if __name__ == "__main__":
    main()
