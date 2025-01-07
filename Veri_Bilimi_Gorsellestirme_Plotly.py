import plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veri = pd.read_csv("universite_siralamasi.csv")

# sütun isimlerinin değiştirilmesi
veri.rename(columns={'world_rank'             : 'dunya_siralama', 
                     'university_name'        : 'uni_isim', 
                     'country'                : 'ulke', 
                     'teaching'               : 'ogretim', 
                     'international'          : 'uluslararası', 
                     'research'               : 'arastirma', 
                     'citations'              : 'alinti', 
                     'income'                 : 'gelir', 
                     'total_score'            : 'toplam_puan',
                     'num_students'           : 'ogrenci_sayisi', 
                     'student_staff_ratio'    : 'ogrenci_calisan_orani', 
                     'international_students' : 'uluslararası_ogrenci',
                     'female_male_ratio'      : 'kadin_erkek_orani',
                     'year'                   : 'yil'}, inplace=True) 
# inplace = True dediğimiz zaman ismi değiştirilen veri otomatik olarak veri variable'a kaydedilir
# unique_ulke  = veri.ulke.unique()
# unique_uni  = veri.uni_isim.unique()
# unique_ogretim  = veri.ogretim.unique()

"""
eksik verileri:
    ogrenci_sayisi       
    ogrenci_calisan_orani  
    uluslararası_ogrenci   
    kadin_erkek_orani
    
    nan değerler var, - degerler var 
    
    dunya_siralamasi: =, - karakterlerin kaldirilip integere cevir
    uni_isim: native language karakterleri var mesela: 'Eötvös Loránd University'
    
    ulke: yanlis yazim var mesela united-> unted
    
    ogretim de sikinti yok
    
    uluslararasi: eksik veri var, ve float a cevrilmesi lazim
    gelir ve toplam puan: kayip veri, ve floata cevrilmesi lazim
    ogrenci_sayisi: kayip veri ve floata cevrilmesi lazim
    
    uluslararasi_ogrenci: % kaldirilmasi
    
    kadin_erkek_orani: normal oran yazilmali ornegin 48:52 yerine -> 48
    
    yil: problem yok

"""

# %% PLOTLY LINE  + SCATTER PLOT

df = veri.iloc[:100, :]

cizgi1 = go.Scatter(x = df.dunya_siralama,  # X ekseninde dunya siralamsi olsun demek
                    y = df.alinti,
                    mode = "lines+markers", # Cizgi ve sacilim grafigi
                    name = "Alinti",
                    marker = dict(color = "rgba(78,78,250,0.85)"), # renk
                    text = df.uni_isim
                    )

cizgi2 = go.Scatter(x = df.dunya_siralama,  # X ekseninde dunya siralamsi olsun demek
                    y = df.alinti,
                    mode = "lines+markers", # Cizgi ve sacilim grafigi
                    name = "Ogretim",
                    marker = dict(color = "rgba(254,0,0,1)"), # renk
                    text = df.uni_isim
                    )

veri_ = [cizgi1, cizgi2]

yerlesim = dict(title = "Ilk 100 Alinti Puani", xaxis = dict(title = "Dunya Siralamasi"))

fig = dict(data = veri_, layout = yerlesim)

plot(fig, filename = "plotly_cizgi1.html")

# %% BAR PLOT

veri2014 = veri[veri.yil == 2014].iloc[:5,:]
 
bar1 = go.Bar(x= veri2014.uni_isim,
              y = veri2014.alinti,
              name = "Alinti",
              marker = dict(color = "rgba(255, 127, 39, 0.5)", line = dict(color = "rgba(0,0,0,0)", width = 1.5)),
              text = veri2014.ulke)

bar2 = go.Bar(x= veri2014.uni_isim,
              y = veri2014.ogretim,
              name = "Ogretim",
              marker = dict(color = "rgba(64, 127, 128, 0.5)", line = dict(color = "rgba(0,0,0,0)", width = 1.5)),
              text = veri2014.ulke)

veri_ = [bar1, bar2]
yerlesim = go.Layout(barmode = "group")
fig = go.Figure(data = veri_, layout = yerlesim)
plot(fig, filename = "plotly_bar.html")

# %% BAR VE SCATTER PLOT
"""
2015 yılına ait ilk 10 üniversitenin öğretim skorlarını bar plot olarak, alıntı skorlarını ise line+scatter plot olarak çizdirelim
"""

veri2015 = veri[veri.yil == 2015].iloc[:10, :]

bar = go.Bar(
    x=veri2015.uni_isim,
    y=veri2015.ogretim,
    name="Öğretim",
    marker=dict(
        color="rgba(255, 120, 20, 0.6)",
        line=dict(color="rgba(0,100,0,0.5)", width=1.5),
    ),
    text=veri2015.ulke,
)

cizgi = go.Scatter(
    x=veri2015.uni_isim,
    y=veri2015.alinti,
    name="Alıntı",
    marker=dict(
        color="rgba(64,0,32,0.5)",
        line=dict(color="rgba(32,200,200,0.5)", width=1.5),
    ),
    text=veri2015.ulke,
)

veri_ = [bar, cizgi]
yerlesim = go.Layout(barmode="group")
fig = go.Figure(data=veri_, layout=yerlesim)
plot(fig, filename="plotly_bar_cizgi.html")
# %% PIE CHART


veri2016 = veri[veri.yil == 2016].iloc[:8,:]
dilim1 = veri2016.ogrenci_sayisi
dilim1_list = [float(i.replace(",", "")) for i in veri2016.ogrenci_sayisi]
etiketler = veri2016.uni_isim

pie = go.Pie(labels = etiketler,
             values = dilim1_list,
             hoverinfo = "label+value+percent",
             textinfo = "value+percent",
             rotation = 180,
             hole = 0.3, 
             marker = dict(line=dict(color = "rgba(0,0,0,1)", width = 1)))
             
veri_ = [pie]   
yerlesim = dict(title = "2016 yili verileri")
fig = dict(data = veri_, layout = yerlesim)
plot(fig, filename = "plotly_pie.html")   

# %% 
"""
2016 ilk 8 uni, gelir dagilimi pie chart
"""
dilim2 = veri2016.gelir

dilim2_list = [float(i) for i in veri2016.gelir]

etiketler = veri2016.uni_isim 

pie = go.Pie(labels = etiketler, 
             values = dilim2_list,
             hoverinfo="label+value+percent", #mouse üstüne gelince 
             textinfo="value+percent", #üzerinde yazan 
             rotation=180, #
             hole=0.3,#%30 demek hole ortada yuvarlak
             marker=dict(line=dict(color="rgba(0,0,0,0)", width=1)))

veri_ = [pie]

yerlesim = dict(title="2016 yili gelir  verileri")

fig = dict( data = veri_, layout=yerlesim)
plot(fig,filename="plotly_pie_gelir.html")

# %% histogram

veri2011 = veri.ogrenci_calisan_orani[veri.yil == 2011]
veri2012 = veri.ogrenci_calisan_orani[veri.yil == 2012]

hist1 = go.Histogram(x = veri2011,
                     name = "2011",
                     opacity=0.75,
                     marker = dict(color = "rgba(171,50.144,0.6)"))

hist2 = go.Histogram(x = veri2012,
                     name = "2012",
                     opacity=0.75,
                     marker = dict(color = "rgba(23,150,196,0.6)"))

veri_ = [hist1, hist2]

yerlesim = go.Layout(title = "2011 ve 2012 ogrenci calisan orani", xaxis = dict(title = "ogrenci calisan orani"), yaxis = dict(title="frekans"))

fig = go.Figure(data = veri_, layout=yerlesim)

plot(fig, filename = "plotly_histogram.html")

# %% box plot
veri2015 = veri[veri.yil == 2015].iloc[:100,:]

kutu1 = go.Box(y = veri2015.toplam_puan.astype("float"),
               name = "2015 Toplam Puan")

kutu2 = go.Box(y = veri2015.arastirma, 
               name = "2015 arastirma puani")

veri_ = [kutu1, kutu2]

plot(veri_, filename = "plotly_box.html")

# %% 
"""
ogrenci calisan orani 
2013, 2014 ve 2015 yillari icin ilk 100 university box plot gosterimi

"""
veri2013 = veri[veri.yil == 2013].iloc[:100,:]
veri2014 = veri[veri.yil == 2014].iloc[:100,:]
veri2015 = veri[veri.yil == 2015].iloc[:100,:]

kutu_1 = go.Box(y = veri2013.ogrenci_calisan_orani,
              name = "2013 Ö/Ç oranı", text = veri2013.uni_isim + "/ " + veri2013.ulke)

kutu_2 = go.Box(y = veri2014.ogrenci_calisan_orani,
              name = "2014 Ö/Ç oranı", text = [f"Üniversite: {uni}, Ülke: {ulke}" for uni, ulke in zip(veri2014.uni_isim, veri2014.ulke)])


kutu_3 = go.Box(y = veri2015.ogrenci_calisan_orani,
              name = "2015 Ö/Ç oranı", text = veri2015.uni_isim)

veri_ = [kutu_1, kutu_2, kutu_3]

plot(veri_, filename= "plotly_box_ogrenci_calisan.html")

# %% subplots

veri2015 = veri[veri.yil == 2015]

sub1 = go.Scatter(x = veri2015.dunya_siralama,
                  y = veri2015.arastirma,
                  name = "arastirma")

sub2 = go.Scatter(x = veri2015.dunya_siralama,
                  y = veri2015.alinti,
                  name = "alinti",
                  xaxis = "x2",
                  yaxis = "y2")

sub3 = go.Scatter(x = veri2015.dunya_siralama,
                  y = veri2015.gelir,
                  name = "gelir",
                  xaxis = "x3",
                  yaxis = "y3")

sub4 = go.Scatter(x = veri2015.dunya_siralama,
                  y = veri2015.toplam_puan,
                  name = "toplam_puan",
                  xaxis = "x4",
                  yaxis = "y4")

veri_ = [sub1, sub2, sub3, sub4]

yerlesim = go.Layout( xaxis = dict(domain = [0, 0.45]),
                         yaxis = dict(domain = [0, 0.45]),
                         xaxis2 = dict(domain = [0.55, 1]),
                         xaxis3 = dict(domain = [0, 0.1], anchor = "y3"),
                         xaxis4 = dict(domain = [0.2, 1], anchor = "y4"),
                         yaxis2 = dict(domain = [0, 0.45], anchor = "x2"),
                         yaxis3 = dict(domain = [0.55, 1]),
                         yaxis4 = dict(domain = [0.55, 1], anchor = "x4"))

fig = go.Figure(data=veri_, layout=yerlesim)
plot(fig, filename = "plotly_subplot.html")


# %% 3d 
veri2015 = veri[veri.yil == 2015]

threeD = go.Scatter3d(x = veri2015.dunya_siralama,
                  y = veri2015.arastirma,
                  z = veri2015.alinti,
                  mode = "markers",
                  marker = dict(size = 10, color = "green"),
                  opacity = 0.5) 

veri_ = [threeD]

yerlesim = go.Layout()

fig = go.Figure(data = veri_, layout = yerlesim)

plot(fig, filename = "plotly_3d.html")

# %% world map
veri2016 = veri[veri.yil == 2016]
# veri2016.ulke.value_counts()

ulkeye_gore_toplam_veriler = veri2016.groupby("ulke").sum()

world_map = go.Choropleth(locations = ulkeye_gore_toplam_veriler.index,
                          locationmode="country names",
                          z = ulkeye_gore_toplam_veriler.arastirma,
                          text = ulkeye_gore_toplam_veriler.index,
                          autocolorscale = True,
                          reversescale=True,
                          colorscale = "iceFire",
                          colorbar = dict(title = "arasştırma puani"))

veri_ = [world_map]

yerlesim = go.Layout(title = "ulkelerin toplam arastirma puanlari",
                     geo = dict(showframe = True, 
                                showlakes = False,
                                showcoastlines = True,
                                projection = dict(type = "natural earth")))

fig = dict(data = veri_, layout = yerlesim)

plot(fig, filename = "plotly_world_map.html")
