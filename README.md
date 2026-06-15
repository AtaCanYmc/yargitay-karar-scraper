# Yargıtay Karar Arama Scraper & MCP Sunucusu

Yargıtay Karar Arama sitesinden veri çeken, bunu bir CLI üzerinden terminalde sunan ve bir MCP (Model Context Protocol) sunucusu olarak büyük dil modelleri ile etkileşime açan Python paketi.

## Özellikler

- **Modüler Scraper:** `httpx` ve `pydantic` kullanılarak yazılmış temiz, nesne yönelimli ve tip güvenli scraper çekirdeği.
- **CLI:** `click` ve `rich` tabanlı, kullanıcı dostu komut satırı arayüzü.
- **MCP Sunucusu:** LLM'lerin (Claude vb.) kullanabilmesi için standart `mcp` arayüzü sağlayan sunucu.

## Kurulum

Projeyi klonladıktan sonra dizine girin ve `pip` ile kurun:

```bash
git clone <repo-url>
cd yargitay-karar-scraper
pip install -e .
```

## Kullanım

### CLI Kullanımı

CLI aracını `yargitay-karar-cli` komutu ile kullanabilirsiniz.

Arama yapmak için:
```bash
yargitay-karar-cli search --kelime "hırsızlık" --daire "1"
```

Bir kararın detayını ID ile çekmek için:
```bash
yargitay-karar-cli detail --id "DOKUMAN_ID"
```

### MCP Sunucusu Olarak Kullanım

Aşağıdaki komut MCP sunucusunu ayağa kaldırır ve LLM'lerin `search_cases` ile `get_case_detail` araçlarını kullanabilmesini sağlar:

```bash
yargitay-karar-mcp
```

Bunu Claude Desktop veya başka bir MCP destekleyen istemcinin `mcp_servers` konfigürasyonuna şu şekilde ekleyebilirsiniz:

```json
{
  "yargitay_scraper": {
    "command": "yargitay-karar-mcp",
    "args": []
  }
}
```
