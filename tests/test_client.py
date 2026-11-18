import pytest
from unittest.mock import patch, AsyncMock
import httpx
from yargitay_karar_scraper.scraper import YargitayClient, SearchCriteria, DetailedSearchCriteria


def test_client_initialization_default():
    client = YargitayClient()
    assert client.verify is True
    assert client.timeout == 30
    assert "User-Agent" in client.headers


def test_client_initialization_custom_verify():
    client = YargitayClient(timeout=15, verify=False)
    assert client.verify is False
    assert client.timeout == 15


@pytest.mark.asyncio
async def test_search_uses_verify():
    client = YargitayClient(verify=True)
    criteria = SearchCriteria(kelime="test", page_size=5, page_number=1)

    mock_response = httpx.Response(
        200,
        request=httpx.Request("POST", "https://karararama.yargitay.gov.tr/aramalist"),
        json={
            "data": {
                "data": [
                    {
                        "id": "123",
                        "daire": "1. Ceza Dairesi",
                        "esasNo": "2020/1",
                        "kararNo": "2021/1",
                        "kararTarihi": "01.01.2021",
                        "arananKelime": "test"
                    }
                ],
                "recordsTotal": 1
            }
        }
    )

    with patch("httpx.AsyncClient") as mock_client_cls:
        mock_instance = AsyncMock()
        mock_instance.post.return_value = mock_response
        mock_instance.__aenter__.return_value = mock_instance
        mock_instance.__aexit__.return_value = None
        mock_client_cls.return_value = mock_instance

        resp = await client.search(criteria)

        mock_client_cls.assert_called_once_with(
            timeout=30,
            headers=client.headers,
            verify=True
        )
        assert resp.total_count == 1
        assert len(resp.results) == 1
        assert resp.results[0].id == "123"
        assert resp.results[0].daire == "1. Ceza Dairesi"


@pytest.mark.asyncio
async def test_get_document_html_cleaning():
    client = YargitayClient(verify=True)
    mock_response = httpx.Response(
        200,
        request=httpx.Request("GET", "https://karararama.yargitay.gov.tr/getDokuman"),
        json={
            "data": "<p>Karar Metni &amp; Gerek&ccedil;e</p><div>Detaylar</div>"
        }
    )

    with patch("httpx.AsyncClient") as mock_client_cls:
        mock_instance = AsyncMock()
        mock_instance.get.return_value = mock_response
        mock_instance.__aenter__.return_value = mock_instance
        mock_instance.__aexit__.return_value = None
        mock_client_cls.return_value = mock_instance

        detail = await client.get_document("123")

        mock_client_cls.assert_called_once_with(
            timeout=30,
            headers=client.headers,
            verify=True
        )
        assert detail.id == "123"
        assert "Karar Metni & Gerekçe Detaylar" in detail.icerik

