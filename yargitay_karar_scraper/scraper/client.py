import httpx
import logging
from typing import Optional, Dict, Any

from .models import SearchCriteria, SearchResponse, CaseResult, CaseDetail

logger = logging.getLogger(__name__)


class YargitayClient:
    """Yargıtay Karar Arama sistemi için HTTP istemcisi."""

    BASE_URL = "https://karararama.yargitay.gov.tr"
    SEARCH_ENDPOINT = f"{BASE_URL}/aramalist"
    DETAIL_SEARCH_ENDPOINT = f"{BASE_URL}/aramadetaylist"
    DOCUMENT_ENDPOINT = f"{BASE_URL}/getDokuman"

    def __init__(self, timeout: int = 30):
        # Gerçekçi bir tarayıcı simülasyonu için User-Agent
        self.headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0.0.0 Safari/537.36"),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json"
        }
        self.timeout = timeout

    async def search(self, criteria: SearchCriteria) -> SearchResponse:
        """Belirtilen kriterlere göre kararları arar."""
        # Gerçek request yapısına göre payload hazırlanması
        data_payload: Dict[str, Any] = {
            "pageSize": 10,
            "pageNumber": 1
        }
        if criteria.kelime:
            data_payload["aranan"] = criteria.kelime
            data_payload["arananKelime"] = criteria.kelime
        if criteria.daire:
            data_payload["daire"] = criteria.daire
        if criteria.esas_no:
            data_payload["esasNo"] = criteria.esas_no
        if criteria.karar_no:
            data_payload["kararNo"] = criteria.karar_no
            
        payload = {"data": data_payload}

        try:
            async with httpx.AsyncClient(timeout=self.timeout, headers=self.headers, verify=False) as client:
                response = await client.post(self.SEARCH_ENDPOINT, json=payload)
                response.raise_for_status()

                # Yanıtın JSON olduğunu varsayıyoruz. 
                # Gerçekte Yargıtay yapısı HTML dönebilir, eğer öyleyse BeautifulSoup eklenip parse edilmeli.
                # Şimdilik JSON modeline uygun varsayarak örnekleme yapıyoruz.
                data = response.json()

                results = []
                # Gerçek JSON yanıt formatına göre ayrıştırma
                response_data = data.get("data", {}) if isinstance(data, dict) else {}
                items = response_data.get("data", []) if isinstance(response_data, dict) else []
                total_count = response_data.get("recordsTotal", len(items)) if isinstance(response_data, dict) else len(items)

                for item in items:
                    if isinstance(item, dict):
                        results.append(CaseResult(
                            id=str(item.get("id", "")),
                            kurum="Yargıtay",
                            daire=item.get("daire", ""),
                            esas_no=item.get("esasNo", ""),
                            karar_no=item.get("kararNo", ""),
                            tarih=item.get("kararTarihi", ""),
                            ozet=item.get("arananKelime", "")
                        ))

                return SearchResponse(results=results, total_count=total_count)

        except httpx.HTTPError as e:
            logger.error(f"HTTP Hatası: {e}")
            return SearchResponse(results=[], error=f"HTTP isteği başarısız: {str(e)}")
        except Exception as e:
            logger.error(f"Beklenmeyen Hata: {e}")
            return SearchResponse(results=[], error=f"Beklenmeyen hata oluştu: {str(e)}")

    async def get_document(self, document_id: str) -> CaseDetail:
        """Belirtilen ID'ye sahip kararın tam metnini getirir."""
        params = {"id": document_id}

        try:
            async with httpx.AsyncClient(timeout=self.timeout, headers=self.headers, verify=False) as client:
                response = await client.get(self.DOCUMENT_ENDPOINT, params=params)
                response.raise_for_status()

                # Gerçek sistemde bu PDF veya HTML olabilir.
                content = response.text

                return CaseDetail(id=document_id, icerik=content)

        except httpx.HTTPError as e:
            logger.error(f"Doküman getirme HTTP Hatası: {e}")
            return CaseDetail(id=document_id, icerik="", error=f"Doküman çekilemedi: {str(e)}")
        except Exception as e:
            logger.error(f"Beklenmeyen Hata: {e}")
            return CaseDetail(id=document_id, icerik="", error=f"Beklenmeyen hata oluştu: {str(e)}")
