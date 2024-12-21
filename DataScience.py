import pandas as pd

# Veriyi iceriye aktaralim
veri = pd.read_csv("olimpiyatlar.csv")
veri_head = veri.head(15)

"""
Veride Nan degerler var yani ya veri setinden cikartilacak ya da doldurulacak
Games column gereksiz, veriden drop
Her sporcu madalya almamis: madalya kisminda Nan = Madalya alamamis
Id gereksiz
Bir kisi iki takima katilmis ? 1900 yilinda orad iki ulke var miydi
Ulke kisaltmasi veya takim gereksiz
1920 den oncesi acaba guvenilir veri mi ?
"""
veri.info()
# Sutun isimlerinin degistirilmesi
column =  veri.columns
veri.rename(columns = {
    "ID" : "id",
    "Name" : "isim",
    "Sex" : "cinsiyet",
    "Age" : "yas",
    "Height" : "boy",
    "Weight" : "kilo",
    "Team" : "takim",
    "NOC" : "uok"  ,  # ulusal olimpiyat komitesi
    "Games" : "oyunlar",
    "Year" : "yil",
    "Season" : "sezon",
    "City" : "sehir",
    "Sport" : "spor",
    "Event" : "etkinlik",
    "Medal" : "madalya",
    }, inplace = True)


# Gereksiz (yararsiz) verilerin cikartilmasi

veri = veri.drop(["id","oyunlar"], axis = 1)


# veri_4282 = veri.loc[4282,:]
# Birbirini tekrarlayan veriler
veri_duplicated = veri[veri.duplicated()] 

veri_head = veri.head(15)


# %%%  # Kayip veri problemi
"""
boy ve kilo sutununda bulunan kayip verileri(etkinlik ort) dolduralim
etkinlige gore doldurma ort veya medyan ?  BU VERI SETI ICIN FARK ETMEZ !!!
madalya alamayan sporculari veri setinden cikartalim
"""
# ortalama ve medyan arasinda karar verme??
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.hist(veri.boy, bins = 100)
plt.title("boy")

plt.figure()
plt.hist(veri.kilo, bins = 100)
plt.title("kilo")

describe = veri.describe()

# Boy ve kilo sutununda bulunan kayip verileri dolduralim (etkinlik ortalamasi)
# Unique etkinliklerin ve sayisinin bulunmasi
unique_etkinlik = pd.unique(veri.etkinlik)

veri_gecici = veri.copy() # Gercek veriyi kaybetmeden kopyasiyla calismak
boy_kilo_list = ["boy","kilo"]

for e in unique_etkinlik:
    
    # Etkinlik Filtresi olustur
    etkinlik_filtresi = veri_gecici.etkinlik == e
    # Veriyi etkinlige gore filtrele
    veri_filtreli = veri_gecici[etkinlik_filtresi]
    
    # Boy ve kilo icin etkinlik ozelinde ortalama bul
    for s in boy_kilo_list:
        
        ortalama = np.mean(veri_filtreli[s])
        
        if ~np.isnan(ortalama):  # if np.isnan(ortalama) == False:  IKISI AYNI KULLANIM.
            veri_filtreli[s] = veri_filtreli[s].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri[s])
            veri_filtreli[s] = veri_filtreli[s].fillna(tum_veri_ortalamasi)

    veri_gecici[etkinlik_filtresi] = veri_filtreli
    
veri = veri_gecici.copy()
veri.info()

# Yasta bulunan kayip veri sorununu cinsiyet ve spora gore dolduralim

# Unique etkinliklerin ve sayisinin bulunmasi
essiz_cinsiyet = pd.unique(veri.cinsiyet)
essiz_spor = pd.unique(veri.spor)

veri_gecici = veri.copy() # Gercek veriyi kaybetmeden kopyasiyla calismak
boy_kilo_list = ["boy","kilo"]

for c in essiz_cinsiyet:
    for s in essiz_spor:
        # Cinsiyet Filtresi olustur
        cinsiyet_spor_filtresi = np.logical_and(veri_gecici.cinsiyet == c, veri_gecici.spor == s)
        
        # Spor Filtresi olustur
        spor_filtresi = veri_gecici.spor == s

        # Veriyi etkinlige gore filtrele
        veri_filtreli = veri_gecici[cinsiyet_spor_filtresi]
        
        ortalama = np.mean(veri_filtreli["yas"])
        
        if ~np.isnan(ortalama):  # if np.isnan(ortalama) == False:  IKISI AYNI KULLANIM.
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri["yas"])
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(tum_veri_ortalamasi)

        veri_gecici[cinsiyet_spor_filtresi] = veri_filtreli
    
veri = veri_gecici.copy()
veri.info()


# Madalya alamayan sporcularin bulunmasi
madalya_degiskeni = veri.madalya
null_sayisi = pd.isnull(madalya_degiskeni).sum()

madalya_degiskeni_filtresi = pd.isnull(madalya_degiskeni)

veri = veri[~madalya_degiskeni_filtresi]

veri.to_csv("olimpiyatlar_temizlenmis.csv", index = False)  



# %%  Tek Degiskenli Veri Analizi
import matplotlib.pyplot as plt
def plothistogram(degisken):
    plt.figure()
    plt.hist(veri[degisken], bins= 85, color = "orange")
    plt.xlabel(degisken)
    plt.show()

sayisal_degisken = ["yas","boy","kilo","yil"]

for degisken in sayisal_degisken:
    plothistogram(degisken)


def plotBox(degisken):
    plt.figure()
    plt.boxplot(veri[degisken])
    plt.xlabel(degisken)
    plt.show()

sayisal_degisken = ["yas","boy","kilo"]

for degisken in sayisal_degisken:
    plotBox(degisken)






























