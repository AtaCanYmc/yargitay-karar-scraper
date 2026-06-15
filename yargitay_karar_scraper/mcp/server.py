from mcp.server.fastmcp import FastMCP
from pydantic import Field

from yargitay_karar_scraper.scraper import YargitayClient, DetailedSearchCriteria

# MCP Sunucusunu başlatıyoruz
mcp = FastMCP("Yargitay Karar Arama Sunucusu")


@mcp.tool()
async def search_cases(
        kelime: str = Field("", description="Aranacak kelime veya kelime öbeği"),
        daire: str = Field("", description="İlgili daire (Ör: 1, 2, Ceza, Hukuk vb.)"),
        baslangic_tarihi: str = Field("", description="Başlangıç Tarihi (GG.AA.YYYY)"),
        bitis_tarihi: str = Field("", description="Bitiş Tarihi (GG.AA.YYYY)"),
        esas_yil: str = Field("", description="Esas Yıl"),
        esas_ilk_sira_no: str = Field("", description="Esas İlk Sıra No"),
        esas_son_sira_no: str = Field("", description="Esas Son Sıra No"),
        karar_yil: str = Field("", description="Karar Yıl"),
        karar_ilk_sira_no: str = Field("", description="Karar İlk Sıra No"),
        karar_son_sira_no: str = Field("", description="Karar Son Sıra No"),
        siralama: str = Field("3", description="Sıralama türü"),
        siralama_direction: str = Field("asc", description="Sıralama yönü (asc/desc)"),
        page_size: int = Field(10, description="Sayfa başı kayıt sayısı"),
        page_number: int = Field(1, description="Sayfa numarası")
) -> str:
    """
    Yargıtay kararlarında detaylı arama yapar ve sonuç listesini döndürür.
    Bu listeye dayanarak spesifik kararların detayını okumak isterseniz 'get_case_detail' aracını çağırın.
    """
    criteria = DetailedSearchCriteria(
        kelime=kelime,
        daire=daire,
        baslangic_tarihi=baslangic_tarihi,
        bitis_tarihi=bitis_tarihi,
        esas_yil=esas_yil,
        esas_ilk_sira_no=esas_ilk_sira_no,
        esas_son_sira_no=esas_son_sira_no,
        karar_yil=karar_yil,
        karar_ilk_sira_no=karar_ilk_sira_no,
        karar_son_sira_no=karar_son_sira_no,
        siralama=siralama,
        siralama_direction=siralama_direction,
        page_size=page_size,
        page_number=page_number
    )

    client = YargitayClient()
    response = await client.detailed_search(criteria)

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
