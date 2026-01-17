<img width="200" height="200" alt="logo" src="https://github.com/user-attachments/assets/8f4b52dd-9ff1-4f7b-adf8-8ea54b32c950" />


# CineAI – Film Öneri Sistemi

CineAI, **içerik tabanlı (content-based)** çalışan ve **Flask** altyapısı ile web arayüzüne sahip olan bir film öneri sistemidir. Kullanıcının seçtiği bir filme dayanarak; film açıklamaları, türler ve anahtar kelimeler üzerinden en benzer filmleri listeler.

Bu projede **Count Vectorizer + Cosine Similarity** algoritmaları kullanılmış ve sonuçlar modern bir web arayüzü üzerinden sunulmuştur.

Ayrıca sistem, öneri sonuçlarını daha anlaşılır hale getirmek için GPT destekli açıklayıcı yorumlama özelliğine sahiptir.

---

## Kullanılan Teknolojiler

* Python
* Pandas
* Scikit-learn
* Flask
* OpenAI GPT API
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

   * `CountVectorizer`
     kullanılarak sayısal vektörlere dönüştürülür.
3. Filmler arasındaki benzerlik **Cosine Similarity** ile hesaplanır.
4. En yüksek benzerliğe sahip 5 film film kullanıcıya önerilir.

---

* `.pkl` dosyaları **çok büyük boyutlu** olabilir (yüzlerce MB).
* GitHub büyük dosyalar için uygun değildir.
* Bu dosyalar **yeniden üretilebilir** dosyalardır.
Bu nedenle `.pkl` dosyaları `.gitignore` içine eklenmiştir.

---

## GPT Entegrasyonu

CineAI projesinde, öneri sistemini daha etkileşimli ve anlaşılır hale getirmek amacıyla GPT entegrasyonu bulunmaktadır.

Öneri süreci şu şekilde ilerler:

1-Kullanıcı bir film seçer

2-Sistem, içerik tabanlı algoritma ile benzer filmleri listeler

3-Kullanıcı, önerilen filmlerden herhangi birine tıkladığında seçilen film ile başlangıçta izlenen film arasındaki benzerlik,GPT modeli tarafından doğal dilde yorumlanır

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

Cosine Similarity

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/df4a5238-9dfe-45c8-9288-436591afbbf0" />

