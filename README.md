# Flask_Quiz_Page

Bu proje, Flask ile hazırlanmış basit ama işlevsel bir sınav (quiz) uygulamasıdır. Kullanıcılar giriş yaptıktan sonra 5 soruluk sınava katılır ve sistem puanlarını hesaplayarak kaydeder.

## Özellikler
- Kullanıcı adıyla giriş
- 5 soruluk quiz (sabit)
- Doğru cevaplara göre puan hesaplama
- Kullanıcının:
  - En son skoru
  - En yüksek skoru
- Tüm kullanıcılar arasında en yüksek skor
- Veritabanı: SQLite + SQLAlchemy
- Yayınlanabilir (PythonAnywhere uyumlu)
- Sayfalarda "Hazırlayan: Feyza Çelik" bilgisi

## Kurulum
```bash
pip install -r requirements.txt
python app.py

