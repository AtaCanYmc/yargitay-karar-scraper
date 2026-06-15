import asyncio
from yargitay_karar_scraper.scraper import YargitayClient, DetailedSearchCriteria


async def main():
    print("Yargıtay Karar Arama (Detaylı Arama) Örneği\n")

    client = YargitayClient()

    # Detaylı arama parametreleri
    # Örnek: "1. Ceza Dairesi"nin, 2015 ile 2018 yılları arasındaki "hırsızlık" kelimesi geçen kararları
    criteria = DetailedSearchCriteria(
        kelime="hırsızlık",
        daire="1. Ceza Dairesi",
        baslangic_tarihi="",
        bitis_tarihi="",
        esas_yil="2015",
        karar_yil="2018",
        siralama="3",  # Yargıtay'ın kullandığı özel sıralama parametresi
        siralama_direction="desc",  # Yeniden eskiye sırala
        page_size=10,
        page_number=1
    )

    print("Kriterler ile arama yapılıyor...")
    response = await client.detailed_search(criteria)

    if response.error:
        print(f"Hata: {response.error}")
        return

    print(f"\nToplam {response.total_count} kayıt bulundu.")
    print("=" * 60)

    for case in response.results:
        print(f"Karar ID: {case.id}")
        print(f"Daire: {case.daire}")
        print(f"Esas / Karar: {case.esas_no} / {case.karar_no}")
        print(f"Tarih: {case.tarih}")
        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
