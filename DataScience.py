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

# %%  Kategorik Degiskenler

def plotBar(degisken, n = 5): # EN COK 5 ADET VERIYI GORSELLESTIR
    
    veri_ = veri[degisken]
    # value counts
    veri_sayma = veri_.value_counts() # value counts
    veri_sayma = veri_sayma[:n]
    
    plt.figure()
    plt.bar(veri_sayma.index, veri_sayma, color = "orange")
    plt.xticks(veri_sayma.index ,veri_sayma.index.values)
    plt.xticks(rotation = 45)
    plt.ylabel("Frekans")
    plt.title(f"Veri Frekansi : {degisken}")
    plt.show()
    print(f"{veri_sayma}")
    
# Dataframe icerisinde istenilen tipteki degiskenleri bul
categorical_columns = veri.select_dtypes(include = ["object"]).columns

for degisken in categorical_columns:
    plotBar(degisken, 10)

# %%  IKI DEGISKENLI VERI ANALIZI

# Cinsiyete gore boy ve kilo karsilastirmasi.
import pandas as pd
erkek = veri[veri.cinsiyet == "M"]
kadin = veri[veri.cinsiyet == "F"]


plt.figure()
plt.scatter(kadin.boy, kadin.kilo, alpha = 0.8, label = "Kadin")
plt.scatter(erkek.boy, erkek.kilo, alpha = 0.1, label = "Erkek")
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Boy ve Kilo Arasindaki Iliski")
plt.legend()

# correlation calculation
numeric_correlation = veri.loc[:, ["yas","boy","kilo"]].corr()

# madalya ve yas arasindaki correlation
veri_gecici = veri.copy()
veri_gecici = pd.get_dummies(veri_gecici, columns = ["madalya"])
numeric_correlation_yas_madalya = veri_gecici.loc[:, ["yas",'madalya_Gold','madalya_Bronze','madalya_Silver']].corr()

# Takimlarin kazandiklari altin gumus ve bronz madalya sayilari
# Group By
veri_gecici["takim"] = veri_gecici["takim"].replace({
    "Soviet Union": "Russia"})
groupby_takim = veri_gecici[["takim","madalya_Gold","madalya_Silver","madalya_Bronze"]].groupby(["takim"], as_index = False).sum()
groupby_takim_sorted = groupby_takim.sort_values(by = "madalya_Gold", ascending = False)
groupby_takim_sorted_20 = groupby_takim_sorted[:20]


turkey = groupby_takim.query("takim == 'Turkey'") # Sadece Turkiyeyi filtreleme

# Kazanilan madalyalarin sehirlere gore ortalamalari

groupby_sehir = veri_gecici[["sehir","madalya_Bronze","madalya_Gold","madalya_Silver"]].groupby("sehir").sum().sort_values(by = "madalya_Gold", ascending = False)

# Kazanilan madalyalarin cinsiyete gore ortalamalari

groupby_cinsiyet = veri_gecici[["cinsiyet","madalya_Bronze","madalya_Gold","madalya_Silver"]].groupby("cinsiyet").sum().sort_values(by = "madalya_Gold", ascending = False)

# %% COK DEGISKENLI VERI ANALIZI

# Pivot table
# Madalya alan sporcularin cinsiyetlerine gore boy, kilo ve yas ort bakalim.
# 3 adet madalya, 2(cinsiyet)*3(boy,kilo,yas)*3(mean,max,min) = 18
veri_pivot = veri.pivot_table(index = "madalya",
                              columns = "cinsiyet",
                              values = ["boy","kilo","yas"],
                              aggfunc = {"boy": np.mean,
                                         "kilo": [np.median,np.max,np.min],
                                         "yas": [np.min,np.max,np.std]})

# Takimlara ve cinsiyete gore alinan madalya sayilarinin toplami, max ve min degerleri


#takımlara ve cinsiyete gore alınan madalya sayıların toplamı ve maks ve min değeleri

veri_pivot_takim = veri_gecici.pivot_table(index="takim", columns = "cinsiyet",
                                           values=["madalya_Gold","madalya_Silver","madalya_Bronze"],
                                           aggfunc={"madalya_Gold":[np.sum],
                                                    "madalya_Silver":[np.sum],
                                                    "madalya_Bronze":[np.sum]})

veri_pivot_takim["total"] = (
    veri_pivot_takim["madalya_Gold"].sum(axis = 1) +
    veri_pivot_takim["madalya_Broze"].sum(axis = 1) +
    veri_pivot_takim["madalya_Silver"].sum(axis = 1))

veri_pivot_takim = veri_pivot_takim.sort_values(by = "total", ascending = False)[:100]























