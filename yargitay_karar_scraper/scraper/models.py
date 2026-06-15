from pydantic import BaseModel, Field
from typing import List, Optional, Any

class SearchCriteria(BaseModel):
    kelime: Optional[str] = Field(None, description="Aranacak kelime veya kelime öbeği")
    daire: Optional[str] = Field(None, description="İlgili daire (Ör: 1, 2, Ceza, Hukuk vb.)")
    esas_no: Optional[str] = Field(None, description="Esas numarası")
    karar_no: Optional[str] = Field(None, description="Karar numarası")
    mahkeme: Optional[str] = Field(None, description="Mahkeme adı")

class CaseResult(BaseModel):
    id: str = Field(description="Karar doküman ID'si")
    kurum: Optional[str] = Field(None, description="Kurum (Ör: Yargıtay)")
    daire: Optional[str] = Field(None, description="Daire")
    esas_no: Optional[str] = Field(None, description="Esas Numarası")
    karar_no: Optional[str] = Field(None, description="Karar Numarası")
    tarih: Optional[str] = Field(None, description="Karar Tarihi")
    ozet: Optional[str] = Field(None, description="Karar Özeti veya Kısa İçerik")
    
class SearchResponse(BaseModel):
    results: List[CaseResult]
    total_count: int = 0
    error: Optional[str] = None

class CaseDetail(BaseModel):
    id: str = Field(description="Karar doküman ID'si")
    icerik: str = Field(description="Kararın tam metni veya detaylı içeriği")
    error: Optional[str] = None
