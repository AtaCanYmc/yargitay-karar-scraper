# Yargıtay Karar Arama MCP Sunucusu Kullanımı

Model Context Protocol (MCP), Claude ve benzeri Yapay Zeka (LLM) asistanlarının dış sistemlere entegre olmasını sağlayan açık bir standarttır. Bu paket sayesinde LLM'nize doğrudan Yargıtay kararlarında arama yapma ve okuma yeteneği kazandırabilirsiniz.

## 1. MCP Sunucusunu Başlatmak

Komut satırından standart girdi/çıktı (stdio) üzerinden MCP sunucusunu ayağa kaldırmak çok basittir:

```bash
yargitay-karar-mcp
```
*(Bu komut arka planda çalışıp standart JSON-RPC protokolü üzerinden dinlemeye başlar. İnsanların doğrudan okuması için değil, LLM istemcileri için tasarlanmıştır.)*

## 2. Claude Desktop ile Entegrasyon

Claude Desktop uygulamasına bu aracı öğretmek için konfigürasyon dosyanıza eklemeniz gereklidir.

**MacOS için yapılandırma dosyası yolu:** 
`~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows için yapılandırma dosyası yolu:**
`%APPDATA%\Claude\claude_desktop_config.json`

Konfigürasyon dosyasına şu bloğu ekleyin (eğer dosya yoksa yeni bir JSON olarak oluşturun):

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

*Not: Eğer `yargitay-karar-mcp` komutu ortam değişkenlerinizde (PATH) bulunamıyorsa, "command" kısmına python sanal ortamınızdaki (venv) tam yolunu yazabilirsiniz.*

Claude Desktop uygulamasını yeniden başlattığınızda sistem bu araçları (Tools) otomatik tanıyacaktır.

## 3. Claude ile Örnek Etkileşimler (Promptlar)

Kurulum tamamlandıktan sonra Claude ile sohbet ederken aşağıdaki gibi komutlar verebilirsiniz. Claude otomatik olarak arka planda MCP sunucunuza bağlanacak, arama yapacak ve sonucu size özetleyecektir.

**Örnek Prompt 1 (Detaylı Arama):**
> "Bana Yargıtay 1. Ceza Dairesinin 2018 yılında vermiş olduğu 'kasten adam öldürme' ile ilgili kararları bulur musun?"
*(Claude otomatik olarak `search_cases` aracını çağırıp daire ve karar_yil filtrelerini kullanır)*

**Örnek Prompt 2 (Metin İncelemesi):**
> "Az önce bulduğun '415233000' ID'li kararın tam metnini oku ve bana bu kararda sanığın neden beraat ettiğini açıkla."
*(Claude otomatik olarak `get_case_detail` aracını çağırır ve HTML'den arındırılmış saf metni okuyarak analiz yapar)*
