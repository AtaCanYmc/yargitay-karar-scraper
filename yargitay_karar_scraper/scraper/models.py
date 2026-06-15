from pydantic import BaseModel, Field
from typing import List, Optional, Any


class SearchCriteria(BaseModel):
    kelime: Optional[str] = Field(None, description="Aranacak kelime veya kelime öbeği")
    page_size: int = Field(10, description="Sayfa başı kayıt sayısı")
    page_number: int = Field(1, description="Sayfa numarası")


class DetailedSearchCriteria(BaseModel):
    kelime: Optional[str] = Field("", description="Aranacak kelime")
    daire: Optional[str] = Field("", description="İlgili daire")
    baslangic_tarihi: Optional[str] = Field("", description="Başlangıç Tarihi (GG.AA.YYYY)")
    bitis_tarihi: Optional[str] = Field("", description="Bitiş Tarihi (GG.AA.YYYY)")
    esas_yil: Optional[str] = Field("", description="Esas Yıl")
    esas_ilk_sira_no: Optional[str] = Field("", description="Esas İlk Sıra No")
    esas_son_sira_no: Optional[str] = Field("", description="Esas Son Sıra No")
    karar_yil: Optional[str] = Field("", description="Karar Yıl")
    karar_ilk_sira_no: Optional[str] = Field("", description="Karar İlk Sıra No")
    karar_son_sira_no: Optional[str] = Field("", description="Karar Son Sıra No")
    siralama: str = Field("3", description="Sıralama türü")
    siralama_direction: str = Field("asc", description="Sıralama yönü (asc/desc)")
    page_size: int = Field(10, description="Sayfa başı kayıt sayısı")
    page_number: int = Field(1, description="Sayfa numarası")


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
