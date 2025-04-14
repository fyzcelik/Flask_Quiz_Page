# 🧠 Flask Quiz Page

Bu proje, **Flask** ile hazırlanmış basit ama işlevsel bir sınav (quiz) uygulamasıdır.  
Kullanıcılar giriş yaptıktan sonra 5 soruluk sınava katılır, sistem doğru cevaplara göre puanlarını hesaplar ve veritabanına kaydeder.

---

## 🚀 Özellikler

✅ Kullanıcı adıyla giriş yapma  
✅ 5 sabit soruluk sınav  
✅ Doğru cevaplara göre puan hesaplama  
✅ Kullanıcının:
- Son skoru  
- En yüksek skoru  
✅ Tüm kullanıcılar arasında en yüksek skor gösterimi  
✅ SQLite + SQLAlchemy ile veritabanı yönetimi  
✅ Bootstrap ile sade ve şık arayüz  
✅ Mobil uyumlu sayfalar  
✅ PythonAnywhere üzerinden yayında!

---

## 🌐 Canlı Uygulama

👉 [https://feyzacelik.pythonanywhere.com](https://feyzacelik.pythonanywhere.com)

---

## ⚙️ Kurulum

### 💻 Bilgisayarınızda çalıştırmak için:

```bash
# Sanal ortam oluştur (isteğe bağlı ama tavsiye edilir)
python -m venv venv
source venv/bin/activate  # Windows'ta: venv\Scripts\activate

# Gerekli paketleri yükle
pip install -r requirements.txt

# Uygulamayı başlat
python main.py
