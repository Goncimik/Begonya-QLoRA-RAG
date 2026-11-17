# 🌺 Begonya | QLoRA & RAG-Powered AI Assistant

**Begonvil Otel için Yapay Zekâ Destekli Misafir Hizmetleri Asistanı**

Tech İstanbul Uygulamalı Yapay Zekâ Bootcamp kapsamında geliştirilen Begonya, kurgusal bir otelin misafir hizmetlerini desteklemek amacıyla büyük dil modeli ince ayarı, bilgi erişimi ve araç kullanan yapay zekâ ajanlarını bir araya getiren uygulamalı bir bitirme projesidir.

## 🎯 Projenin Amacı

Begonya; Türkçe misafir sorularını yanıtlamak, otel rehberinden bilgi edinmek ve tanımlanan araçlar aracılığıyla oda, konaklama ve misafir hizmetleriyle ilgili işlemleri desteklemek üzere geliştirilmiştir.

## 🧠 Kullanılan Teknolojiler

| Teknoloji | Kullanım amacı |
|---|---|
| Qwen2.5-1.5B-Instruct | Taban dil modeli |
| QLoRA / PEFT | Parametre verimli ince ayar |
| Hugging Face Transformers | Model ve eğitim altyapısı |
| ChromaDB | Vektör tabanlı bilgi erişimi |
| RAG | Otel rehberine dayalı yanıt üretimi |
| Python | Uygulama ve ajan araçları |
| Gradio | Web arayüzü |
| GGUF / llama.cpp | CPU üzerinde model çalıştırma |
| TF-IDF | CPU uygulamasında belge erişimi |

## ⚙️ Sistem Mimarisi

Proje iki uygulama yaklaşımı içerir:

**1. Google Colab ortamı**

QLoRA ile model ince ayarı, Chroma tabanlı RAG, araç kullanan ajan ve Gradio arayüzü.

**2. CPU tabanlı uygulama**

GGUF model, llama.cpp, TF-IDF tabanlı bilgi erişimi ve Gradio arayüzü.

Bu iki yaklaşımın bilgi erişim mekanizmaları farklıdır.

## 📂 Proje Dosyaları

- `🌺Begonya🌺.ipynb` — Eğitim, deneyler ve değerlendirmeler
- `space/app.py` — Uygulama arayüzü
- `space/proje.py` — Proje yapılandırması
- `space/araclar.py` — Ajan araçları
- `space/rehber.pdf` — Otel bilgi rehberi
- `space/odalar.csv` — Oda bilgileri
- `space/test_sorulari.csv` — Test soruları
- `space/requirements.txt` — Uygulama bağımlılıkları

## 🤗 Hugging Face Kaynakları

- [Begonya-1.5B — Ana Model](https://huggingface.co/goncimik/Begonya-1.5B)
- [Begonya-1.5B-LoRA — Adaptör](https://huggingface.co/goncimik/Begonya-1.5B-LoRA)
- [Begonya-1.5B-GGUF — GGUF Modeli](https://huggingface.co/goncimik/Begonya-1.5B-GGUF)
- [Begonya Eğitim Verisi](https://huggingface.co/datasets/goncimik/Begonya-1.5B-veri)

## 📊 Deneyler ve Değerlendirme

Projede modelin ince ayar öncesi ve sonrası davranışları, RAG yanıtları ve araç kullanım performansı değerlendirilmiştir.

Deney sonuçları ve çalışma çıktıları Jupyter notebook içerisinde sunulmaktadır.

## ⚠️ Mevcut Sınırlılıklar

- Eğitim verileri sentetik olarak oluşturulmuştur.
- Değerlendirmeler sınırlı örneklem büyüklüklerine dayanmaktadır.
- Model bazı sorularda hatalı veya yetersiz yanıtlar üretebilmektedir.
- RAG sistemi her durumda doğru bilgi kullanımını garanti etmemektedir.
- Uygulamanın üretim ortamındaki güvenilirliği ayrıca doğrulanmalıdır.


## 📝 Medium | Geliştirme Hikâyesi

[medium](https://medium.com/@goncacomert/bir-dil-modelini-e%C4%9Fitmek-yetiyor-mu-qlora-rag-ve-begonya-deneyimi-1749ebcd69d7)

*Begonya, eğitim ve araştırma amaçlı geliştirilmiş bir yapay zekâ prototipidir.*


## 🚀 Gelecek Geliştirmeler

Projenin sonraki sürümlerinde yanıt doğruluğunun artırılması, RAG mimarisinin iyileştirilmesi, daha kapsamlı değerlendirmeler ve uygulama performansının geliştirilmesi hedeflenmektedir.

---
Yeni projelerde, yeni deneylerde ve bazen de beklenmedik hatalarda görüşmek üzere! 🌺

Mutlu kodlamalar! 💻✨
