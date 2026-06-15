import asyncio
import json
from mcp.server.fastmcp import FastMCP
from pydantic import Field

from yargitay_karar_scraper.scraper import YargitayClient, SearchCriteria

# MCP Sunucusunu başlatıyoruz
mcp = FastMCP("Yargitay Karar Arama Sunucusu")

@mcp.tool()
async def search_cases(
    kelime: str = Field(None, description="Aranacak kelime veya kelime öbeği"),
    daire: str = Field(None, description="İlgili daire (Ör: 1, 2, Ceza, Hukuk vb.)"),
    esas_no: str = Field(None, description="Esas numarası"),
    karar_no: str = Field(None, description="Karar numarası")
) -> str:
    """
    Yargıtay kararlarında arama yapar ve sonuç listesini döndürür.
    Bu listeye dayanarak spesifik kararların detayını okumak isterseniz 'get_case_detail' aracını çağırın.
    """
    criteria = SearchCriteria(
        kelime=kelime,
        daire=daire,
        esas_no=esas_no,
        karar_no=karar_no
    )
    
    client = YargitayClient()
    response = await client.search(criteria)
    
    if response.error:
        return f"Arama sırasında hata oluştu: {response.error}"
        
    if not response.results:
        return "Belirtilen kriterlere uygun sonuç bulunamadı."
        
    output = f"Toplam {response.total_count} sonuç bulundu:\n\n"
    
    for case in response.results:
        output += f"ID: {case.id}\n"
        output += f"Daire: {case.daire}\n"
        output += f"Esas/Karar: {case.esas_no} / {case.karar_no}\n"
        output += f"Tarih: {case.tarih}\n"
        output += f"Özet: {case.ozet}\n"
        output += "-" * 40 + "\n"
        
    return output

@mcp.tool()
async def get_case_detail(
    document_id: str = Field(..., description="Arama sonuçlarından elde edilen karar doküman ID'si")
) -> str:
    """
    Belirli bir Yargıtay kararının detaylı metnini veya tam içeriğini getirir.
    """
    client = YargitayClient()
    response = await client.get_document(document_id)
    
    if response.error:
        return f"Karar detayı getirilirken hata oluştu: {response.error}"
        
    return f"Karar ID: {response.id}\n\n{response.icerik}"

def main():
    """MCP Sunucusunu ayağa kaldıran ana fonksiyon."""
    # FastMCP otomatik olarak stdio transportunu kullanır
    mcp.run()

if __name__ == "__main__":
    main()
