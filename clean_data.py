import pandas as pd
import numpy as np
import os
import json

#Dosya Yolları
base_dir=os.path.dirname(os.path.abspath(__file__))
csv_path=os.path.join(base_dir,'app','data','tmdb_5000_movies.csv')
output_path=os.path.join(base_dir,'app','data','clean_tmdb_movies.csv')

print("Veri Okunuyor..")

movies_data=pd.read_csv(csv_path)
print("Veri Okundu..")
# print(movies_data.columns)

#verideki karmaşık json yapısını temizler
def clean_data(json_str):
    try:
        data=json.loads(json_str)
        names_list=[item['name'] for item in data]
        return " ".join(names_list)
        
    except:
        return ""


json_columns=[
    "genres","keywords"
]
for json_col in json_columns:
    movies_data[f"{json_col}_str"]=movies_data[json_col].apply(clean_data)

# print(movies_data[["keywords","keywords_str"]].head())

# print(f"Eksik Veriler\n{movies_data.isnull().sum()}")

#Özetlerde nan olmaması lazım
movies_data["overview"]=movies_data["overview"].fillna("") 

#modelin tek bakacağı yer oln tags kısmı
movies_data["tags"]=(
    movies_data["original_title"] + " " +
    movies_data["overview"] + " " +
    movies_data["genres_str"] + " "+
    movies_data["keywords_str"]
)

# print(f"Modelin Göreceği Örnek Veri:\n{movies_data.iloc[0]['tags'][:150]}...")
print("Temiz veri kaydediliyor..")

new_movies_data=movies_data[["id","original_title","tags","vote_average","release_date"]].copy()
new_movies_data.to_csv(output_path,index=False)
print("İşlem Başarılı..")


