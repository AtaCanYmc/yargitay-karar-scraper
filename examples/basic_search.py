import asyncio

# Proje dizininde çalıştırılırken yargitay_karar_scraper modülünün bulunabilmesi için
# sys.path'e eklenebilir (pip install -e . yaptıysanız buna gerek yoktur)
# import sys; sys.path.insert(0, "..")

from yargitay_karar_scraper.scraper import YargitayClient, SearchCriteria


async def main():
    print("Yargıtay Karar Arama (Basit Arama) Örneği\n")

    # 1. İstemciyi oluştur
    client = YargitayClient(timeout=30)

    # 2. Arama kriterlerini belirle
    # Sadece "hırsızlık" kelimesi geçen, 1. sayfadaki ilk 5 kararı getirelim
    criteria = SearchCriteria(
        kelime="hırsızlık",
        page_size=5,
        page_number=1
    )

    print(f"'{criteria.kelime}' kelimesi aranıyor...")

    # 3. İsteği gönder ve yanıtı al
    response = await client.search(criteria)

    if response.error:
        print(f"Hata: {response.error}")
        return

    print(f"\nToplam Bulunan Kayıt: {response.total_count}")
    print("-" * 50)

    for case in response.results:
        print(f"ID: {case.id}")
        print(f"Esas/Karar: {case.esas_no} / {case.karar_no}")
        print(f"Tarih: {case.tarih}")
        print("-" * 50)


if __name__ == "__main__":
    asyncio.run(main())
