# Yargıtay Karar Arama CLI Kullanım Kılavuzu

`yargitay-karar-cli`, Yargıtay Karar Arama sistemine terminal üzerinden erişim sağlayan komut satırı arayüzüdür.

---

## Kurulum ve Başlangıç

Paket kurulduktan sonra CLI komutları doğrudan terminalden çalıştırılabilir:

```bash
# Geliştirici modunda kurulum
pip install -e .

# Genel yardım ekranı
yargitay-karar-cli --help
```

---

## Komutlar ve Seçenekler

### 1. Basit Arama (`search`)

Tek bir kelime veya kelime öbeği üzerinden arama yapar.

```bash
yargitay-karar-cli search --kelime "hırsızlık" --page-size 10 --page-number 1
```

#### Parametreler

| Parametre | Tip | Zorunlu | Varsayılan | Açıklama |
| --- | --- | --- | --- | --- |
| `--kelime` | Metin | Evet | - | Aranacak anahtar kelime veya kelime öbeği. |
| `--page-size` | Tamsayı | Hayır | `10` | Sayfa başına listelenecek karar sayısı. |
| `--page-number` | Tamsayı | Hayır | `1` | Getirilecek sayfa numarası. |

---

### 2. Gelişmiş Arama (`detailed-search`)

Daire, tarih aralığı, esas/karar yılları ve sıralama ölçütlerine göre filtreleme yapar.

```bash
yargitay-karar-cli detailed-search \
  --kelime "dolandırıcılık" \
  --daire "11. Ceza Dairesi" \
  --karar-yil "2021" \
  --siralama "3" \
  --siralama-direction "desc" \
  --page-size 10
```

#### Parametreler

| Parametre | Tip | Zorunlu | Varsayılan | Açıklama |
| --- | --- | --- | --- | --- |
| `--kelime` | Metin | Hayır | `""` | Aranacak anahtar kelime. |
| `--daire` | Metin | Hayır | `""` | İlgili Yargıtay dairesi (ör. `1. Ceza Dairesi`, `4. Hukuk Dairesi`). |
| `--baslangic-tarihi` | Metin | Hayır | `""` | Karar başlangıç tarihi (`GG.AA.YYYY`). |
| `--bitis-tarihi` | Metin | Hayır | `""` | Karar bitiş tarihi (`GG.AA.YYYY`). |
| `--esas-yil` | Metin | Hayır | `""` | Esas dosya yılı (ör. `2020`). |
| `--karar-yil` | Metin | Hayır | `""` | Karar yılı (ör. `2021`). |
| `--siralama` | Metin | Hayır | `"3"` | Sıralama ölçütü kodu (`3`: Karar Tarihi). |
| `--siralama-direction` | Metin | Hayır | `"asc"` | Sıralama yönü (`asc` veya `desc`). |
| `--page-size` | Tamsayı | Hayır | `10` | Sayfa başına listelenecek kayıt sayısı. |
| `--page-number` | Tamsayı | Hayır | `1` | Getirilecek sayfa numarası. |

---

### 3. Karar Detayı Görüntüleme (`detail`)

Arama çıktısında listelenen karar ID numarasını kullanarak kararın tam metnini terminalde Rich paneli içinde gösterir. Karar metni HTML etiketlerinden arındırılmış ve karakter kodlaması çözülmüş olarak sunulur.

```bash
yargitay-karar-cli detail --id "120109100"
```

#### Parametreler

| Parametre | Tip | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `--id` | Metin | Evet | Görüntülenecek kararın Yargıtay sistemindeki benzersiz doküman ID değeri. |

---

## Hata Yönetimi ve Çıktı Formatı

- Ağ bağlantısı veya sunucu kaynaklı hatalarda hata mesajı standart hata kanalına kırmızı renkle basılır.
- Arama sonuçları bulunamadığında sarı bilgilendirme mesajı verilir.
- Çıktılar ANSI destekli terminallerde otomatik olarak boyutlandırılan Rich tabloları halinde gösterilir.
