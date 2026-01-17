# CineAI – Film Öneri Sistemi

CineAI, **içerik tabanlı** bir film öneri sistemidir. Kullanıcının seçtiği filme göre, film açıklamaları, türler ve anahtar kelimeler üzerinden benzer filmleri önerir.

Bu projede **TF-IDF + Cosine Similarity** kullanılarak filmler arasındaki benzerlik hesaplanmıştır.

---

## Kullanılan Teknolojiler

* Python
* Pandas
* Scikit-learn
* Flask
* HTML / CSS
* Pickle

---

## Veri Seti

Projede kullanılan veri seti Kaggle üzerinden alınmıştır:

**TMDB Movie Metadata Dataset**
[https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Veri seti projede temizlenmiş ve işlenmiş haliyle kullanılmıştır.

---

## Model Mantığı

1. Film bilgileri birleştirilerek **tags** adlı metinsel bir özellik oluşturulur.
2. Bu metinler:

   * `CountVectorizer` veya
   * `TfidfVectorizer`
     kullanılarak sayısal vektörlere dönüştürülür.
3. Filmler arasındaki benzerlik **Cosine Similarity** ile hesaplanır.
4. En yüksek benzerliğe sahip 5 film film kullanıcıya önerilir.

---

* `.pkl` dosyaları **çok büyük boyutlu** olabilir (yüzlerce MB).
* GitHub büyük dosyalar için uygun değildir.
* Bu dosyalar **yeniden üretilebilir** dosyalardır.
Bu nedenle `.pkl` dosyaları `.gitignore` içine eklenmiştir.

---

## Model Dosyalarını Nasıl Oluştururum?

Aşağıdaki script çalıştırılarak `.pkl` dosyaları otomatik olarak oluşturulur:

```bash
python prepare_model.py
```

Bu işlem:

* Veri setini okur
* Vektörleştirme yapar
* Cosine similarity hesaplar
* Gerekli `.pkl` dosyalarını üretir

---

## Projeyi Çalıştırma

```bash
pip install pandas numpy scikit-learn flask python-dotenv openai
python run.py
```

## Notlar

* Veri seti ve model dosyaları **ilk kurulumda manuel olarak oluşturulmalıdır**.
---

TF-IDF
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/18901c9d-b808-4ced-90e1-5c77c691590c" />

Cosine Similarity
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/df4a5238-9dfe-45c8-9288-436591afbbf0" />

