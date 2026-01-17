import pickle
import os
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv

class MovieReccomender:
    #Program başladığında gerekli dosyaları belleğe alır
    def __init__(self):
        base_dir=os.path.dirname(os.path.abspath(__file__))
        movie_path=os.path.join(base_dir,'data','movie_list.pkl')
        sim_path=os.path.join(base_dir,'data','similarity.pkl')

        print("Modeller Yükleniyor..")
        self.movies=pickle.load(open(movie_path,"rb"))
        self.similarity=pickle.load(open(sim_path,"rb"))
        print("Modeller Yüklendi..")

        #Gpt api anahtarı
        load_dotenv()
        api_key=os.getenv("OPENAI_API_KEY")
        if api_key:
            print("Api Anahtarı Bulundu..")
            self.client=OpenAI(api_key=api_key)
        else:
            print("Api Anahtarı Bulunmadı.. ")
            self.client=None


    #Öneri yapacağımız kısım
    def recommend(self,movie_title):

        #Kullanıcının girdiği film yoksa boş döndürür
        if movie_title not in self.movies['original_title'].values:
            return []
        
        movie_index=self.movies[self.movies["original_title"] == movie_title].index[0]
        distances=self.similarity[movie_index]  #seçilen filmin diğer filmlere benzerliği

        #en benzer 5 film
        movies_list=sorted(
            list(enumerate(distances)),
            reverse=True,
            key= lambda x:x[1])[1:6]

        recommendations=[]
        for i in movies_list:
            title=self.movies.iloc[i[0]].original_title
            recommendations.append({'title': title})

        return recommendations
    
    def get_gpt_response(self,user_movie,recommend_movie):
        if not self.client:
            return "Api Anahtarı Yok"
        
        prompt=f"""
            Kullanıcı '{user_movie}' filmini izlemiş ve beğenmiş.
            Kullanıcıya '{recommend_movie}' filmini önerdik.
            Sinema uzmanı gibi davran. Bu iki filmin ortak noktalarına (konu, yönetmen vs) değinerek,
            kullanıcıya '{recommend_movie}' filmini neden izlemesi gerektiğini bir kaç cümle ile açıkla.
        """

        try:
            response=self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Hata: {str(e)}"


if __name__ == "__main__":
    recommender = MovieReccomender()
    print(f"Önerilen Filmler:\n{recommender.recommend('Cars')}\n")
    print(f"AI YORUMU:\n{recommender.get_gpt_response('Cars','Herbie Fully Loaded')}")




