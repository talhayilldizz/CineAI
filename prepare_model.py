import pandas as pd
import pickle
import json
import os
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def train_and_save_model():
    base_dir=os.path.dirname(os.path.abspath(__file__))
    csv_path=os.path.join(base_dir,'app','data','clean_tmdb_movies.csv')
    movies_pkl_path=os.path.join(base_dir,'app','data','movie_list.pkl')
    sim_pkl_path=os.path.join(base_dir,'app','data','similarity.pkl')

    print("Veri Okunuyor..")
    if not os.path.exists(csv_path):
        print("Dosya Bulunamadı..")
        return
    
    movies_df=pd.read_csv(csv_path)

    print("Vektörleştirme Yapılıyor Bu İşlen Uzun Sürebilir...")
    cv=TfidfVectorizer(
        max_features=5000,
        stop_words='english',
        lowercase=True
    )

    vectors=cv.fit_transform(movies_df["tags"]).toarray()

    print("Cosine Similarity hesaplanıyor...")
    similarity=cosine_similarity(vectors)
    print(f"Cosine Similarity: {similarity.shape}")

    print("Modeller Kaydediliyor..")
    pickle.dump(movies_df,open(movies_pkl_path,"wb"))
    pickle.dump(similarity,open(sim_pkl_path,"wb"))

    print("İşlem Tamam..")

if __name__ == "__main__":
    train_and_save_model()