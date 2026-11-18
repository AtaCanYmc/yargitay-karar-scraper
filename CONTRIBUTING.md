# Katkı Kılavuzu (Contributing Guide)

Bu belge, `yargitay-karar-scraper` projesine kod, hata bildirimi veya dokümantasyon katkısında bulunacak geliştiriciler için temel kuralları ve iş akışını açıklar.

---

## 1. Geliştirme Ortamı Kurulumu

Projeyi yerel ortamınızda çalıştırmak ve bağımlılıkları yüklemek için aşağıdaki adımları izleyin:

```bash
# Depoyu klonlayın
git clone https://github.com/AtaCanYmc/yargitay-karar-scraper.git
cd yargitay-karar-scraper

# Sanal ortam oluşturun ve aktif edin
python3 -m venv .venv
source .venv/bin/activate  # Windows için: .venv\Scripts\activate

# Projeyi düzenlenebilir modda test bağımlılıklarıyla birlikte kurun
pip install --upgrade pip
pip install -e .
pip install flake8 pytest pytest-asyncio
```

---

## 2. Kodlama ve Kalite Standartları

Tüm katkılar aşağıdaki kalite kontrollerinden geçmelidir:

### A. Linter ve Biçimlendirme

Proje `flake8` kurallarına uyar. PR açmadan önce linter kontrolünün sıfır hata ile tamamlandığından emin olun:

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

### B. Birim Testler

Eklenen yeni özellikler veya hata düzeltmeleri için `tests/` dizini altına asenkron birim testleri eklenmelidir. Test paketini çalıştırmak için:

```bash
pytest
```

### C. Güvenlik ve Ağ Hijyeni

- Harici HTTPS isteklerinde TLS sertifika doğrulaması (`verify=True`) korunmalıdır.
- Depoya `.env`, kimlik bilgisi veya geçici test dosyaları commit edilmemelidir.

---

## 3. Git İletisi Kuralları (Conventional Commits)

Commit iletileri [Conventional Commits](https://www.conventionalcommits.org/) standardına uygun olmalıdır.

Örnek format:
`<tip>(<kapsam>): <kısa ve emir kipiyle açıklama>`

Kullanılan tipler:
- `feat`: Yeni bir kullanıcı özelliği veya API yeteneği.
- `fix`: Bir hata veya güvenlik zafiyeti düzeltmesi.
- `docs`: Yalnızca dokümantasyon değişiklikleri.
- `refactor`: Davranış değiştirmeyen kod iyileştirmeleri.
- `test`: Test ekleme veya mevcut testleri güncelleme.
- `chore`: Bağımlılık, CI veya derleme betiği güncellemeleri.

Örnek:
`fix(scraper): handle html entities when parsing case content`

---

## 4. Dal (Branch) İsimlendirme ve Çekme İsteği (PR) Süreci

1. Yeni bir çalışma dalı oluşturun:
   - Özellik için: `feat/aciklama`
   - Düzeltme için: `fix/aciklama`
2. Değişikliklerinizi küçük, bağımsız ve mantıksal commit'lere bölün.
3. PR açmadan önce yerel ortamınızda testleri ve linter'ı çalıştırın.
4. PR açıklamasında yapılan değişiklikleri ve yerel doğrulama komutlarını belirtin.
