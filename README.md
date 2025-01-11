# **Altyazı Uyum Aracı**

### **Proje Açıklaması**
**Altyazı Uyum Aracı**, Türkçe altyazı dosyalarında yaşanan karakter kodlama sorunlarını düzeltmek için geliştirilmiş bir araçtır. Bu araç, altyazı dosyalarını (SRT formatında) **ISO-8859-9** karakter kodlamasından **UTF-8** formatına dönüştürerek Türkçe karakterlerin düzgün görüntülenmesini sağlar.

---

## **Özellikler**
- **Kullanıcı Dostu Arayüz**: Sade ve şık bir arayüzle kullanıcıların kolayca işlem yapmasına olanak tanır.
- **Hızlı Dönüşüm**: SRT dosyalarını UTF-8 formatına dönüştürerek Türkçe karakter sorunlarını çözer.
- **CMD Penceresi Yok**: EXE olarak çalıştırıldığında arka planda terminal açılmaz.
- **Taşınabilirlik**: Python dosyası veya EXE formatıyla kolayca kullanılabilir.

---

## **Dosyalar**
- **altyazi.py**: Python kaynak kodu.
- **Altyazı_Uyum_Aracı.exe**: Masaüstü uygulaması olarak çalıştırılabilir dosya.
- **README.md**: Proje hakkında bilgi.

---

## **Kurulum**
### Python ile Çalıştırma
1. **Gerekli Bağımlılıkları Yükleyin**:
   ```bash
   pip install tk
   ```
2. **altyazi.py** dosyasını indirin.
3. Terminal veya Komut İstemcisinde şu komutu çalıştırarak programı başlatın:
   ```bash
   python altyazi.py
   ```

### EXE Olarak Çalıştırma
1. **Altyazı_Uyum_Aracı.exe** dosyasını indirin.
2. Dosyayı çift tıklayarak çalıştırın.

---

## **Kullanım**
1. **Girdi Dosyasını Seçin**:
   - "Dosya Seç" butonuna tıklayarak dönüştürmek istediğiniz SRT dosyasını seçin.
2. **Dönüştürme**:
   - "Dönüştür" butonuna tıklayın.
   - Dönüştürülen dosya, seçtiğiniz dosyayla aynı klasöre `*_utf8.srt` adıyla kaydedilecektir.

---

## **Geliştirme**
Projeyi geliştirmek veya katkıda bulunmak için aşağıdaki adımları izleyebilirsiniz:

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
5. Bir **Pull Request** gönderin.

---

## **Lisans**
Bu proje **MIT Lisansı** ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.
