import pandas as pd
import numpy as np



df= pd.read_csv("imdb.csv")


# 1.Dosya hakkında bilgiler.
result1= df

print(result1)

# 2.ilk 5 kaydı gösterin.
result2= df.head()

print(result2)

# 3.ilk 10 kaydı gösterin.

result3= df.head(10)

print(result3)

# 4.son 5 kaydı gösterin.
result4= df.tail()

print(result4)

# 5.son 10 kaydı gösterin.
result5= df.tail(10)

print(result5)

# 6.Sadece Title kolonu alın.
result6= df["Title"]

print(result6)

# 7.Sadece Title kolonu içeren ilk 5 kaydı alın.
result7= df["Title"].head()

print(result7)

# 8.Sadece Title ve Year kolonu içeren ilk 5 kaydı alın
result8= df[["Title","Year"]].head()

print(result8)

# 9.Sadece Title ve Year kolonu içeren son 7 kaydı alın.
result9= df[["Title","Year"]].tail(7)

print(result9)

# 10.Sadece Title ve Year kolonu içeren ikinci 5 kaydı alın.
result10 = df[5:][["Title","Year"]].head()

print(result10)

# 11.Sadece Title ve Year kolonu içeren ve
# imdb 2005 yıllı ve üstünde olan kayıtlardan ilk 50 kaydı alın.
result11= df[df["Year"]>= 2005][["Title","Year"]].head(50)

print(result11)

# 12.yaygın tarih 2014 ile 2015 arasında olan filmlerin isimilerin getiriniz.
result12= df[(df["Year"]>=2014) & (df["Year"]<=2015)][["Title","Year"]]

print("2014-2015 arasunda filmler:",result12)





