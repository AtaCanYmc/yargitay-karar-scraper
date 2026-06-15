# Yargıtay Karar Arama CLI Kullanım Örnekleri

Bu dokümanda `yargitay-karar-cli` komut satırı aracının nasıl kullanılacağına dair örnekler yer almaktadır.

Proje bağımlılıklarını kurduktan sonra (`pip install -e .` çalıştırarak) terminalinizde doğrudan `yargitay-karar-cli` komutunu kullanabilirsiniz.

## 1. Basit Arama (`search`)

Bu komut, bir kelime öbeği üzerinden arama yapmanızı ve sayfalandırma seçeneklerini kontrol etmenizi sağlar.

**Örnek:** Sadece "hırsızlık" kelimesi geçen kararları aramak:
```bash
yargitay-karar-cli search --kelime "hırsızlık"
```

**Örnek:** Sayfa başı 5 kayıt getirecek şekilde, 2. sayfadaki kararları aramak:
```bash
yargitay-karar-cli search --kelime "dolandırıcılık" --page-size 5 --page-number 2
```

## 2. Karar Detayı Okuma (`detail`)

Arama sonuçlarında (veya başka bir yerden) elde ettiğiniz Yargıtay Karar ID'si ile kararın saf metnini (HTML etiketlerinden arındırılmış haliyle) okuyabilirsiniz.

**Örnek:** ID'si `120109100` olan kararın metnini getirmek:
```bash
yargitay-karar-cli detail --id "120109100"
```

## Yardım (Help) Dokümantasyonu

Kullanabileceğiniz tüm alt komutları ve argümanları görmek için `--help` bayrağını ekleyin:

```bash
# Ana menü yardımı
yargitay-karar-cli --help

# Arama komutu yardımı
yargitay-karar-cli search --help

# Detay komutu yardımı
yargitay-karar-cli detail --help
```
