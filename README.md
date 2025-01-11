Aşağıda, GitHub'da proje açıklamanız (README) için uygun bir format sunuyorum. Açıklama, projenizin özelliklerini ve kullanımını net bir şekilde ifade eder.

---

# **Altyazı Uyum Aracı**

Bu proje, altyazı dosyalarını (SRT formatında) ISO-8859-9 karakter kodlamasından UTF-8 formatına dönüştüren bir masaüstü uygulamasıdır. Türkçe karakter problemleri yaşayan altyazı dosyalarını düzeltmek için basit bir çözüm sunar.

---

## **Özellikler**
- **Kullanıcı Dostu Arayüz**: Modern ve sade bir grafik arayüz sunar.
- **Karakter Kodlama Düzeltmesi**: ISO-8859-9 (Latin5) ile UTF-8 formatı arasında hızlı ve doğru dönüşüm sağlar.
- **Dosya İşleme**: Giriş dosyasını seçtikten sonra dönüştürülen dosyayı aynı klasöre kaydeder.
- **CMD'siz Çalıştırma**: Kullanıcı deneyimini artırmak için arka planda terminal penceresi açılmaz.

---

## **Gereksinimler**
- Python 3.7 veya üstü
- Gerekli kütüphaneler:
  - `tkinter` (Python ile birlikte gelir)
  - `codecs`

Opsiyonel:
- PyInstaller (EXE dosyası oluşturmak için)

---

## **Kurulum**
1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/altyazi-uyum-araci.git
   ```
2. Ana dizine gidin:
   ```bash
   cd altyazi-uyum-araci
   ```
3. Gerekli bağımlılıkları yükleyin (opsiyonel):
   ```bash
   pip install pyinstaller
   ```

---

## **Kullanım**
### Python Dosyasını Çalıştırma
1. Terminal veya Komut İstemcisinden aşağıdaki komutu çalıştırarak programı başlatabilirsiniz:
   ```bash
   python altyazı.py
   ```
2. Uygulama açıldığında:
   - "Dosya Seç" butonuyla dönüştürmek istediğiniz SRT dosyasını seçin.
   - "Dönüştür" butonuna tıklayın.
   - Dönüştürülen dosya, aynı klasöre `*_utf8.srt` uzantısıyla kaydedilecektir.

### EXE Olarak Çalıştırma
1. PyInstaller kullanarak EXE dosyasını oluşturun:
   ```bash
   pyinstaller --noconsole --onefile --icon="favicon.ico" altyazı.py
   ```
2. EXE dosyanız `dist` klasöründe oluşacaktır. Çift tıklayarak çalıştırabilirsiniz.
