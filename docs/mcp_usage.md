# Yargıtay Karar Arama MCP Sunucusu Kılavuzu

Model Context Protocol (MCP), Yapay Zeka istemcilerinin dış araçlar ve veri kaynakları ile standart JSON-RPC üzerinden haberleşmesini sağlayan açık protokoldür. Bu paket, Yargıtay kararlarını LLM ajanlarının doğrudan sorgulamasına imkan veren yerel bir stdio MCP sunucusu sağlar.

---

## Sunucuyu Başlatma

Sunucu, Python paketinin giriş noktası olan `yargitay-karar-mcp` komutuyla stdio üzerinden çalışır:

```bash
yargitay-karar-mcp
```

Bu süreç terminale doğrudan okunabilir metin basmaz. JSON-RPC protokolü üzerinden stdin ve stdout kanallarını dinler.

---

## Sunulan Araçlar (Tools)

Sunucu iki ana araç sunar:

### 1. `search_cases`

Yargıtay karar arama servisinde detaylı kriterlere göre sorgulama yapar ve eşleşen kararları özet metin halinde döndürür.

#### Girdi Parametreleri

| Parametre | Tip | Varsayılan | Açıklama |
| --- | --- | --- | --- |
| `kelime` | `string` | `""` | Aranacak kelime veya kelime öbeği. |
| `daire` | `string` | `""` | Yargıtay dairesi (ör. `1. Ceza Dairesi`). |
| `baslangic_tarihi` | `string` | `""` | Başlangıç tarihi (`GG.AA.YYYY`). |
| `bitis_tarihi` | `string` | `""` | Bitiş tarihi (`GG.AA.YYYY`). |
| `esas_yil` | `string` | `""` | Esas dosya yılı. |
| `karar_yil` | `string` | `""` | Karar yılı. |
| `siralama` | `string` | `"3"` | Sıralama ölçütü kodu. |
| `siralama_direction` | `string` | `"asc"` | Sıralama yönü (`asc` veya `desc`). |
| `page_size` | `integer` | `10` | Sayfa başı kayıt sayısı. |
| `page_number` | `integer` | `1` | Sayfa numarası. |

#### Çıktı Formatı

Her karar kaydı için `ID`, `Daire`, `Esas/Karar`, `Tarih` ve `Özet` alanlarını içeren yapılandırılmış metin bloğu döndürülür.

---

### 2. `get_case_detail`

Verilen karar ID numarasına ait kararın tam metnini döndürür. HTML etiketleri temizlenmiş ve karakter kodlaması çözülmüş metin içerir.

#### Girdi Parametreleri

| Parametre | Tip | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `document_id` | `string` | Evet | Karar doküman ID numarası. |

#### Çıktı Formatı

`Karar ID: <id>\n\n<tam metin>` biçiminde düz metin döndürülür.

---

## İstemci Entegrasyonları

### Claude Desktop Yapılandırması

Claude Desktop uygulamasının MCP sunucusunu tanıması için işletim sisteminize uygun yapılandırma dosyasını düzenleyin:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Yapılandırma dosyasına aşağıdaki sunucu tanımını ekleyin:

```json
{
  "mcpServers": {
    "yargitay_kararlar": {
      "command": "yargitay-karar-mcp",
      "args": []
    }
  }
}
```

Eğer komut global PATH içinde bulunamıyorsa sanal ortamdaki mutlak çalıştırılabilir dosya yolunu belirtin:

```json
{
  "mcpServers": {
    "yargitay_kararlar": {
      "command": "/Users/kullanici/proje/.venv/bin/yargitay-karar-mcp",
      "args": []
    }
  }
}
```

---

## Örnek Ajan İstemleri

Entegrasyon tamamlandıktan sonra LLM istemcinize doğal dille sorgu verebilirsiniz:

1. **Arama İstemi:**
   > "Yargıtay 4. Hukuk Dairesinin 2022 yılındaki manevi tazminat kararlarından ilk 5 tanesini listeler misin?"
   *Ajan `search_cases` aracını `daire="4. Hukuk Dairesi"`, `karar_yil="2022"`, `kelime="manevi tazminat"`, `page_size=5` argümanlarıyla çağırır.*

2. **Detay ve İnceleme İstemi:**
   > "Yukarıdaki listede yer alan 264811900 ID'li kararın tam metnini çekip bozma gerekçesini açıklar mısın?"
   *Ajan `get_case_detail` aracını `document_id="264811900"` argümanıyla çağırır ve dönen içtihadı analiz eder.*
