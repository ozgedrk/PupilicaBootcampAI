import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

# %% SCATTER PLOT


# boy vs kilo gorsellestirme

plt.figure()
sns.set_style("white")
sns.scatterplot(x = "boy", y = "kilo", data = veri )
plt.title("boy vs kilo")

# figure style
plt.figure()
sns.set_style("dark")
sns.scatterplot(x = "boy", y = "kilo", data = veri )
plt.title("boy vs kilo")

# figure style
plt.figure()
sns.set_style("darkgrid")
sns.scatterplot(x = "boy", y = "kilo", data = veri )
plt.title("boy vs kilo")

# figure style
plt.figure()
sns.set_style("whitegrid")
sns.scatterplot(x = "boy", y = "kilo", data = veri )
plt.title("boy vs kilo")


# boy vs kilo cinsiyet tiplerine gore 
plt.figure()
sns.scatterplot(x = "boy", y= "kilo", data = veri, hue = "cinsiyet")

# scatter plot with linear regression
plt.figure()
sns.regplot(x = "boy", y = "kilo", data = veri, marker = "+", scatter_kws = {"alpha":0.2})

# Renk paletleri
# boy vs kilo madalya tiplerine gore 
plt.figure()
sns.scatterplot(x = "boy", y= "kilo", data = veri, hue = "madalya", palette = "Set1")

# sezona gore boy ve kilo karsilastirmasi
plt.figure()
sns.scatterplot(x = "boy", y= "kilo", data = veri, hue = "sezon", palette = "Purples")
plt.title("Boy ve Kilo Dagilimi - Beyaz Izgara Tema")
plt.show()

# %% LINE PLOT

plt.figure()
sns.lineplot(x = "boy", y = "kilo", data = veri)

# Kategorik cizgi grafigi
plt.figure()
sns.lineplot(x = "boy", y = "kilo", data = veri, hue = "madalya")
 
# %% HISTOGRAM 


sns.displot(veri, x = "kilo")
sns.displot(veri, x = "kilo", hue = "cinsiyet")


# Col yazdigimiz zaman iki grafigi ayri ayri sekilde gosterir
sns.displot(veri, x = "kilo", col = "cinsiyet")


# Iki boyutlu histogram
sns.displot(veri, x = "kilo", y = "boy", kind = "kde", hue = "cinsiyet")

sns.displot(veri, x = "kilo", y = "boy", kind = "kde", hue = "sezon")

# %% BAR PLOT

sns.barplot(x = "madalya", y = "boy", data = veri)

sns.barplot(x = "madalya", y = "boy", data = veri, hue = "cinsiyet")

sns.catplot(x = "madalya", y = "boy", data = veri, hue = "cinsiyet", col = "sezon")

sns.catplot(x = "madalya", y = "boy", data = veri, hue = "cinsiyet", col = "sezon", kind = "bar")


# Spor vs Boy cinsiyet kategorisine ve sezon sutununa gore
sns.catplot(x = "spor", y = "boy", data = veri, hue = "cinsiyet", col = "sezon", kind = "bar")
plt.xticks(rotation = 90)

# %% BOX PLOT

plt.figure()
sns.boxplot(x = "sezon", y = "boy", data = veri)

plt.figure()
sns.boxplot(x = "sezon", y = "boy", data = veri, hue = "cinsiyet")

plt.figure()
veri_gecici = veri.loc[:,["yas", "boy", "kilo"]]
sns.boxplot(data = veri_gecici, orient = "h" )

sns.catplot(x = "sezon", y = "boy", hue = "cinsiyet", col = "madalya", data = veri, kind = "box")

# Cinsiyete vs Yas kategori = madalya columns = sezon
sns.catplot(x = "cinsiyet", y = "yas", hue = "madalya", col = "sezon", data = veri, kind = "box")

# %% HEATMAP

veri_gecici = veri.loc[:,["yas", "boy", "kilo"]]
correlation = veri_gecici.corr()

sns.heatmap(correlation, annot = True, fmt = ".2f", linewidths = 0.5)

# %% VIOLIN PLOT

sns.violinplot(x = "sezon", y = "boy", data = veri)

sns.violinplot(x = "sezon", y = "boy", data = veri, hue = "cinsiyet")

sns.violinplot(x = "sezon", y = "boy", data = veri, hue = "cinsiyet", split = True)

sns.catplot(x = "sezon", y = "boy", hue = "cinsiyet", col = "madalya", data = veri, kind = "violin", split = True)

# %% JOIN PLOT

sns.jointplot(data = veri, x = "kilo", y = "boy", hue = "sezon", kind = "kde")

g = sns.jointplot(data = veri, x = "kilo", y = "boy")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)

# %% PAIR PLOT

sns.pairplot(veri)

g = sns.PairGrid(veri)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde = True)
# %% COUNT PLOT 

sns.countplot(x = "sehir", data = veri)
plt.xticks(rotation = 90)

sns.countplot(x = "spor", data = veri)
plt.xticks(rotation = 90)