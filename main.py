import tkinter as tk
from datetime import datetime


class Ürün:
    def __init__(self, adı, fiyatı, barkodu):
        self.adı = adı
        self.fiyatı = fiyatı
        self.barkodu = barkodu
        self.adet = 1

    def __str__(self):
        return f"{self.adı}: {self.fiyatı}₺"


# Ürünler listesi
ürünler = [
    Ürün("Süt", 13, "stü1015"),
    Ürün("Yoğurt", 15, "stü2030"),
]

# Sepet
sepet = []


# saat güncelleme
def saat_güncelle():
    şimdi = datetime.now()
    tarih = şimdi.strftime("%Y-%m-%d")
    saat = şimdi.strftime("%H:%M:%S")
    tarih_label.config(text=tarih)
    saat_label.config(text=saat)
    kasa_penceresi.after(1000, saat_güncelle)


def insert_number(num):
    current_value = entry.get()
    entry.delete(0, tk.END)  # Clear current value
    entry.insert(0, current_value + num)




# ürün ekleme
def ürün_ekle():
    global barkod_girişi, hata_mesajı, sepet

    giriş = barkod_girişi.get().lower()
    eklenen = False
    for ürün in ürünler:
        if ürün.barkodu == giriş or ürün.adı.lower() == giriş:
            if any(item.barkodu == ürün.barkodu for item in sepet):
                for item in sepet:
                    if item.barkodu == ürün.barkodu:
                        item.adet += 1
            else:
                sepet.append(Ürün(ürün.adı, ürün.fiyatı, ürün.barkodu))
            sepet_güncelle()
            hata_mesajı.config(text="")
            eklenen = True
            break

    if not eklenen:
        hata_mesajı.config(text="Girdiğiniz ürün bulunmuyor")


# ürün çıkarma
def ürün_çıkar(index):
    sepet.pop(index)
    sepet_güncelle()
    hata_mesajı.config(text="")


# adet güncelleme
def adet_güncelle(index, yeni_adet):
    sepet[index].adet = int(yeni_adet)
    sepet_güncelle()


# sepet güncelleme
def sepet_güncelle():
    for widget in sepet_frame.winfo_children():
        widget.destroy()

    for i, ürün in enumerate(sepet):
        barkod_label = tk.Label(sepet_frame, text=ürün.barkodu, font=("Helvetica", 12))
        barkod_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

        ürün_adı_label = tk.Label(sepet_frame, text=ürün.adı, font=("Helvetica", 12))
        ürün_adı_label.grid(row=i + 1, column=1, padx=15, pady=5, sticky="w")

        kdv_label = tk.Label(sepet_frame, text=f"{ürün.fiyatı * 0.01:.2f}₺", font=("Helvetica", 12))
        kdv_label.grid(row=i + 1, column=2, padx=5, pady=5, sticky="w")

        adet_entry = tk.Entry(sepet_frame, width=5, font=("Helvetica", 12))
        adet_entry.insert(tk.END, ürün.adet)
        adet_entry.grid(row=i + 1, column=3, padx=20, pady=5, sticky="w")

        # Enter tuşuna basıldığında güncelleme işlemi
        adet_entry.bind("<Return>", lambda event, idx=i, entry=adet_entry: adet_güncelle(idx, entry.get()))

        toplam_label = tk.Label(sepet_frame, text=f"{ürün.adet * ürün.fiyatı * 1.08:.2f}₺", font=("Helvetica", 12))
        toplam_label.grid(row=i + 1, column=4, padx=50, pady=5, sticky="w")

    # Toplam tutarı hesapla ve göster
    if sepet:
        toplam_tutar = sum(item.adet * item.fiyatı * 1.08 for item in sepet)
    else:
        toplam_tutar = 0.0

    toplam_tutar_label.config(text=f"Toplam Tutar: {toplam_tutar:.2f}₺")


# kasa ekranı
def kasa_ekranı():
    global saat_label, tarih_label, kasa_penceresi, sepet_frame, toplam_tutar_label, hata_mesajı, barkod_girişi  # global değişkenler

    kasa_penceresi = tk.Toplevel(ana_ekran)
    kasa_penceresi.title("Kasa")
    kasa_penceresi.minsize(1200, 650)

    zaman_fontu = ("Helvetica", 15)

    tarih_label = tk.Label(kasa_penceresi, font=zaman_fontu, fg="orange")
    tarih_label.place(x=1070, y=10)

    saat_label = tk.Label(kasa_penceresi, font=zaman_fontu, fg="orange")
    saat_label.place(x=1082, y=40)

    saat_güncelle()

    barkod_girişi = tk.Entry(kasa_penceresi, font=("Helvetica", 12))
    barkod_girişi.grid(row=0, column=0, padx=10, pady=15)

    ekle_butonu = tk.Button(kasa_penceresi, text="Ekle", command=ürün_ekle, font=("Helvetica", 12))
    ekle_butonu.grid(row=0, column=1, padx=10, pady=15)

    çerçeve = tk.Frame(kasa_penceresi, width=800, height=400, highlightthickness=2, highlightbackground="blue",
                       bg="white")
    çerçeve.grid(row=1, column=1, columnspan=4, padx=10, pady=15, sticky="nsew")

    barkod_label = tk.Label(çerçeve, text="Barkod", font=("Helvetica", 12, "bold"))
    barkod_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    ürün_adı_label = tk.Label(çerçeve, text="Ürün Adı", font=("Helvetica", 12, "bold"))
    ürün_adı_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    kdv_label = tk.Label(çerçeve, text="KDV", font=("Helvetica", 12, "bold"))
    kdv_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

    adet_label = tk.Label(çerçeve, text="Adet", font=("Helvetica", 12, "bold"))
    adet_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")

    toplam_label = tk.Label(çerçeve, text="Toplam Tutarı (₺)", font=("Helvetica", 12, "bold"))
    toplam_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")

    hata_mesajı = tk.Label(kasa_penceresi, text="", font=("Helvetica", 12), fg="red")
    hata_mesajı.grid(row=2, column=0, columnspan=2, padx=10, pady=15)

    # Canvas içinde scrollbar ekleme
    canvas = tk.Canvas(çerçeve)
    scrollbar = tk.Scrollbar(çerçeve, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=1, column=0, columnspan=5, sticky="nsew")
    scrollbar.grid(row=1, column=5, sticky="ns")

    sepet_frame = scrollable_frame

    toplam_tutar_çerçeve = tk.Frame(kasa_penceresi, highlightthickness=5, highlightbackground="blue", bg="white")
    toplam_tutar_çerçeve.grid(row=4, column=3, columnspan=2, padx=10, pady=15, sticky="e")

    toplam_tutar_label = tk.Label(toplam_tutar_çerçeve, text="Toplam Tutar: 0₺", font=("Helvetica", 16, "bold"),
                                  bg="white")
    toplam_tutar_label.pack()

    toplam_tutar_çerçeve.grid_propagate(False)

#tuş takımı
    def __init__(self, kasa_penceresi):

        self.entry = tk.Entry(kasa_penceresi, width=20, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=3)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click(x)
            tk.Button(kasa_penceresi, text=button, width=10, height=3, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def click(self, value):
        current_text = self.entry.get()
        new_text = current_text + value
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)

    class NumpadApp:
        def __init__(self, root):
            self.entry = tk.Entry(kasa_penceresi, width=20, font=('Arial', 18))
            self.entry.grid(row=0, column=0, columnspan=3)

            buttons = [
                '1', '2', '3',
                '4', '5', '6',
                '7', '8', '9',
                '0'
            ]

            row_val = 1
            col_val = 0

            for button in buttons:
                action = lambda x=button: self.click(x)
                tk.Button(kasa_penceresi, text=button, width=10, height=3, command=action).grid(row=row_val, column=col_val)
                col_val += 1
                if col_val > 2:
                    col_val = 0
                    row_val += 1

        def click(self, value):
            current_text = self.entry.get()
            new_text = current_text + value
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)


# ekran seçimi
def seçenek(seçim):
    if seçim == "ürünler":
        ürünler_penceresi()
    elif seçim == "kasa":
        kasa_ekranı()


# ana ekran
ana_ekran = tk.Tk()
ana_ekran.title("Seçim Penceresi")
ana_ekran.minsize(260, 100)
ana_ekran.configure(bg="#D7F0EB")

buton_fontu = ("Helvetica", 11, "bold")

# Butonlar oluşturuluyor
button1 = tk.Button(ana_ekran, text="Ürünler", command=lambda: seçenek("ürünler"), width=20, height=3,
                    background="#507da4", foreground="white", font=buton_fontu)
button2 = tk.Button(ana_ekran, text="Kasa", command=lambda: seçenek("kasa"), width=20, height=3, background="#1c434a",
                    foreground="#FFEAA7", font=buton_fontu)

# Butonlar yerleştiriliyor
button1.grid(row=1, column=0, padx=10, pady=15)
button2.grid(row=1, column=1, padx=20, pady=15)

ana_ekran.mainloop()
