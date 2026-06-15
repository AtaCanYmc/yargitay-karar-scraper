import asyncio
from yargitay_karar_scraper.scraper import YargitayClient


async def main():
    print("Yargıtay Karar Arama (Doküman Detayı Çekme) Örneği\n")

    client = YargitayClient()

    # Doküman ID'si (Arama sonuçlarından alınmış örnek bir ID)
    # Burada sizin sağladığınız "120109100" ID'sini kullanıyoruz.
    document_id = "120109100"

    print(f"ID'si '{document_id}' olan karar çekiliyor...\n")

    response = await client.get_document(document_id)

    if response.error:
        print(f"Hata: {response.error}")
        return

    print("--- KARAR İÇERİĞİ ---")
    print(response.icerik)
    print("\n--- SON ---")


if __name__ == "__main__":
    asyncio.run(main())
