# **Altyazı Uyum Aracı**
**Altyazı Uyum Aracı**, altyazı dosyalarındaki Türkçe karakter sorunlarını çözmek için geliştirilmiş bir masaüstü uygulamasıdır. Araç, SRT formatındaki altyazı dosyalarını **ISO-8859-9** karakter kodlamasından **UTF-8** formatına dönüştürerek Türkçe karakterlerin düzgün görüntülenmesini sağlar.

---

## **Hızlı Başlangıç**
### **1. EXE Dosyasını İndirin**
1. [**Altyazı_Uyum_Aracı.exe**](https://github.com/shenfurkan/AltyaziUyumAraci/raw/main/Altyazı_Uyum_Aracı.exe) dosyasını indirin.
2. Dosyayı indirdikten sonra çift tıklayarak çalıştırın.

> **Not**: Windows tarafından bilinmeyen bir kaynaktan indirilen dosyalar için güvenlik uyarısı alabilirsiniz. Bu durumda, "Güvenliği aş" seçeneğini kullanarak çalıştırabilirsiniz.

---

### **2. Kullanım**
1. **Dosya Seçimi**:
   - "Dosya Seç" butonuna tıklayarak dönüştürmek istediğiniz SRT dosyasını seçin.
2. **Dönüştürme**:
   - "Dönüştür" butonuna tıklayın.
   - Dönüştürülen dosya, seçtiğiniz dosyayla aynı klasöre `*_utf8.srt` adıyla kaydedilecektir.

---

## **Python ile Çalıştırma (Opsiyonel)**
Eğer kaynak koddan çalıştırmak isterseniz:

1. **Gerekli Bağımlılıkları Yükleyin**:
   ```bash
   pip install tk
   ```
2. **altyazi.py** dosyasını indirin.
3. Aşağıdaki komutu çalıştırarak uygulamayı başlatın:
   ```bash
   python altyazi.py
   ```

---

## **Özellikler**
- **Kolay Kullanım**: Kullanıcı dostu, modern bir grafik arayüz sunar.
- **Hızlı Dönüşüm**: ISO-8859-9 kodlamasından UTF-8 formatına dönüşümü saniyeler içinde tamamlar.
- **Taşınabilirlik**: EXE dosyası olarak kullanılabilir, Python kurulumuna gerek yoktur.

---

## **Katkıda Bulunma**
Projeye katkıda bulunmak için şu adımları izleyebilirsiniz:

1. Bu projeyi **fork** edin.
2. Yeni bir dal oluşturun:
   ```bash
   git checkout -b yeni-ozellik
   ```
3. Değişikliklerinizi işleyin:
   ```bash
   git commit -m "Yeni özellik eklendi"
   ```
4. Değişiklikleri gönderin:
   ```bash
   git push origin yeni-ozellik
   ```
5. Bir **Pull Request** gönderin
