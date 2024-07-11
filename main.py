import tkinter as tk
from datetime import datetime
# Saat güncelleme fonksiyonu
def saat_güncelle():
    şimdi = datetime.now()
    tarih = şimdi.strftime("%Y-%m-%d")
    saat = şimdi.strftime("%H:%M:%S")
    tarih_label.config(text=tarih)
    saat_label.config(text=saat)
    kasa_penceresi.after(1000, saat_güncelle)

# Ürünler ekranı
def ürünler():
    ürünler_penceresi = tk.Toplevel(ana_ekran)
    ürünler_penceresi.title("Ürünler")
    ürünler_penceresi.minsize(1200, 650)

# Kasa ekranı
def kasa():
    global saat_label, tarih_label, kasa_penceresi  # global değişkenler

    kasa_penceresi = tk.Toplevel(ana_ekran)
    kasa_penceresi.title("Kasa")
    kasa_penceresi.minsize(1200, 650)

    zaman_fontu = ("Helvetica", 15)

    tarih_label = tk.Label(kasa_penceresi, font=zaman_fontu, fg="orange")
    tarih_label.place(x=1070, y=10)

    saat_label = tk.Label(kasa_penceresi, font=zaman_fontu, fg="orange")
    saat_label.place(x=1082, y=40)

    saat_güncelle()

def seçenek(selection):
    if selection == "ürünler":
        ürünler()
    elif selection == "kasa":
        kasa()

ana_ekran = tk.Tk()
ana_ekran.title("Seçim Penceresi")
ana_ekran.minsize(260, 100)
ana_ekran.configure(bg="#D7F0EB")

buton_fontu = ("Helvetica", 11, "bold")

# Butonlar oluşturuluyor
button1 = tk.Button(ana_ekran, text="Ürünler", command=lambda: seçenek("ürünler"), width=20, height=3, background="#507da4", foreground="white", font=buton_fontu)
button2 = tk.Button(ana_ekran, text="Kasa", command=lambda: seçenek("kasa"), width=20, height=3, background="#1c434a", foreground="#FFEAA7", font=buton_fontu)

# Butonlar yerleştiriliyor
button1.grid(row=1, column=0, padx=10, pady=15)
button2.grid(row=1, column=1, padx=20, pady=15)

ana_ekran.mainloop()


#product class
class ürün():
    def __init__(self, adı, fiyatı, miktarı, barkodu):
        self.adı = adı
        self.fiyatı = fiyatı
        self.barkodu = barkodu
        self.miktarı = miktarı

    def __str__(self):
        return f"{self.miktarı} {self.adı}:{self.fiyatı}₺"
#Products
süt = ürün("süt", 13, "1l", "stü1015")
yoğurt = ürün("yoğurt", 15, "5kg", "stü2030")
#class to receive products supplied by the user
ürünler = []

while True:
    istek = input("ürün giriniz.çıkmak için q tuşuna basınız: ")
    if istek == "q":
        break
    elif istek == "süt" or istek == "stü1015":
        print(süt)
        ürünler.append(süt)
    elif istek == "yoğurt" or istek == "stü2030":
        print(yoğurt)
        ürünler.append(yoğurt)
    else:
        print("girdiğiniz ürün bulunmuyor")

print("\n".join([f"{ürün.adı}: {ürün.fiyatı}₺" for ürün in ürünler]))
print(f"\033[1mToplam:\033[0m {sum([ürün.fiyatı for ürün in ürünler])}₺")
